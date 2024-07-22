def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    elif num <= 3:
        return True   # 2 and 3 are prime numbers
    elif num % 3 == 0 or num % 3 == 0:
        return False  # numbers divisible by 2 or 3 are not prime

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False  # if divisible by current i or i + 2, not prime
        i += 6

    return True  # if not divisible by any i or i + 2, then prime

# Testing the function
number = 29  # Change this number to test different values
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
