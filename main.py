import os
import time

# Função para exibir a palavra com letras adivinhadas
def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

# Função para exibir a forca
def mostrar_forca(tentativas):
    etapas = [
        """
           -----
           |   
           O   
          /|\\  
          / \\  
               
        """,
        """
           -----
           |   
           O   
          /|\\  
          /    
                
   
        """,
        """
           -----
           |   
           O   
          /|\\  
               
               
        """,
        """
           -----
           |   
           O   
          /|   
                
                
        """,
        """
           -----
           |   
           O   
           |   
                
                
  
        """,
        """
           -----
           |   
           O   
               
               
               

        """,
        """
           -----
           |   
                    
                    
                
                    
        """
    ]
    return etapas[tentativas]

# Função principal para jogar o jogo da forca
def jogar():

    # Palavra e Dica usado no jogo
    palavra = "algoritmo"
    dica = "Sequência de instruções para resolver um problema computacional."
    letras_adivinhadas = set() 
    palavra_adivinhada = False
    tentativas = 6

    print(f"Dica: {dica}")

    while tentativas > 0 and not palavra_adivinhada:
        os.system('cls')
        print(mostrar_forca(tentativas))
        print(mostrar_palavra(palavra, letras_adivinhadas))  # Mostra a palavra após limpar a tela
        adivinhar = input("Adivinhe uma letra: ").lower()

        if adivinhar in letras_adivinhadas:
            print("Letra repetida.")
        elif adivinhar in palavra:
            letras_adivinhadas.add(adivinhar)
            print("Acertou!")
        else:
            letras_adivinhadas.add(adivinhar)
            tentativas -= 1
            print(f"Errou! Você tem {tentativas} tentativas restantes.")

        exibicao_atual = mostrar_palavra(palavra, letras_adivinhadas)
        print(exibicao_atual)

        if '_' not in exibicao_atual:
            palavra_adivinhada = True

    if palavra_adivinhada:
        print("Parabens! Ganhou.")
        print(f"A palavra era: {palavra}")

        print("Encerrando jogo")
        time.sleep(5)
    else:
        os.system('cls')
        print(mostrar_forca(tentativas))
        print("Fim de jogo! Perdeu.")
        print(f"A palavra era: {palavra}")

        print("Encerrando jogo")
        time.sleep(5)

# Executar o jogo
if __name__ == "__main__":
    jogar()
