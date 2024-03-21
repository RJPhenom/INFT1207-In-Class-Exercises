###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           January 31 2024
#   File:           ICE2_Updated.py
#   Description:    ***Updated version of ICE2 for use in ICE3***
#                   Program 'minimum' performs boundary testing on a list of
#                   elements separated by spaces. Tests for robustness.
###############################################################################

# CLASS
class MinimumFinder:
    # METHODS
    # find_minimum loops over each element in a list, and finds the lowest
    # integer among all elements. It skips all non-int convertible data types.
    def find_minimum(self, values_list):
        current_minimum = None  # init local minimum tracker

        # Loop through list to find min
        for element in values_list:
            # If minimum is still null, sets up first int as minimum
            if current_minimum is None:
                current_minimum = element

            # Else, if the current int element is less than the current
            # minimum, then it becomes the new minimum.
            elif element < current_minimum:
                current_minimum = element

        # Return the current_minimum we found, if any
        return current_minimum


if __name__ == '__main__':
    find_min = MinimumFinder()

