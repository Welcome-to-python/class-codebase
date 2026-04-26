# 1. write a program to print "hello world" in python 
print("hello world")

# 2.Take input from the user and print its square.
num=int(input("enter a number:"))
square=num*num
print("square is ",square)

# 3.Write a program to calculate the sum of two numbers.
a=10
b=30
print("sum of two nuber is",a+b)

# 4. Check whether a number is even or odd.
num=10
if num%2==0:
    print("even")
else:
    print("odd")
    
# 5.Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)
    
# 6. Print all elements of a list.
list=["pen","book","pencil","eariser","college","red"]
print(list)

# 7.Reverse a string without using built-in functions.
name="sharanu"
print(name[::-1])

# 8. Find the maximum of three numbers.
num=[18,83,33]
print(max(num))

# 9. Find the factorial of a number.
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(4))

# 10. Count the number of vowels in a string
name="education"
vowels="aeiou"
count=0
for ch in name:
    if ch in vowels:
        count+=1
print(count)

# 11.Print the Fibonacci series up to n terms.
n=int(input("enter a number"))
a=0
b=1
if n<=0:
    print("enter positive number")
elif n==1:
    print("fibonci series",a)
    
else:
    print("fibonci series")
    for i in range(n):
        print(a,end="")
        a,b=b,b+1
        

#. 12.Check whether a string is a palindrome or not.
st=input("enter a string:")
if st==st[::-1]:
    print("palindrome")
else:
    print("not palindrome")    
    
#. 13. Find duplicate elements in a list.

# 14. Write a program to check if a number is prime.
n=int(input("enter a number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
            print("prime")
else:
    print("not prime")

# 15. Create a dictionary and access its values.
dict= {
    "name":"sharanu",
    "age":20
    }
print(dict)


# 16.16 Sort a list in ascending order without using sort().
list=[50,30,10,20,40]
n=len(list)
for i in range(n):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
         list[j],list[j+1]=list[j+1],list[j]
            
    print(list)
            


# 17. Find common elements between two lists.
list1=[10,20,30,40]
list2=[30,20,15,13]
common=list(set(list1)& set(list2))
print(common)
    
# 18.Read a file and count the number of words in it.

# 19. Create a simple class and object (basic OOP example).

# 20.Write an example of exception handling using try-except.