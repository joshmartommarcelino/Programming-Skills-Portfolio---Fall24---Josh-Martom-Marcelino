    ## Exercise 8: Simple Search - 30 Marks

    #Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

    ### Optional Requirements:
    #1. Allow the user to input the search term instead of using a predefined value.
    #2. Implement the search functionality based on user input.

names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]

what_is_your_name_bro = (input("What is the name you are looking for~?: "))

if what_is_your_name_bro in names:
    print(f"The name '{what_is_your_name_bro}' is in the list bro!")
else:
    print(f"The name '{what_is_your_name_bro}' is not in the list bro.")