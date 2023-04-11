def fibonacci(n):

    fib = [0, 1]

    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    if n in fib:
        print(f'O número {n} pertence à sequência')
    else:
        print(f'O número {n} não pertence à sequência')


num = int(input('Digite um número: '))


fibonacci(num)
