## Exercise 7: Some Counting - 20 Marks

#Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
#in each case.
#* Write a loop that counts up from 0 to 50 in increments of 1.
#* Write a loop that counts down from 50 to 0 in decrements of 1.
#* Write a loop that counts up from 30 to 50 in increments of 1.
#* Write a loop that counts down from 50 to 10 in decrements of 2.
#* Write a loop that counts up from 100 to 200 in increments of 5.
#*You may include all loops in a single project*

print("0 to 50")
for i in range(0,51,1):
    print(i)
print("50 to 0")
for i in range(50,-1,-1):
    print(i)
print("30 to 50")
for i in range(30,51,1):
    print(i)
print("50 to 10")
for i in range(50,8,-2):
    print(i)
print("100 to 200")
for i in range(100,201,5):
  print(i)