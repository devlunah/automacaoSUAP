
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError, Page
from flask import Flask, redirect
from winotify import Notification, audio
import os, time, threading

# Importação do usuário e senha definido no arquivo .env
load_dotenv("config.env")

usuario = os.environ["SUAP_USUARIO"]
senha = os.environ["SUAP_SENHA"]

if not usuario or not senha:
    raise ValueError("Usuário ou senha não definidos nas variáveis de ambiente.")

# Flask App para capturar clique
app = Flask(__name__)
clique_na_notificacao = False

@app.route("/notificacao-clicada")
def notificacao_clicada():
    global clique_na_notificacao
    clique_na_notificacao = True
    print("🟢 O botão da notificação foi clicado!")
    return redirect("https://suap.ifac.edu.br/centralservicos/listar_chamados_suporte/")

def iniciar_flask():
    app.run(port=5000, use_reloader=False)

threading.Thread(target=iniciar_flask, daemon=True).start()

# Variavel para tratamento das exceções:
parar = False

# Função para pegar a quantidade de chamados:
def total_chamados(pagina: Page, timeout: float = 5_000) -> int:
    
    try:
        #Total de chamados
        # seleciona o <li class="disabled"> dentro de <ul class="pagination"> dentro de <div id="chamados">

        item = pagina.locator("#chamados .accordion-body ul.pagination li.disabled").first

        item.wait_for(state="visible", timeout=timeout)
        texto = item.inner_text()   # ex: "Total de 1 item"
        return int("".join(filter(str.isdigit, texto)) or 0)
    
    except TimeoutError:
        return 0
    

with sync_playwright() as pw:
    try:

        navegador = pw.chromium.launch() #headless=False
        contexto = navegador.new_context()
        pagina = contexto.new_page() 

        pagina.goto("https://suap.ifac.edu.br/accounts/login/?next=/centralservicos/listar_chamados_suporte/")

        pagina.get_by_role("textbox", name="Usuário:").click()
        pagina.get_by_role("textbox", name="Usuário:").fill(usuario)
        
        pagina.get_by_role("textbox", name="Senha:").click()
        pagina.get_by_role("textbox", name="Senha:").fill(senha)

        botaoAcessar = pagina.get_by_role("button", name="Acessar").click()

        total_chamados_inicial = total_chamados(pagina)
        print(f"Total Inicial: {total_chamados_inicial}")

        #Loop para recarregar a cada 30s e verificar a quantidade de chamados:
        while True:
            time.sleep(30)      
            pagina.reload()
            total_chamados_atual = total_chamados(pagina)
            print(f"Total chamados: {total_chamados_atual}")

            if total_chamados_inicial is not None and total_chamados_atual is not None and total_chamados_atual > total_chamados_inicial:
                notificacao = Notification(app_id="SUAP",
                                title="Novo chamado detectado!",
                                msg="Verifique o SUAP agora.")  
                notificacao.set_audio(audio.Default, loop=False)
                notificacao.add_actions(label="Ir para SUAP", launch="http://localhost:5000/notificacao-clicada")
                notificacao.show()

                if clique_na_notificacao == True:
                    total_chamados_inicial = total_chamados_atual
                    clique_na_notificacao = False
            else:
                total_chamados_inicial = total_chamados_atual

    except KeyboardInterrupt:
        print("Finalizando o programa...")
        parar = True
    
    except Exception as e:
        notificacao = Notification(app_id="Python",
                        title="Erro na automação",
                        msg="Verificar")  
        notificacao.set_audio(audio.Default, loop=False)
        notificacao.show()
        print(f"Erro durante a automação: {e}")
        input("Pressione Enter para sair...")
        parar = True

    finally:
        botaoSair = pagina.locator("#mainmenu").get_by_role("link", name="Sair")
        botaoSair.click()
        navegador.close() 
