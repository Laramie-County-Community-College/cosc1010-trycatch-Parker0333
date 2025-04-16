try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey, that wasn't a number!")
else:
    print("I see that you are " + age + " years old.")
#I predict that the code will print out the else statement, so long as it is a numerical value.
#My prediction was incorrect, upon entering a number I recieve a typeerror "can only cencatenate str (not "int") to str"