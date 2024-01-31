###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           January 31 2024
#   File:           ICE2_robert.py
#   Description:    Program 'minimum' performs boundary testing on a list of
#                   elements separated by spaces. Tests for robustness.
###############################################################################

# VARS
split_list = None  # init our list
minimum = None  # init our minimum


# FUNCS
# find_minimum loops over each element in a list, and finds the lowest
# integer among all elements. It skips all non-int convertible data types.
def find_minimum(values_list):
    current_minimum = None  # init local minimum tracker
    for element in values_list:
        try:
            int_element = int(element)  # Cast current element as int

            # If minimum is still null, sets up first int as minimum
            if current_minimum is None:
                current_minimum = int_element

            # Else, if the current int element is less than the current
            # minimum, then it becomes the new minimum.
            elif int_element < current_minimum:
                current_minimum = int_element

        except:  # If there is exception (cast to int failed) then skip
            continue

    # Return the current_minimum we found, if any
    return current_minimum


# PROGRAM
# Start with the welcome message and user prompt
print("\nWelcome to the Minimum Program.")
print("Enter any list and we'll find the minimum integer value in it!")

# While we do not have a valid list to work with
# loop for valid list that can be split on " ".
while split_list is None:
    try:  # Processing to split list
        raw_input = input("\nPlease enter your list now: ")  # Prompt
        split_list = raw_input.split()  # Split

    except:  # Exception handling if input cannot be split (prints and loops)
        print("***ERROR***")
        print("This list you entered could not be parsed.")
        print("Please re-enter using only integers separated by spaces.")

# Skips function processing if list is empty, prevents any possible issues
if len(split_list) == 0:
    print("\nYour list contained no integers, therefore there was no minimum.")

# If we have a good list with at least 1 element, run the function
else:
    minimum = find_minimum(split_list)

    # It's possible to have a len > 0 list with no ints, so check if the
    # current minimum is still null (func ran and found no ints)
    if minimum is not None:
        print(f"\nCongratulations! Your minimum element is {minimum}")
        print("Goodbye")

    else:
        print("\nYour list contained no integers, therefore there was no minimum.")

