
import csv
from tabulate import tabulate

print("Welcome To The Library Searching Books Section.\n\n")
name = input('Enter book to search : \n')

file = open("books.txt", "r")
file_stuff = []  
for line in file:
    line=line.strip()
    file_stuff.append(line)
file.close()
if name in file_stuff:
    print(name)
    print("\n\nThis Book Is Available\n\n")
                 
else:
    print("This book is unavilable\n\n")
        
