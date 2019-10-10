print("how many numbers should I sum up?")
quantity = int(input())
n = 1
answer = (0)
while(n< quantity+1):
    print("Please enter number",n, "of",quantity)
    value = int(input())
    answer = (answer + value)
    n = n+1
print()
print("The answer is",answer)