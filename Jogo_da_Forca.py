# Feito por Leoxy (https://github.com/LeoxyOF)

def inicio():
    print("-" * 40)
    print("JODO DA FORCA".center(40))
    print("-" * 40)
    print()
    print("Nível 1 - Muito Fácil ")
    print("Nível 2 - Fácil")
    print("Nível 3 - Médio")
    print("Nível 4 - Difícil")
    print("Nível 5 - Muito Difícil")
    print('Nível 6 - IMPOSSÍVEL')
    print()
    while True:
        try:
            dif = int(input("Nível >> "))
            if 7 > dif > 0:
                return dif
            else:
                print("Digite uma opção dentro do menu!")
        except (ValueError, TypeError):
            print("Digite um valor válido!!")


def desenhos(erros):
    if erros != 0:
        print()
        print("-" * 30)
        match erros:
            case 6:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 5:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |       |     ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 4:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 3:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 2:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            case 1:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")
                print(" |            ")
                print("_|___         ")
        print()
        print("-" * 30)
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
            resp = str(input("Sua resposta >> ")).strip().upper()
            resp_sem_acento = unidecode(resp)
            palpite += 1
            if len(palavra) > len(resp) > 1:
                print("Chute ou diga uma letra!")
                continue
            if resp.isnumeric():
                print("Digite uma letra por favor!")
                continue
            if resp in ja_comentados:
                print(f"Você já comentou a Letra {resp}")
                continue
            if resp in chutes_ja_comentados:
                print(f"Você já chutou a Palavra {resp}")
                continue
            if resp == '':
                print("Digite algo!!")
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
            print("-" * (len(palavra) * 3))
            for v in descobrir:
                if v == "-":
                    print("", end=" ")
                else:
                    print("", end=" ")
                print(v, end=" ")
            print()
            print("-" * (len(palavra) * 3))
        else:
            vida -= 1
            desenhos(vida)
            if vida > 0:
                print(f"ERROU!", end="")
                if vida > 1:
                    print(f" você tem {vida} chances")
                else:
                    print(" Você tem apenas uma chance! cuidado!!")
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
        print("=" * 40)
        print("VOCÊ VENCEU!!!!".center(40))
        print("=" * 40)
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        print(f"\nPalpites: {palpites}")
        return 1
    else:
        print("=" * 40)
        print("VOCÊ FOI ENFORCADO :(".center(40))
        print("=" * 40)
        print("    _______________         ")
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
        print(f"\nA palavra era {palavra}")
        return 0


def continuar():
    while True:
        try:
            print()
            continuar = str(input("Jogar Novamente? [S/N]: ")).strip().upper()[0]
            print()
            if continuar in 'NS':
                break
        except IndexError:
            print("Digite Algo!")
        else:
            print("Digite um valor válido!")
    if continuar == "N":
        print("Programa Finalizado </>")
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
            print(f"Vitórias: {vitorias}")
        novamente = continuar()
        if novamente == 0:
            break
        if novamente == 1:
            continue


jogo_da_forca()
