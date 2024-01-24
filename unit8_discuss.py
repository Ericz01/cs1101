def raise_error(filename):
    '''Creates a new diary entry. Displays the contents if the diary exists.'''
    # Try creating file if non existent.
    try:
        with open(filename, "x") as write_file: # Open in exclusive creation mode.
            write_content = write_file.write("Today is on Jan 6.\nIt's a learning day.")
            print("Entry added successfully.")

    # Show diary's contents if it exixts.
    except FileExistsError:
        print(f"This entry already exists with contents below:\n{'-'* 45}")
        with open(filename) as read_file: # Open in read mode.
            content = read_file.read()
        print(content)

# Call the function if script's running as the main program.
if __name__ == "__main__":
    raise_error("today.txt")