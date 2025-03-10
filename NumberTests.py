#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def getFactors(num):
  """Returns a list of all factors of a given integer"""
  factors = []
  for f in range(1, num//2 +1):
    if num % f == 0:
      factors.append(f)

  return factors

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p == 2:
    return 2
  if isEven(p):
    return False

  for div in range(3, p // 2, 2):
    if p % div == 0:
      return False
    
  return True

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

def find_nth_prime(n):
    prime_count = 0
    number = 1
    while prime_count < n:
        number += 1
        if isPrime(number):
            prime_count += 1
    return number


def sum_primes_below(limit):
    prime_sum = [True] * limit
    prime_sum[0] = prime_sum[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if prime_sum[start]:
            prime_sum[start*start:limit:start] = [False] * len(range(start*start, limit, start))
    return sum(i for i, is_prime in enumerate(prime_sum) if is_prime)
#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
