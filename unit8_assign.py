import json

# Create an empty dict.
inverted_dict = {}

# Open the input file in read mode.
with open('input_file.txt') as input_file:
    read_content = input_file.read()
        
    # Convert the string from the text file to a dict.
    write_content = json.loads(read_content) 

    # Iterate over the dict items and inverse the dictionary.
    for key, value in write_content.items():
        # If the value is a list.
        if isinstance(value, list):
            for item in value:
                if item not in inverted_dict:
                    inverted_dict[item] = [key]
                else:
                    inverted_dict[item].append(key)
        else:
            # If the value is not a list.
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)

    # Open the output file in write mode and write the inverted string.
    with open('output_file.txt', 'w') as output_file:
        write_content = output_file.write(json.dumps(inverted_dict))
