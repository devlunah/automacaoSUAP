Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
texto = "Total de 1 item"
texto
'Total de 1 item'
for t in texto:
    t

    
'T'
'o'
't'
'a'
'l'
' '
'd'
'e'
' '
'1'
' '
'i'
't'
'e'
'm'
for t in texto:
    if t.isdigit
    
SyntaxError: expected ':'
num = 0
for t in texto:
    if t.isdigit:
        num = t

        
num
'm'
for t in texto:
    t.isdigit
    if t.isdigit:
        num = t

        
<built-in method isdigit of str object at 0x00007FF9CDC11D70>
<built-in method isdigit of str object at 0x00007FF9CDC12280>
<built-in method isdigit of str object at 0x00007FF9CDC12370>
<built-in method isdigit of str object at 0x00007FF9CDC11FE0>
<built-in method isdigit of str object at 0x00007FF9CDC121F0>
<built-in method isdigit of str object at 0x00007FF9CDC113B0>
<built-in method isdigit of str object at 0x00007FF9CDC12070>
<built-in method isdigit of str object at 0x00007FF9CDC120A0>
<built-in method isdigit of str object at 0x00007FF9CDC113B0>
<built-in method isdigit of str object at 0x00007FF9CDC116E0>
<built-in method isdigit of str object at 0x00007FF9CDC113B0>
<built-in method isdigit of str object at 0x00007FF9CDC12160>
<built-in method isdigit of str object at 0x00007FF9CDC12370>
<built-in method isdigit of str object at 0x00007FF9CDC120A0>
<built-in method isdigit of str object at 0x00007FF9CDC12220>
for t in texto:
    t.isdigit()
    if t.isdigit():
        num = t

        
False
False
False
False
False
False
False
False
False
True
False
False
False
False
False
num
'1'
for t in texto:
    t.isdigit()
    if t.isdigit():
        num = int(t)

        
False
False
False
False
False
False
False
False
False
True
False
False
False
False
False
>>> num
1
>>> lista = [for t in texto]
SyntaxError: invalid syntax
>>> lista = [t for t in texto]
>>> lista
['T', 'o', 't', 'a', 'l', ' ', 'd', 'e', ' ', '1', ' ', 'i', 't', 'e', 'm']
>>> lista = [t for t in texto if t.isdigit()]
>>> lista
['1']
>>> lista = [int(t) for t in texto if t.isdigit()]
>>> lista
[1]
>>> lista[0]
1
>>> lista = [int(t) for t in texto if t.isdigit()][0]
>>> lista
1
>>> lista = {'num':int(t) for t in texto if t.isdigit()}
>>> lista
{'num': 1}
>>> lista.get('num')
1
>>> lista.get('nu5m')
>>> lista.get('nu5m', 0)
0
>>> lista.get('num', 0)
1

#---------------------------------------------------------------------------------------------------------
#try:
            #     item = pagina.locator("#chamados .accordion-body ul.pagination li.disabled").first

            #     item.wait_for(state="visible")
            #     texto = item.inner_text()   # ex: "Total de 1 item"

            # except TimeoutError:
            #     texto = "Total de 0 item"
            #     quant_chamados = 0
            #     print(f"Não há chamados.")

            # item = pagina.locator("#chamados .accordion-body ul.pagination li.disabled").first

            # item.wait_for(state="visible")
            # texto = item.inner_text()   # ex: "Total de 1 item"

            # quant_chamados = int("".join(filter(str.isdigit, texto_inicial)))
            # print(f"Total de Chamados: {quant_chamados}")

#Se não, verificar a quantidade chamados existentes:
    # item = pagina.locator("#chamados .accordion-body ul.pagination li.disabled").first

    # item.wait_for(state="visible")
    # texto_inicial = item.inner_text()   # ex: "Total de 1 item"

    # quant_chamados_inicial = int("".join(filter(str.isdigit, texto_inicial)))
    # print(f"Total de Chamados: {quant_chamados_inicial}")