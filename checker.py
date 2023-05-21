import sys
import re

def check_password_strength(password):
    if len(password) < 11:
        return "A senha deve ter no mínimo 11 caracteres."

    if not re.search("[a-z]", password) or not re.search("[A-Z]", password) or \
            not re.search("[0-9]", password) or not re.search("[!@#$%^&*()]", password):
        return "A senha deve conter letras maiúsculas, minúsculas, números e caracteres especiais."

    if re.search(r"(.)\1\1", password):
        return "A senha não deve conter sequências de caracteres repetidos. Em caso de caracteres repetidos, um atacante pode analisar o hash ou criptografia de saída, padrões que levem o tratamento da senha como comuns e torne o processo de quebra mais fácil. Boas práticas de senhas incluem o uso de hash + salt ou delegar a responsabilidade do armazenamento de senhas para empresas grandes, como LinkedIn, Google, Facebook, por exemplo."

    return "A senha é forte. Lembre-se de adotar práticas seguras de armazenamento de senhas e evitar práticas inseguras, como armazenar senhas em texto simples, criptografia fraca ou uso de hashes sem salt. Tenha em mente que existem ferramentas, como o hashcat, hydra e john the ripper, que podem ser usadas para quebrar senhas."

def main():
    if len(sys.argv) < 2:
        print("Por favor, forneça uma senha como argumento.")
        return

    password = sys.argv[1]
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
