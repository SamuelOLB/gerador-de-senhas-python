import random
import string


def gerar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    
    todos_caracteres = letras + numeros + simbolos
    
    senha = ""
    for i in range(tamanho):
        senha += random.choice(todos_caracteres)
    
    return senha


def pedir_tamanho():
    while True:
        tamanho_input = input("Digite o tamanho da senha (apenas números): ")
        
        if tamanho_input.isdigit():
            tamanho = int(tamanho_input)
            
            if tamanho > 0:
                return tamanho
            else:
                print("Digite um número maior que zero.")
        else:
            print("Entrada inválida. Digite apenas números.")


def perguntar_continuar():
    while True:
        resposta = input("\nDeseja gerar outra senha? (s/n): ").lower()
        
        if resposta in ["s", "sim"]:
            return True
        elif resposta in ["n", "nao", "não"]:
            return False
        else:
            print("Entrada inválida. Digite apenas 's' para sim ou 'n' para não.")


def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")
    
    while True:
        tamanho = pedir_tamanho()
        senha = gerar_senha(tamanho)
        
        print("\n🔐 Senha segura gerada com sucesso!")
        print(f"Sua senha com {tamanho} caracteres é: {senha}")
        
        if not perguntar_continuar():
            print("\n🔒 Encerrando geração de senhas seguras...")
            break


if __name__ == "__main__":
    main()