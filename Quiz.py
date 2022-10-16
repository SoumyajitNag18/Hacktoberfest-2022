print("Welcome to our Quiz")
play = input("Do you want to start? ")
if play.lower()!="yes": 
    quit()
sc=0
#QUESTION 1
ans= input("What is the full form of Ram?\n")
if ans.lower()=='random access memory':
    print('Correct answer')
    sc+=1
else:
    print('Incorrect answer') 
#QUESTION 2
ans= input("What is the full form of Rom?\n")
if ans.lower()=='read only memory':
    print('Correct answer')
    sc+=1
else:
    print('Incorrect answer') 
#QUESTION 3
ans= input("What is the full form of Lcd?\n")
if ans.lower()=='liquid crystal display':
    print('Correct answer')
    sc+=1
else:
    print('Incorrect answer') 
#QUESTION 4
ans= input("What is the upcoming generation of ram?\n")
if ans.lower()=='ddr5':
    print('\nCorrect answer')
    sc+=1
else:
    print('Incorrect answer') 
#QUESTION 5
ans= input("What are two desktop cpu making companies?\n")
if ans.lower()=='intel and amd':
    print('Correct answer')
    sc+=1
else:
    print('\nIncorrect answer') 
#QUESTION 6
ans= input("What is the full form of LED?\n")
if ans.lower()=='light emitting diode':
    print('Correct answer')
    sc+=1
else:
    print('Incorrect answer') 
#QUESTION 7
ans= input("Which is the cpu generation of Intel to support DDR5 ram?\n")
if ans.lower()=='12th generation':
    print('Correct answer')
    sc+=1
else:
    print('Incorrect answer') 
p= (sc*100)/7
p="{:.2f}".format(p)
print("You answered ", sc," correct questions with" ,p,"%")