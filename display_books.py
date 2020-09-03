from tabulate import tabulate


print("Displaying......")
file = open("books.txt", "r")
file_contents = file.read()

table_1 = [[file_contents]]
headers_1 = ["Name Of Books"]
print(tabulate(table_1, headers_1 , tablefmt = "grid"))
               
