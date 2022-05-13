import re,os,linecache


def search(filename,valuename):
    try:
        f = open(f"{filename}.txt", "r")
        print("\nfile exists!")
        pattern = re.compile(valuename)
        for line in f:
            for match in re.finditer(pattern,line):
                print(line)
    except FileNotFoundError:
        print("\nfile does not exist!")
    finally:
        f.close()

def create(filename):
    f = open(f"{filename}.txt", "w")
    usn = input("Enter student usn:>>")
    f.write(f"USN:{usn}\n")
    name = input("Enter student name:>>")
    f.write(f"NAME:{name}\n")
    subcode1 = subcode2 = subcode3 = subcode4 = ""
    marks = ""
    while subcode1 !="none":
        subcode1 = input("Enter subject code for ia1:>>")
        marks = input("Enter the marks for the subject for ia1:>>")
        f.write(f"ia1-{subcode1}-{marks}\n")
    while subcode2 !="none":
        subcode2 = input("Enter subject code for ia2:>>")
        marks = input("Enter the marks for the subject ia2:>>")
        f.write(f"ia2-{subcode2}-{marks}\n")
    while subcode3 !="none":
        subcode3 = input("Enter subject code for ia3:>>")
        marks = input("Enter the marks for the subject for ia3:>>")
        f.write(f"ia1-{subcode3}-{marks}\n")
    while subcode4 !="none":
        subcode4 = input("Enter subject code for finals :>>")
        marks = input("Enter the marks for the subject for finals:>>")
        f.write(f"final-{subcode4}-{marks}\n")
    f.close()
def update(filename,valuename):
    f = open(f"{filename}.txt","r")
    
    for number, line in enumerate(f):
        if valuename in line:
            line_number = number
            break
    list_of_lines = f.readlines()
    length = len(list_of_lines)
    f.seek(0)
    list_of_lines = f.readlines()
    print(list_of_lines)
    update = input("what is the update you want to do:>>")
    list_of_lines[-(length+1)] = f"{valuename}:{update}\n"
    print(list_of_lines)
    f = open(f"{filename}.txt", "w")
    f.writelines(list_of_lines)
    f.close()

def remove(filename):
    if os.path.exists(f"{filename}.txt"):
        os.remove(f"{filename}.txt")

print('''1.Searching inside a file
2.Creating a file
3.Update a file
4.remove file
5.Exit''')
func = input("Enter your option(1 or 2 or 3 or 4 or 5):>>>")
while func != "5":
    
    if func == "1":
        filename = input("Enter the filename of the student:>>")
        valuename = input("Enter the value you want to search:>>")
        search(filename,valuename)
    elif func == "2":
        filename = input("Enter the filename of the student:>>")
        create(filename)
    elif func == "3":
        filename = input("Enter the filename of the student:>>")
        valuename = input("Enter the value you want to search:>>")
        update(filename,valuename)
    elif func == "4":
        filename = input("Enter the filename of the student:>>")
        remove(filename) 
    elif func == "5":
        break
    print('''1.Searching inside a file
2.Creating a file
3.Update a file
4.remove file
5.Exit''')
    func = input("Enter your option(1 or 2 or 3 or 4 or 5):>>>")
