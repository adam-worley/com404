print("please enter the first whole number")
int_1 = int(input())
print("please enter the second whole number")
int_2 = int(input())
print("please enter the third whole number")
int_3 = int(input())
print()
even = 0
odd = 0
if(int_1%2 == 0):
    even=even + 1
else:
    odd=odd + 1
if(int_2%2 == 0):
    even=even + 1
else:
    odd=odd + 1
if(int_3%2 == 0):
    even=even + 1
else:
    odd=odd + 1
print()
print("there where",even,"even and",odd,"odd numbers")

    

