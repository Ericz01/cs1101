import calendar

# A program to check the return value and how it is being used.

def main():
    '''Calls all the other functions.'''
    print(tell_date(12, 11))
    print(tell_date(1, 1))
    print(tell_date(5, 30))
    print(tell_date(8, 4))

def tell_date(month, date):
    '''Takes ints as month and day. Returns a string representation of the date.'''
    print(f'......Working on {month}, {date}') # Check the parameteres passed.
    print()
    print('Returning......') # Checking the values returned.
    return f"Today is on {calendar.month_name[month]} {date}.\n____________________________"

main()