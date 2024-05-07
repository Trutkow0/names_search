# Timothy Rutkowski 04/25/2024 timothyRutkowski_lab7-1.py

# This program will read the files BoyNames.txt and GirlNames.txt as lists and
# allow the user to search for names in the lists. As the program loops, each
# attempt to search for a name and every successful search will be tracked and
# displayed.

def main():
    boy_names, girl_names = open_and_read_files()
    boy_attempts, boy_count, girl_attempts, girl_count = search(boy_names, girl_names)
    results(boy_attempts, boy_count, girl_attempts, girl_count)

# Function to open and read files as a list.   
def open_and_read_files():
    # Read BoyNames.txt as a list
    boy_file = open('BoyNames.txt', 'r')
    boy_names = boy_file.readlines()

    # Strip \n from each element in boy_names
    for index in range(len(boy_names)):
        boy_names[index] = boy_names[index].rstrip('\n').lower()

        # Read GirlNames.txt as a list
        girl_file = open('GirlNames.txt', 'r')
        girl_names = girl_file.readlines()

        # Strip \n from each element in girl_names
        for index in range (len(girl_names)):
            girl_names[index] = girl_names[index].rstrip('\n').lower()
    
    # Close files
    boy_file.close()
    girl_file.close()
    
    return boy_names, girl_names 

# Funciton to ask the user if the want to search for a boy name or a girl name,
# what name they would like to search, and loop until told to stop.
def search(boy_names, girl_names):
    # Initialize the attempts and count for boy and girl names to 0
    boy_attempts = 0
    girl_attempts = 0
    boy_count = 0
    girl_count = 0
    
    while True:
        boy_or_girl = input("Would you like to search a boy or a girl name? " +
                    "(Enter 'boy' or 'girl', or 'stop' to end): ")
    
        if boy_or_girl == 'stop':
            break

        if boy_or_girl == 'boy':
            boy_search = input('\nEnter the name you would like ' +
                           'to search for: ').lower()
            boy_attempts += 1
            if boy_search in boy_names:
                print(f"\t'{boy_search.capitalize()}' was found in the " +
                  "boy names list.\n")
                boy_count += 1
            else:
                print(f"\t'{boy_search.capitalize()}' was not found in the " +
                  "boy names list.\n")
        elif boy_or_girl == 'girl':
            girl_search = input('\nEnter the name you would like ' +
                            'to search for: ').lower()
            girl_attempts += 1
            if girl_search in girl_names:
                print(f"\t'{girl_search.capitalize()}' was found in the " + 
                  "girl names list.\n")
                girl_count += 1
            else:
                print(f"\t'{girl_search.capitalize()}' was not found in the " +
                  "girl names list.\n")
        else:
            print("Invalid Input: Please enter 'boy' or 'girl', or 'stop' " +
                  "to end.\n")
            
    return boy_attempts, boy_count, girl_attempts, girl_count
            
# Funtion to display how many boy and girl names were tested and how many were 
# found in the lists 
def results(boy_attempts, boy_count, girl_attempts, girl_count):
    print(f'\nBoy Names Tested: {boy_attempts}  \nBoy Names Found: {boy_count}')
    print(f'\nGirl Names Tested: {girl_attempts} \nGirl Names Found: {girl_count}')
    
# Call the main function
if __name__ == '__main__':
    main()