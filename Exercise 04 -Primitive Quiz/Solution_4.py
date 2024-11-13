## Exercise 4: Primitive Quiz - 30 Marks

#In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
#Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
#Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.

def quiz():
    questions = {
        "1. What is the capital of France? ": "Paris",
        "2. What is the capital of Germany? ": "Berlin",
        "3. What is the capital of Italy? ": "Rome",
        "4. What is the capital of Spain? ": "Madrid",
        "5. What is the capital of Portugal? ": "Lisbon",
        "6. What is the capital of Sweden? ": "Stockholm",
        "7. What is the capital of Norway? ": "Oslo",
        "8. What is the capital of Denmark? ": "Copenhagen",
        "9. What is the capital of Finland? ": "Helsinki",
        "10. What is the capital of Greece? ": "Athens"
    }

    score = 0
    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", answer)

    print("Your final score is:", score, "out of 10")

quiz()