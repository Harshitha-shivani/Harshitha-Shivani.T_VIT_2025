"""Given an integer N, write a program to count the number of digits in N.

Input Format

Example 1: Input0: N = 12345

Example 2: Input1: N = 8394

Constraints

n <= 10000

Output Format

Output0: 5 Explanation: N has 5 digits

Output1: 4 Explanation: N has 4 digits

Sample Input 0

12345
Sample Output 0

5
Sample Input 1

876349
Sample Output 1

6"""

"logic 1:"

n = input()
def countDigit(n):
    n = str(n)
    count = len(n)
    count = int(count)
    return count
print(countDigit(n))

"logic 2:"

def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
N = int(input().strip())
if N <= 10000:
    result = count_digits(N)
    print(result)
else:
    print("Input constraint violation: N should be less than or equal to 10000.")