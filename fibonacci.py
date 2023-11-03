# Gera a sequência de Fibonacci até o número passado como parâmetro
def fibonacci(numero_sequencia):
    # Esses são os dois primeiros números da sequência
    fib_1, fib_2 = 1, 1
    sequencia = [fib_1, fib_2]

    # Flag para dar continuidade à sequência
    maior_igual_tres = numero_sequencia >= 3

    match numero_sequencia:
        case 1:
            return fib_1
        case 2:
            return sequencia
        case maior_igual_tres:
            # Gera a sequência de Fibonacci em si
            for numero_fib in range(numero_sequencia - 2):
                fib_1, fib_2 = fib_2, fib_1 + fib_2

                sequencia.append(fib_2)

            return sequencia


sequencia = fibonacci(10)

print(*sequencia)




# SDG
