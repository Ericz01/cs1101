entries = {}

def main():
    add_entries()

def add_entries():
    entry = input("Enter your entry's title: ")
    content = input("Enter the entry's content: ")
    entries[entry] = content
    
    option = input("Enter 'A' to add an entry, 'V' to view your entries or 'C' to cancel: ").lower()
    if option == 'a':
        add_entries()
    elif option == 'v':
        print("-" * 10 + "YOUR ENTRIES" + "-" * 10) 
        for entry, content in entries.items():
            print(f"{entry.upper()}:\n{content}\n________________________________\n")
        # stage
        choice = input("Enter 'A' to add an entry, 'V' to view your entries or 'C' to cancel: ").lower()
        if choice == 'a':
            add_entries()
        elif choice == 'c':
            print("Successfully returned")
    elif option == 'c':
        print("Successfully returned")
if __name__ == "__main__":
    main()