from tkinter import * # type: ignore
from random import randint
from pyautogui import confirm # type: ignore
from os import system


try:
    system('cls')
except:
    system('clear')

def imagensCriar():
    global imagemBomba, imagemBombaErrada, imagemBombaPerda, imagemBotaoNada, imagemBandeira, imagensNumeros

    # bg='gray75'
    try:
        imagemN1 = PhotoImage(file='imagens/N1.png')
    except:
        imagemN1 = PhotoImage(file='campo_minado.py/imagens/N1.png')
    try:
        imagemN2 = PhotoImage(file='imagens/N2.png')
    except:
        imagemN2 = PhotoImage(file='campo_minado.py/imagens/N2.png')
    try:
        imagemN3 = PhotoImage(file='imagens/N3.png')
    except:
        imagemN3 = PhotoImage(file='campo_minado.py/imagens/N3.png')
    try:
        imagemN4 = PhotoImage(file='imagens/N4.png')
    except:
        imagemN4 = PhotoImage(file='campo_minado.py/imagens/N4.png')
    try:
        imagemN5 = PhotoImage(file='imagens/N5.png')
    except:
        imagemN5 = PhotoImage(file='campo_minado.py/imagens/N5.png')
    try:
        imagemN6 = PhotoImage(file='imagens/N6.png')
    except:
        imagemN6 = PhotoImage(file='campo_minado.py/imagens/N6.png')
    try:
        imagemN7 = PhotoImage(file='imagens/N7.png')
    except:
        imagemN7 = PhotoImage(file='campo_minado.py/imagens/N7.png')
    try:
        imagemN8 = PhotoImage(file='imagens/N8.png')
    except:
        imagemN8 = PhotoImage(file='campo_minado.py/imagens/N8.png')

    try:
        imagemBomba = PhotoImage(file='imagens/bomba.png')
    except:
        imagemBomba = PhotoImage(file='campo_minado.py/imagens/bomba.png')
    try:
        imagemBombaErrada = PhotoImage(file='imagens/bombaErrada.png')
    except:
        imagemBombaErrada = PhotoImage(file='campo_minado.py/imagens/bombaErrada.png')
    try:
        imagemBombaPerda = PhotoImage(file='imagens/bombaPerda.png')
    except:
        imagemBombaPerda = PhotoImage(file='campo_minado.py/imagens/bombaPerda.png')
    try:
        imagemBotaoNada = PhotoImage(file='imagens/botaoNada.png')
    except:
        imagemBotaoNada = PhotoImage(file='campo_minado.py/imagens/botaoNada.png')
    try:
        imagemBandeira = PhotoImage(file='imagens/bandeira.png')
    except:
        imagemBandeira = PhotoImage(file='campo_minado.py/imagens/bandeira.png')

    imagensNumeros = [imagemN1, imagemN2, imagemN3, imagemN4, imagemN5, imagemN6, imagemN7, imagemN8]

def linguagem(lingua):
    global txtDifi, txtDifi2, difiB, txtS, txtR, txtB, txtIB, txtV, txtD, titulo

    txtDifi = 'Dificuldade' if lingua == 'Português' else 'Difficulty'
    txtDifi2 = 'Clique na dificuldade desejada:' if lingua == 'Português' else 'Click on the desired difficulty:'
    difiB = ['Fácil', 'Médio', 'Difícil'] if lingua == 'Português' else ['Easy', 'Medium', 'Hard']
    txtS = 'SAIR' if lingua == 'Português' else 'LEAVE'
    txtR = 'RECOMEÇAR' if lingua == 'Português' else 'RESTART'
    txtB = 'BANDEIRA' if lingua == 'Português' else 'FLAG'
    txtIB = 'Info e botões' if lingua == 'Português' else 'Info and buttons'
    txtV = 'Você ganhou!' if lingua == 'Português' else 'You won!'
    txtD = 'Você perdeu!' if lingua == 'Português' else 'You lost!'
    titulo = 'Campo Minado' if lingua == 'Português' else 'Minefield'

lang = ''
def configsIniciais():
    global janela, totalBombas, tabuleiro, tamanhoBotão, saida, aN, lN, totalBandeiras, largura, altura, fim, lang

    saida = False
    fim = False
    while True:
        if lang == '':
            respL = confirm(title='Language', text='English or português', buttons=[ 'Português', 'English'])
            if respL == None:
                saida = True
                break
            else:
                lang = respL
                linguagem(respL)

        respD = confirm(title=txtDifi, text=txtDifi2, buttons=difiB)
        if respD == None:
            saida = True
            break
        # tamanho do tabuleiro
        if respD == difiB[0]:
            #            Y, X
            tabuleiro = [9, 9]
            totalBombas = 10
            aN = 175
            lN = 157
        elif respD == difiB[1]:
            tabuleiro = [16, 16]
            totalBombas = 40
            aN = 295
            lN = 280
        else:
            tabuleiro = [16, 30]
            totalBombas = 99
            aN = 295
            lN = 525
        totalBandeiras = totalBombas
        # abrir a janela
        janela = Tk()
        janela.resizable(False, False)
        try:
            icone = PhotoImage(file='imagens/iconecampominado.png')
        except:
            icone = PhotoImage(file='campo_minado.py/imagens/iconecampominado.png')
        janela.iconphoto(False, icone)
        # pegando altura e largura
        altura, largura = int(janela.winfo_screenheight()/2) - aN, int(janela.winfo_screenwidth()/2) - lN
        # criar as imagens
        imagensCriar()
        # titulo da janela
        janela.title(titulo)
        # tamanho do botao
        tamanhoBotão = 35
        # x e y da janela
        y, x = tabuleiro[0] * tamanhoBotão, tabuleiro[1] * tamanhoBotão
        # tamanho da tela
        janela.geometry(f'{x}x{y}+{largura}+{altura}')
        criarJanela2()
        break

def criarJanela2():
    global janela2, bandeiraAD, campoBotoes, txtBombas

    janela2 = Tk()
    janela2.resizable(False, False)
    janela2.title(txtIB)
    janela2.geometry(f'360x70+{largura+lN-180}+{altura-75}')
    janela2.attributes('-topmost', True)
    bandeiraAD = False

    def destroyJ():
        try:
            janela2.destroy()
            janela.destroy()
        except:
            pass
    def recomecar():
        destroyJ()
        configsIniciais()
        if not saida:
            criarBotoes()
    def bandeira(botao):
        global bandeiraAD

        if not fim:
            if botao['text'] == f'{txtB} / ON':
                botao['text'] = f'{txtB} / OFF'
                bandeiraAD = False
            else:
                botao['text'] = f'{txtB} / ON'
                bandeiraAD = True
    def resetarBandeiras():
        global campoBotoes, totalBandeiras

        try:
            if not fim and janela.state():
                for x in range(tabuleiro[0]):
                    for y in range(tabuleiro[1]):
                        if campoBotoes[x][y]['image'] == str(imagemBandeira):
                            campoBotoes[x][y]['image'] = imagemBotaoNada
                totalBandeiras = totalBombas
                txtBombas['text'] = f'{totalBandeiras}'
        except:
            pass

    txtSair = Button(janela2, text=txtS, fg='black', bg='red3', font='Impact', activebackground='red4', command=destroyJ)
    txtSair.place(x=0, y=0, height=35, width=120)
    txtRecomecar = Button(janela2, text=txtR, fg='black', bg='green3', font='Impact', activebackground='green', command=recomecar)
    txtRecomecar.place(x=120, y=0, height=35, width=120)
    txtBandeira = Button(janela2, text=f'{txtB} / OFF', fg='black', bg='red2', font='Impact', activebackground='red3')
    txtBandeira['command'] = lambda botao = txtBandeira: bandeira(botao)
    txtBandeira.place(x=240, y=0, height=35, width=120)
    txtDesfazerBandeiras = Button(janela2, text=f'{txtB}S RESET', fg='black', bg='blue', font='Impact', activebackground='blue3', command=resetarBandeiras)
    txtDesfazerBandeiras.place(x=240, y=35, height=35, width=120)
    txtBandeira.place(x=240, y=0, height=35, width=120)
    txtBombas = Label(janela2, text=f'{totalBandeiras}', font=('Impact', 30), fg='red', bg='black')
    txtBombas.place(x=120, y=35, height=35, width=120)
    fundoPreto = Label(janela2, bg='black')
    fundoPreto.place(x=0, y=35, height=35, width=120)

def verificarNumerosCampoBombas(x, y):
    global campoBombas

    for a in range(9):
        try:
            if campoBombas[x][y][0] == a:
                campoBombas[x][y][0] += 1
                campoBombas[x][y][1] = imagensNumeros[a]
                break
        except:
            pass

def criarBombas(l, c):
    global campoBombas

    z = 1
    while z <= totalBombas:
        n1 = randint(0, tabuleiro[0]-1)
        n2 = randint(0, tabuleiro[1]-1)
        
        if campoBombas[n1][n2][1] == '💣' or (n1, n2) == (l, c):
            continue
        campoBombas[n1][n2][1] = '💣'
        campoBombas[n1][n2][0] = -1
        for a in range(n1-1, n1+2):
            for b in range(n2-1, n2+2):
                if a >= 0 and b >= 0:
                    verificarNumerosCampoBombas(a, b)
        z += 1

def criarBotoes():
    global campoBombas, campoBotoes, tentativa

    campoBombas = [[[0, ''] for x in range(tabuleiro[1])] for x in range(tabuleiro[0])]
    campoBotoes = [[] for x in range(tabuleiro[0])]
    tentativa = 0
    for l in range(tabuleiro[0]):
        for c in range(tabuleiro[1]):
            posX = c*tamanhoBotão
            posY = l*tamanhoBotão
            b = Button(janela, activebackground='gray75', bg='gray90', image=imagemBotaoNada)
            b['command'] = lambda linha = l, coluna = c: clicar(linha, coluna)
            b.place(x=posX, y=posY, height=tamanhoBotão, width=tamanhoBotão)
            campoBotoes[l].append(b)

def mostrarGP(gp, linha, coluna):
    for x in range(tabuleiro[0]):
        for y in range(tabuleiro[1]):
            campoBotoes[x][y]['state'] = DISABLED
            if campoBombas[x][y][1] == '💣' and gp == 'p' and campoBotoes[x][y]['image'] != str(imagemBandeira):
                if (x, y) == (linha, coluna):
                    campoBotoes[x][y]['bg'] = 'red'
                    j = Label(janela, image=imagemBombaPerda, bg='red')
                else:
                    campoBotoes[x][y]['bg'] = 'gray75'
                    j = Label(janela, image=imagemBomba, bg='gray75')
            else:
                if campoBotoes[x][y]['image'] == str(imagemBotaoNada):
                    j = Label(janela, image=imagemBotaoNada, bg='gray75')
                elif campoBotoes[x][y]['image'] == '':
                    continue
                elif campoBotoes[x][y]['image'] == str(imagemBandeira) and campoBombas[x][y][1] != '💣':
                    # campoBotoes[x][y]['image'] = imagemBombaErrada
                    j = Label(janela, image=imagemBombaErrada, bg='gray75')
                elif campoBotoes[x][y]['image'] == str(imagemBandeira):
                    j = Label(janela, image=imagemBandeira, bg='gray75')
                else:
                    j = Label(janela, image=campoBombas[x][y][1], bg='gray75')
            j.place(x=y*35, y=x*35, height=33, width=33)
    textoGP = [txtV, 'green2'] if gp == 'g' else [txtD, 'red']
    j = Label(janela, text=textoGP[0], font=('Impact', 24), fg=textoGP[1], bg='gray75')
    if txtV == 'You won!':
        j.place(x=lN-57, y=aN-39)
    else:
        j.place(x=lN-90, y=aN-39)

def verificarZeros():
    global campo

    for az in range(10):
        for x in range(tabuleiro[0]):
            for y in range(tabuleiro[1]):
                if campoBotoes[x][y]['image'] == '':
                    for a in range(x-1, x+2):
                        for b in range(y-1, y+2):
                            if a >= 0 and b >= 0:
                                try:
                                    if campoBotoes[a][b]['image'] == str(imagemBandeira):
                                        continue
                                    campoBotoes[a][b].config(image=campoBombas[a][b][1], bg='gray75')
                                    if campoBotoes[a][b]['image'] == '':
                                        campoBotoes[a][b]['state'] = DISABLED
                                except:
                                    pass

def verificarEmVolta(n1, n2):
    global bnd, bmb, fim

    bnd = 0
    bmb = 0
    for x in range(n1-1, n1+2):
        for y in range(n2-1, n2+2):
            if x >= 0 and y >= 0:
                trysVerificarEmVolta(x, y)

    if bnd == campoBombas[n1][n2][0]:
        if bmb >= 1:
            return False
        else:
            for x in range(n1-1, n1+2):
                for y in range(n2-1, n2+2):
                    if x >= 0 and y >= 0:
                        try:
                            if campoBotoes[x][y]['image'] == str(imagemBotaoNada):
                                campoBotoes[x][y].config(image=campoBombas[x][y][1], bg='gray75')
                        except:
                            pass
            verificarZeros()

    return True

def trysVerificarEmVolta(x, y):
    global bnd, bmb

    try:
        if campoBotoes[x][y]['image'] == str(imagemBandeira):
            bnd += 1
        elif campoBombas[x][y][1] == '💣':
            bmb += 1
    except:
        pass

def verificarGanho():
    b = 0

    for x in campoBotoes:
        for y in x:
            if y['image'] == str(imagemBotaoNada) or y['image'] == str(imagemBandeira):
                b += 1
    return b

def clicar(linha, coluna):
    global tentativa, totalBandeiras, fim

    try:
        janela2.state()
    except:
        criarJanela2()

    t = False
    if tentativa == 0:
        criarBombas(linha, coluna)
        tentativa = 1
    if campoBombas[linha][coluna][1] == '💣' and campoBotoes[linha][coluna]['image'] != str(imagemBandeira) and not bandeiraAD:
        mostrarGP('p', linha, coluna)
        fim = True
        return
    elif bandeiraAD:
        t = True
        for j in imagensNumeros:
            if campoBotoes[linha][coluna]['image'] == str(j):
                break
        else:
            if campoBotoes[linha][coluna]['image'] == str(imagemBandeira):
                campoBotoes[linha][coluna]['image'] = imagemBotaoNada
                totalBandeiras += 1
            else:
                totalBandeiras -= 1
                campoBotoes[linha][coluna]['image'] = imagemBandeira
    elif campoBombas[linha][coluna][0] == 0:
        campoBotoes[linha][coluna].config(image='', bg='gray75', state=DISABLED)
        verificarZeros()
    for j in imagensNumeros:
        if campoBotoes[linha][coluna]['image'] == str(j):
            if not verificarEmVolta(linha, coluna):
                mostrarGP('p', linha, coluna)
                fim = True
            break
    if campoBotoes[linha][coluna]['image'] != str(imagemBandeira) and not t:
        campoBotoes[linha][coluna].config(image=campoBombas[linha][coluna][1], bg='gray75')
        if not verificarEmVolta(linha, coluna):
            mostrarGP('p', linha, coluna)
            fim = True
    if verificarGanho() == totalBombas:
        mostrarGP('g', linha, coluna)
        fim = True
    txtBombas['text'] = f'{totalBandeiras}'


configsIniciais()
if not saida: # type: ignore
    criarBotoes()


try:
    janela.mainloop() # type: ignore
    janela2.mainloop() # type: ignore
except:
    pass