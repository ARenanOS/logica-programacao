# Dicionário: palíndromo diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.

""" 
Exemplos de palíndromos para testar o algoritmo
Ovo, Asa, Osso, Ana, Radar, Renner, Roma é amor, 1001, 11.
Palíndromos em datas 02/02/2020, 9/10/2019. 
Palíndromos em frases 
"Orava o avaro"
"Socorram-me subi no ônibus em Marrocos"
"Seco de raiva, coloco no colo caviar e doces"
"""

import re

def eh_palindromo(texto):
    # Remove caracteres especiais e espaços, deixando apenas letras e números
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto.lower())
    
    if texto_limpo == texto_limpo[::-1]:
        return f"'{texto}' é um palíndromo."
    else:
        return f"'{texto}' não é um palíndromo."

while True:
    entrada = input("\nDigite uma palavra, frase ou data (ou 'sair' para encerrar): ")
    
    if entrada.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break  # Sai do loop
    
    print(eh_palindromo(entrada))
