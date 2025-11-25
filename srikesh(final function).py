def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def digit_sum(n):
    while n > 9:
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        n = sum
    return n

def is_armstrong(n):
    temp = n
    total = 0
    digits = len(str(n))
    
    while temp > 0:
        d = temp % 10
        total += d ** digits
        temp //= 10
    
    return total == n

def main():
    while True:
        print("\n===== MINI CALCULATOR =====")
        print("1. Factorial of a number")
        print("2. Single digit sum (Repeated digit sum)")
        print("3. Check Armstrong number")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            num = int(input("Enter number: "))
            print("Factorial:", factorial(num))

        elif choice == 2:
            num = int(input("Enter number: "))
            print("Single Digit Sum:", digit_sum(num))

        elif choice == 3:
            num = int(input("Enter number: "))
            if is_armstrong(num):
                print(num, "is an Armstrong Number")
            else:
                print(num, "is NOT an Armstrong Number")

        elif choice == 4:
            print("Exiting program... Bye!")
            break

        else:
            print("Invalid choice! Please enter 1–4.")

main()
