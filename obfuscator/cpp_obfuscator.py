import re
import random
import string
import os
def variable_renamer(given_string):
    """
    Function to rename all variables and functions in C++ code.
    given_string is a string of C++ code.
    """
    # Variable declarations:
    variable_dictionary = {}
    special_cases = {"typedef", "unsigned", "std", "class", "struct", "namespace", "using", "public", "private", "protected", "return", "if", "else", "for", "while", "int", "char", "float", "double", "void"}
    index = 0
    new_string = ""

    # Split the code to indicate when it enters/exits a string
    split_code = re.split('\"', given_string)
    
    # REGEX to find all function and variable declarations ignoring main
    filtered_code = re.findall(
        r"(?:\w+\s+)(?!main)(?:\*)*([a-zA-Z_][a-zA-Z0-9_]*)", given_string)

    # For loop to add examples found from running a REGEX to a dictionary object
    # Ignores special cases and repeats
    # When a value is entered it is also assigned a random string of length 12
    for found_example in filtered_code:
        if found_example not in special_cases:
            if found_example not in variable_dictionary:
                variable_dictionary[found_example] = random_string(12)

    # For each even section in split code (odd indicates that it is in a string)
    # replace all of the variable and function names with what is defined in the dictionary
    for section in split_code:
        if index % 2 == 0:
            for entry in variable_dictionary:
                # Used \W because we don't want to replace a variable if it is inside another word.
                re_string = r"\W{}\W".format(entry)
                while True:
                    first_found_entry = re.search(re_string, section)
                    if not first_found_entry:
                        break
                    # Get the iterator start and end points of the searched re_string
                    start = first_found_entry.start(0)
                    end = first_found_entry.end(0)
                    section = section[:start+1] + variable_dictionary[entry] + section[end-1:]
        # Add the current section back to make the original string but with obfuscated names
        # Accounts for adding a quote every time except for the first scenario
        if index >= 1:
            new_string = new_string + "\"" + section
        else:
            new_string = new_string + section
        index += 1

    return new_string


def random_string(stringLength=8):
    """
    Function to generate a random string.
    Can pass it an integer string length to make it that size else it will be 8
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# def whitespace_remover(a):
#     """
#     Function to remove all whitespace, ensuring #include is on its own line,
#     and maintaining a single space between `namespace` and `std`.
#     """
#     splits = re.split('\"', a)  # Split by strings to avoid messing with strings
#     index = 0
#     a = ""
#     for s in splits:
#         if index % 2 == 0:
#             # Ensure that #include statements are each on a new line
#             s_spaceless = re.sub(r"^\s*#include\s+(.*)", r"\n#include \1", s)

#             # Ensure there is exactly one space between `namespace` and `std`
#             s_spaceless = re.sub(r"\bnamespace\s+std\s*;", "namespace std;", s_spaceless)

#             # Remove excessive spaces everywhere else
#             s_spaceless = re.sub(r"\s+", " ", s_spaceless)  # Replace multiple spaces with a single space
#             s_spaceless = re.sub(r"[\s]$", "", s_spaceless)  # Remove trailing spaces

#         else:
#             s_spaceless = s  # Do nothing with string content

#         if index >= 1:
#             a = a + "\"" + s_spaceless
#         else:
#             a = a + s_spaceless
#         index += 1
#     return a

import re

def whitespace_remover(a):
    """
    Function to ensure each #include directive is on its own line,
    and that there is exactly one space after `namespace` and `std`.
    It does not flatten the entire code.
    """
    splits = re.split('\"', a)  # Split by strings to avoid messing with strings
    index = 0
    a = ""

    for s in splits:
        if index % 2 == 0:
            # Ensure that each #include directive is on its own line
            s_spaceless = re.sub(r"#include(<.*?>|\S+)", r"#include \1", s)
            
            # Ensure there's exactly one space between `namespace` and `std`
            s_spaceless = re.sub(r"\bnamespace\s+std\s*;", "namespace std;", s_spaceless)
        else:
            s_spaceless = s  # Don't modify the content inside strings

        # Append the processed code
        if index >= 1:
            a = a + "\"" + s_spaceless
        else:
            a = a + s_spaceless
        
        index += 1

    return a


def comment_remover(given_string):
    """
    Function to remove C++ and C style comments
    given_string is a string of C++ code
    """
    # This does not take into account if a C++ style comment happens within a string
    # i.e. "Normal String // With a C++ comment embedded inside"
    cpp_filtered_code = re.findall(r"\/\/.*", given_string)
    for entry in cpp_filtered_code:
        given_string = given_string.replace(entry, "")

    # This is a basic start for C style block comments
    c_filtered_code = re.findall(r"\/\*.*\*\/", given_string)
    for entry in c_filtered_code:
        given_string = given_string.replace(entry, "")

    return given_string


import os

def process_file(input_path, output_path):
    """
    Process a single C++ source file and save it with a user-defined output name.
    """
    print(f"\nProcessing: {input_path}")
    try:
        with open(input_path, "r", encoding="utf-8") as file_data:
            file_string = file_data.read()

        file_string = comment_remover(file_string)
        file_string = variable_renamer(file_string)
        file_string = whitespace_remover(file_string)

        # Save the obfuscated code to the output file specified by the user
        with open(output_path, "w+", encoding="utf-8") as f:
            f.write(file_string)
        
        print(f"Obfuscation complete! Output saved to: {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")


def main():
    """
    The main function to begin the obfuscation of C++ code files
    """
    cwd = input('Path to C++ Source Files Directory or File: ').strip()

    if os.path.isfile(cwd):  # If a file is given, process only that file
        process_file(cwd)
    elif os.path.isdir(cwd):  # If a directory is given, process all .cpp and .h files
        print(f"Looking for C++ Source Files in {cwd}...\nLog:")
        for filename in os.listdir(cwd):
            file_path = os.path.join(cwd, filename)
            if filename.endswith((".cpp", ".h")):
                process_file(file_path)
            else:
                print(f"Skipping {filename} (Not a C++ source file)")
    else:
        print(f"Error: {cwd} is neither a file nor a directory. Please enter a valid path.")


if __name__ == "__main__":
    main()
