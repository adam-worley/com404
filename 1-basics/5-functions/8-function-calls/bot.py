def box (word):
    x=len(word)
    print((x+4)*"-")
    print("|",word,"|")
    print((x+4)*"-")

def lcase(word):
    print(word.lower())

def ucase(word):
    print(word.upper())

def mirror(word):
    x = len(word)-1
    for count in range(x, -1, -1):
        print(word[count],end="")

def repeat(word):
    print("how many times do you want to repeat the word? ",end="")
    n = int(input())
    print()
    x=0
    while (n>0):
        x = x+1
        if((x%2)==0):
            print(word.lower(),end="")
        else:
            print(word.upper(),end="")
        n=n-1

def run():
    print("Please enter a word to be deciphered")
    word = input()
    print()
    print("Please select a decipher technique from the list below:")
    print("1) Display in a box")
    print("2) Display lower-case")
    print("3) Display upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    print()
    print("Decipher technique:",end="")
    method = int(input())
    while(method>5):
            print("Invalid selection, please choose again:",end="")
            method = int(input())
            print()
    if(method==1):
        box(word)
    elif(method==2):
        lcase(word)
    elif(method==3):
        ucase(word)
    elif(method==4):
        mirror(word)
    elif(method==5):
        repeat(word)


run()