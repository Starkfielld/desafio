#1
def sentenca_inversa(sentenca):
    palavra = sentenca.split()  
    palavras_inversas = palavra[::-1]  
    sentenca_inversa = ' '.join(palavras_inversas) 
    return sentenca_inversa

input = "hello, World! OpenAi is amazing"
output_desejado = "amazing is OpenAi World! hello,"

output_real = str(sentenca_inversa(input))

if output_real == output_desejado:
    print("O caso de teste passou com sucesso!")
    print("A mensagem insirida foi: ", input)
    print("O resultado foi: ", output_real )
else:
    print("O caso de teste falhou.")
    print("Saída esperada:", output_desejado)
    print("Saída obtida:", output_real)

#2    
def deletar_duplicatas(string):
    letras_unicas = set()
    resultado = ''
    for letra in string:
        if letra not in letras_unicas:
            letras_unicas.add(letra)
            resultado += letra
    return resultado


texto_entrada = "hello world!"
saida_desejada = "helo wrd!"

saida_real = deletar_duplicatas(texto_entrada)


if saida_real == saida_desejada:
    print("O caso de teste passou com sucesso!")
else:
    print("O caso de teste falhou.")
    print("Saída esperada:", saida_desejada)
    print("Saída obtida:", saida_real)



def expandir_centro(s, esquerda, direita):
    while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]:
        esquerda -= 1
        direita += 1
    return s[esquerda + 1: direita]

#3
def maior_palindromo(s):
    maior = ""
    for i in range(len(s)):
        # Para substrings de tamanho ímpar
        substring_impar = expandir_centro(s, i, i)
        if len(substring_impar) > len(maior):
            maior = substring_impar

        # Para substrings de tamanho par
        substring = expandir_centro(s, i, i + 1)
        if len(substring) > len(maior):
            maior = substring

    return maior


string_entrada = "babad"
string_esperada = "bab"

string_saida = maior_palindromo(string_entrada)


if string_saida == string_esperada:
    print("O caso de teste passou com sucesso!")
else:
    print("O caso de teste falhou.")
    print("Saída esperada:", string_esperada)
    print("Saída obtida:", string_saida)

#4
def capitalize_sentences(input_string):
    sentences = input_string.split(". ")
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    output_string = ". ".join(capitalized_sentences)
    return output_string

def test_capitalize_sentences():
    input_string = "hello, how are you? i'm fine, thank you"
    expected_output = "Hello, how are you? i'm fine, thank you"
    assert capitalize_sentences(input_string) == expected_output
    print("Os caso de teste foi executado com sucesso!")


test_capitalize_sentences()

#5
from collections import Counter

def anagrama_palindromo(string):
    contador = Counter(string)
    contador_impar = 0

    for count in contador.values():
        if count % 2 != 0:
            contador_impar += 1

    return contador_impar <= 1

# Caso de teste
entrada = "racecar"
saida = True

saida_booleana = anagrama_palindromo(entrada)

# Verifica se a saída é igual à saída esperada
if saida_booleana == saida:
    print("O caso de teste passou com sucesso!")
else:
    print("O caso de teste falhou.")
    print("Saída esperada:", saida)
    print("Saída obtida:", saida_booleana)
