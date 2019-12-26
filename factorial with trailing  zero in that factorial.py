def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def factorialTrailing():
    count = 0
    i = 5
    while number // i != 0:
        count += int(number / i)
        i = i * 5
        return count


if __name__ == '__main__':
    number = int(input("Enter a number"))
    fac = factorial(number)
    fac1 = factorialTrailing(number)
    print(f"The factorial is : {fac}")
    print(f"Your trailing is: {fac1}")
