#comandos de instalação
#pip install playwright
#playwright install


#abrir um navegador
from playwright.sync_api import sync_playwright #  playwright.sync_api -> biblioteca que armazena informações para o python // sync_playwright -> permite criar o navegador

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page() 

    #navegar para uma página
    pagina.goto("https://suap.ifac.edu.br/")

    #pegar infos da pagina

    #selecionar um elemento:
    #1ª forma - xpath (menos recomendada)
    pagina.locator("xpath=//*[@id='id_username']").click()
    #2ª forma - get_by (mais recomendado)
    pagina.get_by_role("textbox", name="Usuário:").click()

    #preencher formulário
    pagina.get_by_role("textbox", name="Usuário:").fill("3466829")
    
    pagina.get_by_role("textbox", name="Senha:").click()

    #preencher formulário
    pagina.get_by_role("textbox", name="Senha:").fill("221205#Lu")

    #para botões que ao clicar entram em uma nova página, o recomendado é:
    botaoAcessar = pagina.get_by_role("button", name="Acessar")

    with contexto.expect_page() as pagina_inicial:
        botaoAcessar.click()

    pagina_inicial = pagina_inicial.value


    # fechar o navegador
    navegador.close() 


#infos:

#por padrão, o playwright abre o navegador no modo headless
    # para alterar isso (ou seja, abrir o navegador e mostrar): navegador = pw.chromium.launch(headless=false)

# codigo no cmd para pegar os get_by:
    #playwright codegen link_para_acessar

#contexto
    #permite gerenciar várias páginas

#esperar elementos carregarem:
    #(não é tão necessário, pois o playwright já está lendo toda a página e espera 5 minutos para achar o elemento)
    #from playwright.sync_api import expect
    #expect(elemento).to_be_visible()
