checklist = []

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

# Destroy
def destroy(index):
    checklist.pop(index)

def list_all_items():
    items = []
    for element in checklist:
        print(element)
        items.append(element)
    
    return items


def checked(index):

    unchecked = checklist[index]

    checklist[index] = "√ " + unchecked

    return checklist[index]

# USER INPUT FUNCTION
def user_input(prompt):

    entry = input(prompt)

    return entry

# USER CHOICE FUNCTION
def user_choice():

    # initialize variable for while loop
    editing = True 

    while editing:

        choice = user_input("Which function would you like to use? Enter C for create, R for read, U for update, D for destroy, A to view all items currently in the checklist and S to select an item with a checkmark. ")

        if choice == "C" or choice == "c":

            item = user_input("What item do you wish to create? Type out the name of your desired item. ")

            create(item)

            continue

        elif choice == "R" or choice == "r":

            index = user_input("What item do you wish to read? Give a number for the position of the item. ")

            read(int(index))

            continue

        elif choice == "U" or choice == "u":

            update_index = user_input("What item do you wish to update? Give a number for the position of the item. ")

            new_item = user_input("Type out the name of your new item. ")

            update(int(update_index), new_item)

            continue

        elif choice == "D" or choice == "d":

            delete_index = user_input("What item do you wish to delete? Give a number for the position of the item. ")

            destroy(int(delete_index))

            continue

        elif choice == "A" or choice == "a":

            all_items()

            continue

        elif choice == "S" or choice == "s":

            checked_index = user_input("What item do you wish to check off? Give a number for the position of the item. ")

            checked(int(checked_index))

            continue

        else:

            end = user_input("Do you wish to quit? Enter Y for yes or N for no. ")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:

                continue

def test():

    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # print(all_items())
    # print(checked(0))
    # print(user_input("Is this working? "))
    user_choice()

user_choice()