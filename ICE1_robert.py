###############################################################################
#   Title:          ICE 1
#   Author:         Robert Macklem
#   Date:           January 19, 2024
#   Description:    Python Source File (.py)
#
#                   This program calculates the average budget of movies from
#                   a provided dataset, then i) prints out the avergae budget, 
#                   ii) the movies (and their budgets) that had higher budgets 
#                   than average, and iii) the number of movies that had higher
#                   budgets than average.
#
#                   This program allows for users to append movies to the
#                   dataset prior to processing.
#
###############################################################################

#CONST
#Reusable output string
output = "{}: with a budget of {}, it is {} greater than average"

#VARS
#Default movies list (set of 2-tuples)
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

#FUNCTIONS
#Function for appending new movie data supplied by user, runs as many times
#as requested through the parameter 'num', which represents the number of
#movies to be added, which is gathered from user input in the main program
def add_movies(num : int = 0):
    for i in range(num):
        #Includes user input validation check, just to make sure the budget
        #they input is useable and the program can continue
        title = input("Please enter the title of the movie: ")
        validation_passed = False
        while not validation_passed:
            try:
                budget = int(input("Please enter the budget of the movie: "))
                movies.append((title, budget))
                validation_passed = True

            except:
                print("\nPlease enter whole numbers (rounded to the nearest one)")
                print("for the movie budget. Decimals are not accepted.\n")


#Simple avergaing function with movies list as the default parameter
def get_average_budget(movie_data : list = movies):
    total_budgets = 0
    for movie in movies:
        total_budgets += movie[1]
    
    return int(total_budgets/len(movies))

#Function that loops over the list of movies, printing out those movies that
#have budgets higher than average, and the difference by how much they are
#above average. For each movies that meets this condition, it counts it and
#returns the final count once the loop is complete
def count_high_budget_movies(average : int, movie_list : list = movies):
    movies_over_avg = 0
    for movie in movies:
        if movie[1] > average:
            movies_over_avg += 1
            budget_difference = int(movie[1] - average)
            print(output.format(movie[0], movie[1], budget_difference))
    
    return movies_over_avg

#PROGRAM
#Add new movies to the dataset first, scoped inside a while loop that does
#simple validation, letting users know only positive or zero integers will
#be accepted for any numeric inputs
validation_passed = False
while not validation_passed:
    try:
        add_movies(int(input("\nPlease enter the number of movies to add: ")))
        validation_passed = True

    except:
        print("\nPlease use zero or positive integers only for all numbers.")

#Then calculate the average
average = get_average_budget()

#Output the average budget
print("\nThe average budget of the data set is {}".format(average))
print("\nThe movies who have a higher budget than average include:")

#Output movies with higher than average budget using our counting function
high_budget_movies = count_high_budget_movies(average)

#Output the number of movies that had higher than average budgets
print("\n{} movies had budgets over the average!\n".format(high_budget_movies))