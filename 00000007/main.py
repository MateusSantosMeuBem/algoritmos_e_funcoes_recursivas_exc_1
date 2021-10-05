def binomial(n, k):
    if n == 0 and k > 0 : return 0 
    if n >= 0 and k == 0: return 1

print(binomial(0, 1))
print(binomial(0, 0))
print(binomial(1, 0))