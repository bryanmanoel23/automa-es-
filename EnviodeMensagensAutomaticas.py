import pyautogui as pg
from time import sleep 

#clicar em pesquisar
pg.click(130,746, duration=1)
#escrever whastapp
pg.write('whatsApp')
#clicar em abrir
pg.click(464,353, duration=1)
#clicar em procura 
pg.click(119,120, duration=1)
#escrever o nome da conversa para envio dos dados 
pg.write('grupo para teste')
#Clicar na conversa 
pg.click(214,175, duration=1)
#clicar no local de envio de mensagem
pg.click(572,702, duration=1) 
#escrever a mensagem 
pg.write('oi, tudo bem ?')
#enter
pg.hotkey('enter')
#clicar no local de envio de mensagem
pg.click(572,702, duration=1) 
#escrever a mensagem 
pg.write('Por aqui consigo escrever qualquer mensagem ! ')
#enter
pg.hotkey('enter')
#clicar no local de envio de mensagem
pg.click(572,702, duration=1) 
#escrever a mensagem 
pg.write('Boa sorte')
#enter
pg.hotkey('enter')
