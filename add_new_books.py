
list_1 = []
print("\n\nWelcome to The New Books Adding Section\n\n")
name_of_book = str(input("Please enter the name of the book: "))
file = open("books.txt","a")
file.write("\n"+ name_of_book)
file.close()


