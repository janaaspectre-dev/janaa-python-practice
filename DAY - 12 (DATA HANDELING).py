#File Handling



import os


#"x" - Create - Creates the specified file, returns an error if the file exists
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.txt","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.pdf","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.exe","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.png","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.jpeg","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.json","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.xml","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.csv","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.tsv","x")
#A = open("C:\\Users\\Public\\Desktop\\pythprac1.excel","x")
print("succcess")


#"w" - Write - Opens a file for writing, creates the file if it does not exist
with open("C:\\Users\\Public\\Desktop\\pythprac1.txt", "w") as A:
    A.write("task force 141")
    A.close
    print("done")


#"a" - Append - Opens a file for appending, creates the file if it does not exist
with open("C:\\Users\\Public\\Desktop\\pythprac1.txt", "a") as A:
    A.write(" X sas")
    A.close()
print("suii")


#"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
with open("C:\\Users\\Public\\Desktop\\pythprac1.txt", "r") as A:
    print(A.read())
    print(A.read(4))


import os
#os.remove("C:\\Users\\Public\\Desktop\\pythprac1.png")
print("deleted")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.pdf")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.exe")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.jpeg")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.json")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.xml")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.csv")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.tsv")
os.remove("C:\\Users\\Public\\Desktop\\pythprac1.excel")



#2. Create & Write a PDF



    


