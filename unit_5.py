def get_characters(name):
    '''Accepts name and displays: n characters from left, vowel count and reversed name.'''
    vowel_count = 0
    
    # Get user input of n.
    n = int(input("Number of characters from left: "))

    # display name and n characters from left

    print(f"Your name is: {name}.\nFirst {n} chracters: {name[: n]}")

    # Update vowel count and print the total count.
    for char in name.lower():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel_count += 1
    print(f'Vowels count: {vowel_count}')

    # Reverse the name.
    print(f"{name} reversed: {name[::-1]}")

# Call the function.   
get_characters("Eric")