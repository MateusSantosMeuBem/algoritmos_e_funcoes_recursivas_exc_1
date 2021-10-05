def fibonacci(n):
    if n > 0:
        if n == 1:
            print(0)
        else:
            last = 0
            crt = 1
            print(last, crt, end=' ')
            for i in range(n-2):
                aux = last
                last = crt
                crt = last + aux
                print(crt, end=' ')

fibonacci(1000)
