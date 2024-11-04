## Exercise 4: Primitive Quiz - 30 Marks

#In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
#Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
#Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.

Question_1 = (input("1.What is the capital of France: "))
Question_1 = Question_1.lower()
if Question_1 == "paris":
      print("You are Correct")
else:
      print("You are Wrong")

Question_2 = (input("2.What is the capital of Norway: "))
Question_2 = Question_2.lower()
if Question_2 == "oslo":
      print("You are Correct")
else:
      print("You are Wrong")

Question_3 = (input("3.What is the capital of Switzerland: "))
Question_3 = Question_3.lower()
if Question_3 == "bern":
      print("You are Correct")
else:
      print("You are Wrong")

Question_4 = (input("4.What is the capital of Hungary: "))
Question_4 = Question_4.lower()
if Question_4 == "budapest":
      print("You are Correct")
else:
      print("You are Wrong")

Question_5 = (input("5.What is the capital of Greece: "))
Question_5 = Question_5.lower()
if Question_5 == "athens":
      print("You are Correct")
else:
      print("You are Wrong")
    
Question_6 = (input("6.What is the capital of Latvia: "))
Question_6 = Question_6.lower()
if Question_6 == "riga":
      print("You are Correct")
else:
      print("You are Wrong")

Question_7 = (input("7.What is the capital of Bulgaria: "))
Question_7 = Question_7.lower()
if Question_7 == "sofia":
      print("You are Correct")
else:
      print("You are Wrong")

Question_8 = (input("8.What is the capital of Spain: "))
Question_8 = Question_8.lower()
if Question_8 == "madrid":
      print("You are Correct")
else:
      print("You are Wrong")

Question_9 = (input("9.What is the capital of Poland: "))
Question_9 = Question_9.lower()
if Question_9 == "warsaw":
      print("You are Correct")
else:
      print("You are Wrong")

Question_10 = (input("10.What is the capital of Sweden: "))
Question_10 = Question_10.lower()
if Question_10 == "stockholm":
      print("You are Correct")
else:
      print("You are Wrong") 
print("Quiz Completed")