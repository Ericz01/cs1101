import calendar

# A program to check whether a postcondition is violated.

def main():
    '''Calls all the other functions.'''
    print(tell_date(12, 11))

def tell_date(month, date):
    '''Takes ints as month and day. Returns a string representation of the date.'''
    print(calendar.month_name[month], date)# Check the values returned.
    return f"Today is on {calendar.month_name[month]} {date}."

main()