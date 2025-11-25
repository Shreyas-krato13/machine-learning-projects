def factorial(n):
    if n < 0:
        return "Factorial not possible for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def digit_sum(n):
    while n > 9:
        temp = 0
        while n > 0:
            temp += n % 10
            n //= 10
        n = temp
    return n
