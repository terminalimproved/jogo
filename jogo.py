import random

def intro():
    print("Você acorda em um lugar desconhecido.")
    print("O ambiente é escuro e nebuloso. À sua frente, há três caminhos distintos.")
    print("Você sente uma sensação de inquietação e desorientação.")
    print("O que você faz?")

def escolha_caminho():
    print("\n1. Seguir o caminho iluminado por uma luz fraca.")
    print("2. Seguir o caminho coberto de sombras profundas.")
    print("3. Seguir o caminho que leva a uma porta antiga.")
    escolha = input("Escolha (1/2/3): ").strip()

    if escolha == "1":
        return caminho_iluminado()
    elif escolha == "2":
        return caminho_sombrio()
    elif escolha == "3":
        return porta_antiga()
    else:
        print("Escolha inválida. Tente novamente.")
        return escolha_caminho()

def caminho_iluminado():
    print("\nVocê segue o caminho iluminado e encontra uma mesa com uma vela acesa.")
    print("Há também uma inscrição na parede e um livro antigo sobre a mesa.")
    print("O que você faz?")

    print("\n1. Ler a inscrição na parede.")
    print("2. Pegar o livro antigo.")
    print("3. Apagar a vela e voltar para o começo.")
    escolha = input("Escolha (1/2/3): ").strip()

    if escolha == "1":
        return inscricao_na_parede()
    elif escolha == "2":
        return livro_antigo()
    elif escolha == "3":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return caminho_iluminado()

def caminho_sombrio():
    print("\nVocê segue o caminho coberto de sombras e encontra uma figura misteriosa encapuzada.")
    print("A figura parece te observar sem dizer uma palavra.")
    print("O que você faz?")

    print("\n1. Perguntar à figura sobre o que está acontecendo.")
    print("2. Ignorar a figura e seguir pelo caminho.")
    print("3. Voltar para o começo.")
    escolha = input("Escolha (1/2/3): ").strip()

    if escolha == "1":
        return figura_misteriosa()
    elif escolha == "2":
        return caminho_perdido()
    elif escolha == "3":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return caminho_sombrio()

def porta_antiga():
    print("\nVocê se aproxima da porta antiga e encontra uma inscrição gravada nela.")
    print("A porta está entreaberta, revelando uma sala escura atrás dela.")
    print("O que você faz?")

    print("\n1. Ler a inscrição na porta.")
    print("2. Entrar na sala escura.")
    print("3. Voltar para o começo.")
    escolha = input("Escolha (1/2/3): ").strip()

    if escolha == "1":
        return inscricao_na_porta()
    elif escolha == "2":
        return sala_escura()
    elif escolha == "3":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return porta_antiga()

def inscricao_na_parede():
    print("\nA inscrição na parede diz: 'O conhecimento é a chave para o entendimento.'")
    print("Você sente uma aura de mistério ao redor da mensagem.")
    print("O que você faz?")

    print("\n1. Continuar explorando o caminho.")
    print("2. Voltar para o começo.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        print("\nVocê encontra um beco sem saída e percebe que o caminho não leva a lugar algum.")
        print("Você volta para o começo.")
        return escolha_caminho()
    elif escolha == "2":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return inscricao_na_parede()

def livro_antigo():
    print("\nVocê abre o livro antigo e encontra um texto incompreensível, com símbolos estranhos.")
    print("Você sente uma sensação de desconforto ao ler o texto.")
    print("O que você faz?")

    print("\n1. Continuar tentando decifrar o texto.")
    print("2. Fechar o livro e voltar para o começo.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        print("\nVocê tenta decifrar o texto, mas a sensação de desorientação se intensifica.")
        print("Você se perde em seus próprios pensamentos e retorna ao início.")
        return escolha_caminho()
    elif escolha == "2":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return livro_antigo()

def inscricao_na_porta():
    print("\nA inscrição na porta diz: 'A verdade não é o que parece ser.'")
    print("Você se sente mais inquieto com essa nova mensagem.")
    print("O que você faz?")

    print("\n1. Entrar na sala escura.")
    print("2. Voltar para o começo.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        return sala_escura()
    elif escolha == "2":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return inscricao_na_porta()

def sala_escura():
    print("\nVocê entra na sala escura e vê uma figura sentada em um trono de pedra.")
    print("A figura se volta para você e te pergunta sobre o que você procura na vida.")
    print("O que você faz?")

    print("\n1. Dizer que procura respostas sobre a vida.")
    print("2. Dizer que está apenas explorando.")
    print("3. Voltar para o começo.")
    escolha = input("Escolha (1/2/3): ").strip()

    if escolha == "1":
        return resposta_filosofica()
    elif escolha == "2":
        return figura_no_trono()
    elif escolha == "3":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return sala_escura()

def figura_misteriosa():
    print("\nA figura encapuzada sussurra: 'A verdade está escondida nas sombras.'")
    print("Você sente uma presença mais forte ao redor.")
    print("O que você faz?")

    print("\n1. Seguir o conselho e explorar as sombras.")
    print("2. Voltar para o caminho iluminado.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        return explorar_sombras()
    elif escolha == "2":
        return caminho_iluminado()
    else:
        print("Escolha inválida. Tente novamente.")
        return figura_misteriosa()

def explorar_sombras():
    print("\nVocê segue pelas sombras e se perde em um labirinto de escuridão.")
    print("Você vagará para sempre sem encontrar uma saída.")
    print("O jogo termina aqui.")
    return fim_jogo()

def caminho_perdido():
    print("\nVocê segue o caminho perdido e encontra um abismo profundo.")
    print("Você contempla o vazio e se pergunta sobre o significado da vida.")
    print("O jogo termina aqui.")
    return fim_jogo()

def figura_no_trono():
    print("\nA figura no trono observa você com uma expressão de indiferença.")
    print("Você sente um vazio profundo e começa a refletir sobre sua própria existência.")
    print("O jogo termina aqui.")
    return fim_jogo()

def resposta_filosofica():
    print("\nA figura no trono te diz: 'A vida é um enigma a ser desvendado por cada um de nós.'")
    print("Você se sente inspirado a buscar um propósito na vida.")
    print("Você encontra uma saída para o labirinto e segue em frente, com uma nova perspectiva.")
    print("O jogo termina aqui.")
    return fim_jogo()

def livro_antigo():
    print("\nVocê abre o livro antigo e encontra um texto incompreensível, com símbolos estranhos.")
    print("Você sente uma sensação de desconforto ao ler o texto.")
    print("O que você faz?")

    print("\n1. Continuar tentando decifrar o texto.")
    print("2. Fechar o livro e voltar para o começo.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        print("\nVocê tenta decifrar o texto, mas a sensação de desorientação se intensifica.")
        print("Você se perde em seus próprios pensamentos e retorna ao início.")
        return escolha_caminho()
    elif escolha == "2":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return livro_antigo()

def sala_misteriosa():
    print("\nVocê entra em uma sala cheia de velas apagadas e um grande espelho antigo.")
    print("A sala tem um ar de abandono e você sente um frio na espinha.")
    print("O que você faz?")

    print("\n1. Acender as velas.")
    print("2. Olhar no espelho.")
    print("3. Voltar para o começo.")
    escolha = input("Escolha (1/2/3): ").strip()

    if escolha == "1":
        return acender_velas()
    elif escolha == "2":
        return olhar_no_espelho()
    elif escolha == "3":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return sala_misteriosa()

def acender_velas():
    print("\nVocê acende as velas e a sala se ilumina, revelando um caminho oculto atrás do espelho.")
    print("Você decide seguir o caminho.")
    print("O que você faz?")

    print("\n1. Seguir o caminho oculto.")
    print("2. Voltar para a sala inicial.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        return caminho_oculto()
    elif escolha == "2":
        return escolha_caminho()
    else:
        print("Escolha inválida. Tente novamente.")
        return acender_velas()

def olhar_no_espelho():
    print("\nVocê olha no espelho e vê uma versão distorcida de si mesmo, cheia de angústia.")
    print("A visão te faz refletir sobre suas próprias escolhas e a natureza da existência.")
    print("O jogo termina aqui.")
    return fim_jogo()

def caminho_oculto():
    print("\nVocê segue o caminho oculto e encontra um livro antigo sobre um altar.")
    print("O livro está aberto em uma página com uma única frase: 'A verdade está dentro de você.'")
    print("O que você faz?")

    print("\n1. Ler a frase no livro.")
    print("2. Deixar o livro e seguir por um túnel adiante.")
    escolha = input("Escolha (1/2): ").strip()

    if escolha == "1":
        print("\nVocê lê a frase e reflete sobre a verdade dentro de si mesmo.")
        print("Você encontra um caminho de volta ao início com uma nova visão.")
        return escolha_caminho()
    elif escolha == "2":
        print("\nVocê segue pelo túnel e se perde na escuridão.")
        print("O jogo termina aqui.")
        return fim_jogo()
    else:
        print("Escolha inválida. Tente novamente.")
        return caminho_oculto()

def reflexão_sombria():
    print("\nVocê se perde em seus próprios pensamentos e reflete sobre a natureza da existência.")
    print("Você sente uma sensação de desespero e um vazio profundo.")
    print("O jogo termina aqui.")
    return fim_jogo()

def fim_jogo():
    print("\nO jogo chegou ao fim.")
    print("Às vezes, nossas escolhas não têm respostas fáceis e o caminho pode ser sombrio.")
    print("Obrigado por jogar.")

def main():
    intro()
    escolha_caminho()

if __name__ == "__main__":
    main()
