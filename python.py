# Passo a passo
# P1: entrar no sistema da empresa(link)
# P2: fazer login
# P3: exportar base de dados
# P4: calcular indicadores
# P5: enviar o e-mail para o chefe

import pyautogui as py
import time
py.PAUSE = 0.5
py.hotkey('alt', 'tab')
py.press('enter')
py.hotkey('ctrl', 't')
py.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
py.press('enter')
time.sleep(5)
py.click(x=608, y=369)
py.write('Thiago_login')
py.press('tab')
py.write('327832')
py.press('tab')
py.press('enter')
time.sleep(5)
py.click(x=1259, y=329)
time.sleep(2)
py.click(x=1088, y=417)

# Cálculo da base de dados
import pandas as pd
tabela = pd.read_csv(r"Compras.csv", sep= ";")
display(tabela)
total_gasto = tabela["ValorFinal"].sum()
qntd = tabela["Quantidade"].sum()
preço_médio = total_gasto / qntd
print('O total gasto foi de {:.2f}'.format(total_gasto))
print(qntd)
print(preço_médio)

# entrar no email
# fazer o login ou só entrar na pagina
import pyperclip as pp
import pyautogui as py
import time
py.PAUSE = 1
#py.hotkey('alt','tab')
#py.press('enter')
py.hotkey('ctrl','t')
py.write('https://mail.google.com/mail/u/0/#inbox')
py.press('enter')
time.sleep(5)
py.click(x=69, y=185)
time.sleep(3)
py.write('thiago.ribeiro.14@hotmail.com')
py.press('enter')
py.press('tab')
pp.copy('Relatório de Vendas')
py.hotkey('ctrl', 'v')
py.press('tab')

texto = f"""
Chefe segue as informações das vendas 
Total gasto: R${total_gasto:,.2f}
Quantidade vendida: {qntd:,.2f}
Preço Médio: R${preço_médio:,.2f}
att, Thiago Ribeiro
"""
pp.copy(texto)
py.hotkey('ctrl', 'v')
py.hotkey('ctrl', 'enter')