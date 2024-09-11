# Função para gerar a sequência de Fibonacci até o número informado
def pertence_fibonacci(num):
    fib1, fib2 = 0, 1
    if num == 0 or num == 1:
        return True
    
    while fib2 <= num:
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 == num:
            return True
    return False

# Número que deseja verificar
num = int(input("Informe um número: "))

# Verificação
if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
