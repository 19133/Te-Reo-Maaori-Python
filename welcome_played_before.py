
#funtions

#Played before function
def played_before(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "yes" or user_response  == "y":   
        user_response = "yes"
        return user_response
      
    elif user_response == "no" or user_response  == "n":
        user_response = "no"
        return user_response 

    else:
      print("Please say yes or no") 

# welcomes user to the Te Reo Maaori quiz
print("Welcome to the Te Reo Maaori quiz")
# asks user thier name
print("What is your wonderful name")
name = input()
#Greets user in Te Reo Maaori
print("Kia ora" + name)

# asks user if they have played the Te Reo Maaori quiz before
played_quiz = played_before ("have you played the Te Reo Maaori quiz before" + name)

# if yes, the the program continues
if played_before == "yes":
  print("Program continues")

# else if no, then the program explains what it is then continues
elif played_before == "no":
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")

# else, asks user to type yes or no then the question repeats
else:
  print("Please type yes or no")