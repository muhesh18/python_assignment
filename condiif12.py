#Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:
'''n=int(input())
if n>90:
    print("Grade A")
elif (n>=80 and n<=90):
    print("Grade B")
elif (n>=60 and n<=79):
    print("Grade C")
else:
    print("Grade D")
#Q2 . Write a Python program that checks whether a given number is divisible by both 3 and 5. If it is, print "Divisible by both 3 and 5." Otherwise, print "Not divisible by both 3 and 5."
number =int(input())
if number%3 ==0 and number % 5==0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
#Q3 . Write a Python program to check if a character entered by the user is a vowel or a consonant.
alphabet = input()
vowels =['a','e','i','o','u']
if alphabet in vowels:
    print("Vowels")
else:
    print("Consonant")
#Q4 . Create a Python program that checks if a given number is even or odd. Print "Even" if it's even, and "Odd" otherwise.
number = int(input())
if number%2==0:
    print("even")
else:
    print("Odd")'''
#Q5 . Write a Python program to determine whether a year is a leap year. A leap year is either divisible by 4 but not by 100, or divisible by 400.
leap_year = int(input())
if leap_year%4==0 and leap_year%100!=0 or  leap_year%400==0 :
    print("It is a leap year")
else:
    print("It is not a leap year")
