# asks user if they would like to play the quiz on easy, medium, or hard
user_difficulty = input("What difficulty would you like to play. Easy, normal, or hard\n").lower()

# if easy, the program will print easy difficulty questions (Haven't made the questions and answer component yet)
if user_difficulty == "easy":
  print ("program continues")

# if medium, the program will print medium difficulty questions (Haven't made the questions and answer component yet)
elif user_difficulty == "medium":
  print ("program continues")

# if hard, the program will print hard difficulty questions (Haven't made the questions and answer component yet)
elif user_difficulty == "hard":
  print ("program continues")

else:
  print("please type easy, medium, or hard")