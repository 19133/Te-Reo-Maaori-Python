print("Welcome to the Te Reo Maaori quiz")
print("What is your wonderful name")
name = input()
print("Kia ora" + name)

played_before = input ("have you played the Te Reo Maaori quiz before" + name)

if played_before == "yes":
  print("Program continues")

elif played_before == "no":
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")

else:
  print("Please type yes or no")