# Feito por Leoxy (https://github.com/LeoxyOF)

def inicio():
    print("\033[1;34m-" * 40)
    print("JODO DA FORCA".center(40))
    print("-" * 40)
    print("\033[m")
    print("\033[32mNível 1 - Muito Fácil ")
    print("\033[32mNível 2 - Fácil")
    print("\033[33mNível 3 - Médio")
    print("\033[35mNível 4 - Difícil")
    print("\033[31mNível 5 - Muito Difícil")
    print('\033[30mNível 6 - IMPOSSÍVEL')
    print("\033[m")
    while True:
        try:
            dif = int(input("Nível >> "))
            if 7 > dif > 0:
                return dif
            else:
                print("\033[33mDigite uma opção dentro do menu!\033[m")
        except (ValueError, TypeError):
            print("\033[1;31mDigite um valor válido!!\033[m")


def desenhos(erros):
    if erros != 0:
        print()
        print("\033[1;37m-" * 30)
        match erros:
            case 6:
                print("\033[1;32m  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 5:
                print("\033[1;93m  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |       |    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 4:
                print("\033[m  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 3:
                print("\033[1;37m  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 2:
                print("\033[1;91m  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 1:
                print("\033[1;30m  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")
                print(" |            ")
                print("_|___         ")
        print()
        print("\033[1;37m-" * 30)
        print()


def aleatorizar_palavra_secreta(nivel=5):
    from random import randint
    arquivo = open("Palavras.txt", "r", encoding="utf8")
    numero_sorteado = 0
    if nivel == 1:
        numero_sorteado = randint(0, 200)
    if nivel == 2:
        numero_sorteado = randint(201, 400)
    if nivel == 3:
        numero_sorteado = randint(401, 600)
    if nivel == 4:
        numero_sorteado = randint(601, 800)
    if nivel == 5:
        numero_sorteado = randint(801, 1000)
    if nivel == 6:
        numero_sorteado = randint(1001, 1095)
    for key, valor in enumerate(arquivo.readlines()):
        if key == numero_sorteado:
            return str(valor[:-1]).upper()


def sistema_principal(palavra_secreta):
    from unidecode import unidecode
    ja_comentados = []
    chutes_ja_comentados = []
    palavra = palavra_secreta
    palavra_sem_acento = unidecode(palavra)
    print("-" * 30)
    print(f"A palavra tem {len(palavra)} Letras!".center(30))
    print("-" * 30)
    descobrir = []
    palpite = 0
    vida = 7
    for c in range(0, len(palavra)):
        descobrir.append("_")
    while True:
        while True:
            resp = str(input("\033[1;96mSua resposta >> ")).strip().upper()
            resp_sem_acento = unidecode(resp)
            palpite += 1
            if len(palavra) > len(resp) > 1:
                print("\033[1;35mChute ou diga uma letra!\033[m")
                continue
            if resp.isnumeric():
                print("\033[1;33mDigite um valor válido por favor!\033[m")
                continue
            if resp in ja_comentados:
                print(f"\033[1;37mVocê já comentou a Letra \033[31m{resp}\033[m")
                continue
            if resp in chutes_ja_comentados:
                print(f"\033[1;37mVocê já chutou a Palavra \033[31m{resp}\033[m")
                continue
            if resp == '':
                print("\033[1;33mDigite algo!!")
                continue
            else:
                if len(resp) == 1:
                    ja_comentados.append(resp)
                if len(resp) == len(palavra):
                    chutes_ja_comentados.append(resp)
                break
        if resp_sem_acento == palavra_sem_acento:
            return palavra, palpite - 1, palavra
        if resp in palavra_sem_acento or resp in palavra:
            for index, valor in enumerate(palavra_sem_acento):
                if valor == resp:
                    descobrir[index] = palavra[index]
            print("\033[1;37m-" * (len(palavra) * 3))
            for v in descobrir:
                if v == "-":
                    print("\033[1;31;40m", end=" ")
                else:
                    print("\033[1;32;40m", end=" ")
                print(v, end=" ")
            print("\033[m")
            print("\033[1;37m-" * (len(palavra) * 3))
        else:
            vida -= 1
            desenhos(vida)
            if vida > 0:
                print(f"\033[1;31mERROU!", end="")
                if vida > 1:
                    print(f" você tem {vida} chances\033[m")
                else:
                    print("\033[30m Você tem apenas uma chance! cuidado!!")
            print()
        if vida == 0 or "_" not in descobrir:
            return descobrir, palpite - 1, palavra


def perdeu_ou_ganhou(resposta_do_usuario, palpites, palavra):
    from time import sleep
    acumular_string = ""
    print()
    for letra in resposta_do_usuario:
        acumular_string += letra
    if acumular_string == palavra:
        print("\033[1;32m=" * 40)
        print("VOCÊ VENCEU!!!!".center(40))
        print("=" * 40)
        print("\033[1;33m       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        print(f"\n\033[1;35mPalpites:\033[1;36m {palpites}")
        return 1
    else:
        print("\033[1;31m=" * 40)
        print("VOCÊ FOI ENFORCADO :(".center(40))
        print("=" * 40)
        print("\033[1;30m    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        sleep(1)
        print(f"\n\033[1;33mA palavra era \033[34m{palavra}")
        return 0


def continuar():
    while True:
        try:
            print()
            continuar = str(input("\033[mJogar Novamente? [S/N]: ")).strip().upper()[0]
            print()
            if continuar in 'NS':
                break
        except IndexError:
            print("\033[1;31mDigite Algo!\033[m")
        else:
            print("\033[1;33mDigite um valor válido!")
    if continuar == "N":
        print("\033[mPrograma Finalizado </>")
        return 0
    if continuar == "S":
        return 1


def jogo_da_forca():
    vitorias = 0
    while True:
        dificuldade_escolhida = inicio()
        palavra_secreta = aleatorizar_palavra_secreta(dificuldade_escolhida)
        sys = sistema_principal(palavra_secreta)
        perda_ou_vitoria = perdeu_ou_ganhou(sys[0], sys[1], sys[2])
        if perda_ou_vitoria == 1:
            vitorias += 1
            print(f"\033[1;35mVitórias: \033[1;33m{vitorias}\033[m")
        novamente = continuar()
        if novamente == 0:
            print("\033[1;33mPrograma Finalizado </>\033[m")
            break
        if novamente == 1:
            continue


jogo_da_forca()
