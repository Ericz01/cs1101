import calendar

# A program to check whether a precondition is violated.

def main():
    '''Calls all the other functions.'''
    print(tell_date(12, 11))

def tell_date(month, date):
    '''Takes ints as month and day. Returns a string representation of the date.'''
    print(month, date)# Check the arguments passed.
    return f"Today is on {calendar.month_name[month]} {date}."

main()