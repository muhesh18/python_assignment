# Write a Python function to find the Max of three numbers.

'''def maximum(a, b, c): 

	if (a >= b) and (a >= c): 
		largest = a 

	elif (b >= a) and (b >= c): 
		largest = b 
	else: 
		largest = c 
		
	return largest 
a = 10
b = 14
c = 12
print(maximum(a, b, c)) 
#2) Write a Python function to sum all the numbers in a list.
a=[1,2,3,4,5]
def add(a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)
add(a)
#) Write a Python function that accepts a string and calculate 
#the number of upper case letters and lower case letters.
b='aBNADFAbgsjshl'
def stringcount(b):
    upper =0
    lower =0
    for i in b:
        if i.isupper():
            upper=upper+1
        else:
            lower =lower+1
    print(upper)
    print(lower)
stringcount(b)
#4) Write a Python function to calculate the factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Input a number to compute the factorial: "))

print(factorial(n))'''
#5)5) Write a Python function to check whether a given number is prime
num = 71
if num > 1: 
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
      print(i)
      print(num,"is a prime number")
      
    
else:
   print(num,"is not a prime number")

#66) Write a Python function to reverse a string.
'''a='Aravind'
def reverse(a):
    b=a[::-1]
    print(b)
reverse(a)
#7)7) Write a Python function to find the sum of all elements in a list.
a=[1,2,3,4,5]
def add(a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)
add(a)
#8)) Write a Python function to count the number of vowels in a string
'a='aradfgedute'
b=['a','e','i','o','u']
def vowels(a):
    count=0
    for i in a:
        if i in b:
            count=count+1
    print(count)
vowels(a)
#9)Write a function that takes in a list of numbers and returns the sum of all the even numbers in the list.

a=[1,2,3,4,5,6,7,8]
def evennumber(a):
    sum=0
    for i in a:
        if i%2==0:
            sum=sum+i
    print(sum)
evennumber(a)
#10)) Write a function that takes in a string and returns a new string with all vowels removed.
a='aradfgedute'
b=['a','e','i','o','u']
def notvowel(a):
    for i in a:
        if i not in b:
            print(i,end="")
notvowel(a)
#11)Write a function that takes in a list of strings and returns a new list with all strings that have more than 5 characters.
a=['apple' ,'cherrys', 'bananas']
def newstrings(a):
    for i in a:
        if len(i)>5:
            print(i,end=" ")
newstrings(a)
'''
