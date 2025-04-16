isError = True
num1 = 11

while isError == True and num1 > 10:
  try:
    num1 = int(input("Enter a whole number less than 10"))
    isError = False

    if num1 > 10:
      print("You must enter a number less than 10")
      isError = True  
  
  except ValueError:
    print("You must enter a whole number.")
    
  
# What data type is the isError variable?
  # it is boolean

# What is the purpose of the isError variable?
  # so long as iserror is true, it will run the while statement, allowing the user to input numbers until they input a valid one

# Give two example of input that would trigger the except code.  
  # a word such as "word" would trigger the except code, along with any other word

# Give an example of input that would trigger the 'You must enter a number less than 10' error message.
  # any number greater than 10 such as 11 would trigger said error message