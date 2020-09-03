from tabulate import tabulate
table_5 = [["1.","Student", "1"],
           ["2.","Admin/Librarian", "2"]]
headers_5 = ["No.", "Details", "Choice"]
print(tabulate(table_5, headers_5, tablefmt = "grid"))
main_choice = int(input("Please enter your choice : "))

if main_choice == 1:
    from student_login import *
if main_choice == 2:
    from admin_login import *
                  



