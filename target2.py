# Função para contar ocorrências de 'a' ou 'A'
def conta_letra_a(texto):
    return texto.lower().count('a')

# Entrada da string
texto = input("Informe uma string: ")

# Contagem e resultado
contagem = conta_letra_a(texto)
print(f"A letra 'a' ocorre {contagem} vez(es) na string.")
