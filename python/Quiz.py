# Asking user if they want to play the quiz or not
print("Welcome to our Quiz")
play = input("Do you want to start? ")
if play.lower() != "yes":
    quit()

question_sheet = open("./python/questions.txt", "r")
answer_sheet = open("./python/answers.txt", "r")

sc = 0  # for the user_score count this variable is created

question = question_sheet.readline()
answer = str(answer_sheet.readline()).lower()

while question:
    print(question)
    user_answer = str(input("> ")).lower()
    user_answer = user_answer + "\n"

    if (answer == user_answer):
        sc = sc + 1
        print('Correct answer')
    else:
        print('Incorrect answer')

    question = question_sheet.readline(
    )  # Updating the question statements from the question sheet
    answer = answer_sheet.readline(
    )  # Updating the question statements from the question sheet

# Evaluating the score of the user
p = (sc * 100) / 7
p = "{:.2f}".format(p)
print("You answered ", sc, " correct questions with", p, "%")

question_sheet.close()
answer_sheet.close()
