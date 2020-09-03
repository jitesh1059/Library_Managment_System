from tabulate import tabulate
import datetime

file = open("books.txt", "r")

file_contents = []  
for line in file:
    line=line.strip()
    file_contents.append(line)
file.close()   
print("Books Available: ",file_contents)
name = str(input("Please input the books name that you would like to borrow: "))
if name in file_contents:
    table_3= [["Borrow Book","1"],["Cancel Borrowing","2"]]
    headers_3 = ["Details", "No."]
    print(tabulate(table_3, headers_3, tablefmt = "grid"))
    num = int(input("Please input 1 for confirmation of booking and 2 for canceling the booking: "))
    if(num==1):
        try:
            student_id = str(input("Please input your student ID: "))
            print("\n\nYou have succesfully borrowed this book :" + name)
            start = str(input("Please input the date of borrowing this book(DD-MM-YYYY): "))
            start_object = datetime.datetime.strptime(start, "%d-%m-%Y")
            end_object =start_object + datetime.timedelta(days = 7)
            end_object = str(end_object)
            start_object = str(start_object)
            print("You must hand-in this book by : " + end_object)
            file = open(student_id , "a")
            file.write(name +"------"+start_object+"------"+ end_object +"\n")
            file.close()

            print("Thank you for using the Library System\n\n")  
        except Exception as e:
            print("There is an error ",e)

    else:
        print("Thank you and see you again.")
