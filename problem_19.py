# Problem 19: Calculate power of a number   
# Find and fix the error

# Problem 19: Calculate power of a number (using input)

def power(base, exponent):
    result = 1

    if exponent < 0:
        for i in range(-exponent):
            result *= base
        return 1 / result
    else:
        for i in range(exponent):
            result *= base
        return result

base = int(input("Enter base value: "))
exponent = int(input("Enter exponent value: "))

ans = power(base, exponent)
print(f"{base}^{exponent} = {ans}")