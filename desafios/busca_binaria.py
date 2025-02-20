def busca_binaria(lista, alvo):
    # Define os limites inicial (esquerda) e final (direita) da busca
    esquerda, direita = 0, len(lista) - 1  

    # Continua o loop enquanto houver elementos para pesquisar
    while esquerda <= direita:
        # Calcula o índice do meio da lista
        meio = (esquerda + direita) // 2  

        # Se o elemento do meio for o alvo, retorna a posição
        if lista[meio] == alvo:
            return meio +1 # soma 1 para a posição começar em 1

        # Se o elemento do meio for menor que o alvo, descarta a parte esquerda
        elif lista[meio] < alvo:
            esquerda = meio + 1  

        # Se o elemento do meio for maior que o alvo, descarta a parte direita
        else:
            direita = meio - 1  

    # Retorna -1 se o elemento não for encontrado na lista
    return -1  

# Interação com o usuário
print("\n🔍 Busca Binária 🔎")

# Solicita ao usuário uma lista de números, convertendo para inteiros e ordenando
numeros = list(map(int, input("\nDigite uma lista de números inteiros separados por espaço: ").split()))
numeros.sort()  # A busca binária exige uma lista ordenada

print(f"\n📌 Lista ordenada: {numeros}")

# Loop para buscar múltiplos valores
while True:
    try:
        alvo = input("\nDigite um número para buscar (ou 'sair' para encerrar): ")
        if alvo.lower() == "sair":
            print("Encerrando o programa. Até mais! 👋")
            break

        alvo = int(alvo)  # Converte a entrada para número inteiro
        posicao = busca_binaria(numeros, alvo)

        if posicao != -1:
            print(f"✅ O número {alvo} foi encontrado na {posicao}° posição da lista.")
        else:
            print(f"❌ O número {alvo} não está na lista.")
    except ValueError:
        print("⚠️ Entrada inválida! Digite um número inteiro ou 'sair' para encerrar.")
