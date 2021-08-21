
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

print("Welcome to the Te Reo Maaori quiz")
print("What is your wonderful name")
name = input()
print("Kia ora" + name)

played_quiz = played_before ("have you played the Te Reo Maaori quiz before" + name)

if played_before == "yes":
  print("Program continues")

elif played_before == "no":
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")

else:
  print("Please type yes or no")