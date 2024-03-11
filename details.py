#I will make 4 different variable and allow the user be prompted to input their answers this will be stored. 
#The variables will be name, age, house_number and street_name. 
#After this information is gathered, it will be then merged into one sentence.
#To do this we will print the sentence as a string data type using all the different variables. 

name = str(input("what is your name? "))
age = int(input("what is your age? "))
house_number = int(input("What is your house number? "))
street_name = str(input("What is your street name? "))

print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")