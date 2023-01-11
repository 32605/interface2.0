#Program interface should have all these:
#1. tell the user what the program is and what is can do
#2. tell the user make choices or select option
#3. Let the user enter information -you should include a helpful message
#4. Display result or answer
#5. Let the user close the program

teamlist = []
choice = ' '
while choice != 'x':
    print("TEAM MANAGER")
    print("===============")
    print("This program will help you manage your team")
    print("/n")
    print("A: Append a value")
    print("B: Print the team list")
    print("C: Print an Element")
    print("D: Delete an Element")
    print("E: Edit an Element")  
    print("F: Sort the list")  
    print("X: Exit the program")
    choice = input("Enter your choice: ")
    if choice == "A":
        name = input("Enter a name: ")
    teamlist.append(name)
    if choice == "B":
        print(teamlist)
    if choice == "C":
        i = input("Which list item do you want to")
        i =int(i)
        print(teamlist[i-1])
    if choice == "D":
        delete = int(input("which item do you want to delete?:"))
        del teamlist[delete-1]
    if choice == "E":
        edit = int(input("Which list item do you want to edit?"))
        teamlist[edit-1]
        print(teamlist)
    if choice == "F":
         teamlist.sort()
