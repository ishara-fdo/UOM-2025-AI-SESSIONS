# Project Euler Problems 1 to 10 Solutions

# Problem 1: Multiples of 3 or 5
def euler_1(limit=1000):
	return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

# Problem 2: Even Fibonacci numbers
def euler_2(limit=4000000):
	a, b = 1, 2
	total = 0
	while b <= limit:
		if b % 2 == 0:
			total += b
		a, b = b, a + b
	return total

# Problem 3: Largest prime factor
def euler_3(n=600851475143):
	i = 2
	while i * i <= n:
		if n % i == 0:
			n //= i
		else:
			i += 1
	return n

# Problem 4: Largest palindrome product
def euler_4():
	return max(a*b for a in range(100, 1000) for b in range(100, 1000) if str(a*b) == str(a*b)[::-1])

# Problem 5: Smallest multiple
import math
def euler_5(limit=20):
	def lcm(a, b):
		return abs(a*b) // math.gcd(a, b)
	res = 1
	for i in range(2, limit+1):
		res = lcm(res, i)
	return res

# Problem 6: Sum square difference
def euler_6(limit=100):
	sum_sq = sum(i*i for i in range(1, limit+1))
	sq_sum = sum(range(1, limit+1)) ** 2
	return sq_sum - sum_sq

# Problem 7: 10001st prime
def euler_7(n=10001):
	primes = []
	candidate = 2
	while len(primes) < n:
		for p in primes:
			if candidate % p == 0:
				break
		else:
			primes.append(candidate)
		candidate += 1
	return primes[-1]

# Problem 8: Largest product in a series
def euler_8(series, k=13):
	digits = [int(d) for d in series if d.isdigit()]
	max_prod = 0
	for i in range(len(digits) - k + 1):
		prod = 1
		for j in range(k):
			prod *= digits[i + j]
		if prod > max_prod:
			max_prod = prod
	return max_prod

# Problem 9: Special Pythagorean triplet
def euler_9(total=1000):
	for a in range(1, total//3):
		for b in range(a+1, total//2):
			c = total - a - b
			if a*a + b*b == c*c:
				return a*b*c

# Problem 10: Summation of primes
def euler_10(limit=2000000):
	sieve = [True] * limit
	sieve[0:2] = [False, False]
	for i in range(2, int(limit**0.5)+1):
		if sieve[i]:
			sieve[i*i:limit:i] = [False] * len(range(i*i, limit, i))
	return sum(i for i, prime in enumerate(sieve) if prime)
