# A personal journal program.
import sys
# Create an empty dictionary
entries = {}

def main():
    '''Calls all the other functions.'''
    print(add_entries())
def add_entries():
    '''Adds an entry to the entries dictionary.'''
    # Enter user's entry to the dictionary.
    entry = input("Enter your entry's title: ")
    content = input("Enter the entry's content: ")
    entries[entry] = content

    # Give 'View', 'add' and 'exit' options.
    option = input("Enter 'A' to add an entry, 'V' to view your entries or 'C' to cancel: ").lower()
    if option == 'a': # Recursively call the function to add a new entry. 
        add_entries()
    elif option == 'v': # Call the viewing function.
        view_entries(entries)
    elif option == 'c': # Exit the program.
        return "Thank you for using ScriptWaves Journals📜"
    else: # Invalid input.
        print("Invalid option")
        view_entries(entries)
def view_entries(entries):
    '''Prints all entries added.'''
    print("-" * 10 + "YOUR ENTRIES" + "-" * 10) 

    # Iterate through all the entries.
    for entry, content in entries.items():
        print(f"{entry.upper()}:\n{content}\n________________________________\n")
    # Choose option
    option = input("Enter 'A' to add an entry, 'V' to view your entries or 'C' to cancel: ").lower()
    if option == 'a':
        add_entries()
    elif option == 'v':
        view_entries(entries)
    elif option == 'c':
        sys.exit("Thank you for using ScriptWaves Journals📜")
    else:
        print("Invalid option.")
        view_entries(entries)

# Call main.
if __name__ == "__main__":
    main()