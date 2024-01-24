# Provide original dictionary.
original_dict = { 
    'Stud1': ['CS1101', 'CS2402', 'CS2001'], 
    'Stud2': ['CS2402','CS2001','CS1102']
}

def inverse(d):
    ''' 
    Takes a dict of students(keys) and courses(values).
    Returns an inverse of the dictionary.
    '''
    # Initialize an empty dict
    inverted_dict = {}

    # Iterate over the dict items and make a list of keys(courses)
    for student, courses in d.items():
        for course in courses:
            # If course not already in list. 
            if course not in inverted_dict: 
                inverted_dict[course] = [student]
            
            # If the course already in list.    
            else:
                inverted_dict[course].append(student)
    return inverted_dict
# Print original dictionary.
print(original_dict, "\n")

# Call the function and display the inversed dictionary.
print(inverse(original_dict))