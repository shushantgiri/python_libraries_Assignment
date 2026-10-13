# Assignment 3: Colorful Student Report (colorama)
from colorama import Fore, init

init(autoreset=True)

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

print(Fore.CYAN + "Student Name: " + name)
print("Marks:", marks)

if marks >= 40:
    print(Fore.GREEN + "Result: PASS")
else:
    print(Fore.RED + "Result: FAIL")
