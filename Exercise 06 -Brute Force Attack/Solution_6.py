## Exercise 6: Brute Force Attack - 30 Marks

#Write a program that simulates a password entry system. The correct password is defined as 12345. 
#The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

#Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. 
#If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

real_password = "12345"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    password = input("Enter the password: ")

    if password == real_password:
          print("Access has been granted, Welcome User!")
    else:
        attempts += 1
        if attempts == 5:
            print("You have attempted to enter 5 times but have failed, You are now locked out of this device")
        else:
            print(f"Incorrect password. { 5 - attempts} attempts remaining.")
