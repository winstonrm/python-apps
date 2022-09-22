import pyautogui as gui
import pydirectinput as direct
import time
import keyboard as key

opcao_bot = input('Bot(Quests) = 1; Bot(Farm ingrediente) = 2; Bot(Farm+Especial a cada 140s) = 3')

if opcao_bot == '1':
    icon_pular = ''
    icon_missao_concluida  = ''
    icon_nova_quest = ''
    icon_aceita = ''
    icon_missao_principal = ''
    icon_missao_principal2 = ''
    icon_avancar_diag = ''
    icon_levantar = '' 
    icon_confirmar = ''
    icon_continuar = ''
    icon_mao_fonte = ''
    icon_avancar_fast = ''
    local_img = 'C:/wprojetos/python/WebScraping/project1/img-pyautogui/'

    def ini_memoria():
        global icon_pular
        global icon_missao_concluida
        global icon_nova_quest
        global icon_aceita
        global icon_missao_principal
        global icon_missao_principal2
        global icon_avancar_diag
        global icon_levantar
        global icon_confirmar
        global icon_continuar
        global local_img
        global icon_mao_fonte
        global icon_avancar_fast
        icon_pular = gui.locateOnScreen(r''+local_img + 'pular.png', grayscale=True, confidence=0.9)
        icon_missao_concluida = gui.locateOnScreen(r''+local_img + 'missao_concluida.png', grayscale=True, confidence=0.9)
        icon_nova_quest = gui.locateOnScreen(r''+local_img + 'nova_quest.png', grayscale=True, confidence=0.9)
        icon_aceita = gui.locateOnScreen(r''+local_img + 'aceitar.png', grayscale=True, confidence=0.9)
        icon_missao_principal = gui.locateOnScreen(r''+local_img + 'missao_principal.png', grayscale=True, confidence=0.9)
        # icon_missao_principal2 = gui.locateOnScreen(r''+local_img + 'missao_principal2.png', grayscale=True, confidence=0.9)
        icon_avancar_diag = gui.locateOnScreen(r''+local_img + 'avancar_dialogo.png', grayscale=True, confidence=0.9)
        icon_levantar = gui.locateOnScreen(r''+local_img + 'levantar.png', grayscale=True, confidence=0.9)
        icon_confirmar = gui.locateOnScreen(r''+local_img + 'confirmar.png', grayscale=True, confidence=0.9)
        icon_continuar = gui.locateOnScreen(r''+local_img + 'continuar.png', grayscale=True, confidence=0.9)
        icon_mao_fonte = gui.locateOnScreen(r''+local_img + 'mao_fonte.png', grayscale=True, confidence=0.9)
        icon_avancar_fast = gui.locateOnScreen(r''+local_img + 'avancar_fast.png', grayscale=True, confidence=0.9)
        
    def identifica(nome_icon, icon):
        if nome_icon == 'NEXT':
            print("%s%s" % (nome_icon, icon))
            gui.click(icon)    
            time.sleep(0.2)
            gui.moveTo(300,300)
        elif nome_icon == 'MISSAO_PRINCIPAL':
            print("%s%s" % (nome_icon, icon))
            gui.click(icon)    
            time.sleep(0.2)
        else:
            print("%s%s" % (nome_icon, icon))
            gui.click(icon)    
            time.sleep(0.6)
            gui.moveTo(300,300)

    try:
        print('Executando')
        while key.is_pressed('c')==False:    
            ini_memoria()
            if icon_missao_principal:
                identifica('MISSAO_PRINCIPAL', icon_missao_principal)
            # elif icon_missao_principal:
            #     identifica('MISSAO_PRINCIPAL2 ', icon_missao_principal2)
            elif icon_pular:
                identifica('PULAR ', icon_pular)   
            elif icon_avancar_fast:
                identifica('NEXT ', icon_avancar_fast)
            elif icon_mao_fonte:
                identifica('FONTE ', icon_mao_fonte)    
            elif icon_levantar:
                identifica('LEVANTAR ', icon_levantar)
            elif icon_confirmar:
                identifica('CONFIRMAR ', icon_confirmar)
            elif icon_continuar:
                identifica('CONTINUAR ', icon_continuar)
            elif icon_missao_concluida:
                identifica('MISSAO_CONCLUIDA ', icon_missao_concluida) 
            elif icon_nova_quest:
                identifica('NOVA_QUEST ', icon_nova_quest) 
            elif icon_aceita:
                identifica('ACEITAR ', icon_aceita)
            else:
                print('Outro')
                time.sleep(0.5)
                gui.click(80,202)
                gui.moveTo(300,300)
                # direct.click()

    except KeyboardInterrupt:
        print('\nPrograma Fechado')
elif opcao_bot == '2':
    try:
        print('Executando')
        while key.is_pressed('c')==False:    
            gui.click(1606,814)    
            time.sleep(3)
    except KeyboardInterrupt:
        print('\nPrograma Fechado')
elif opcao_bot == '3':
    try:
        print('Executando')
        while key.is_pressed('c')==False:  
            gui.click(1700,653)    
            time.sleep(145)
    except KeyboardInterrupt:
        print('\nPrograma Fechado')