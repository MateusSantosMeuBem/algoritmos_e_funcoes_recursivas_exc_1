def somaSeq(x, n):
    sum = 0
    for i in range(1, n+1):
        sum += (x**i)/i

    return sum


print(somaSeq(2, 4))