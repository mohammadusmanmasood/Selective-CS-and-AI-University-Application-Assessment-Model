print("\nWelcome to University Application Assesment Tool For Computer Science and Artificial Intelligence UnderGraduate Apllicant Students \nThis is an opportunity for candidates hoping to get into highly selective universities to give thier applications\na relaistic apporach, hence this is for all the students planning to apply to top tier universites with acceptance rates below 25%")

print("You will be asked for your grades, extra curriculars and technical portfolio. \n")

print("Based on your profile and the accpeptance rate of your desired univeristy, \nwe will be giving you a prediction of your chance of getting accepted \n")

print("\n")
#desired university information

AcceptanceRate = input("Enter the Acceptance Rate of desired university\nnote that the acceptance rate should be below 25% for the program to work:   ")


while int(AcceptanceRate) > 25:
    AcceptanceRate = input("Enter the Acceptance Rate of desired university\nnote that the acceptance rate should be below 25% for the program to work:   ")


NameOfUniversity = input("Enter name of university:    ")

#Inputs For Application Evaluation

SAT = input("Enter you SAT score, if not given the SAT, Enter Zero:    ")

while int(SAT) > 1600 or int(SAT) < 0:
    SAT = input("Enter you SAT score, if not given the SAT, Enter Zero:    ")

ACT = input("Enter your ACT composite Score, if not given the ACT the Enter Zero:    ")

while int(ACT) > 36 or int(ACT) < 0:
    ACT = input("Enter your ACT composite Score, if not given the ACT the Enter Zero:    ")

AlevelsMath = input("Enter Grade for A level Math or Enter Zero:    ").strip().lower()
AlevelsPhysics = input("Enter grade for A level Physics or Enter Zero:    ").strip().lower()
AlevelSubjects = input("Enter the number of A level Subjects:    ")
Alvlavg = input("Enter you avg grade in A levels:    ").strip().lower()

Olevel = input("Number of subjects in o levels:    ")
Olvlavg = input("Enter you avg grade in O levels:    ").strip().lower()

EnglishProficency = input("Have you studied in English Medium School for more than five years:    ").strip().lower()

TechnicalProjects = input("Enter the number of technical projects you have done on kaggle, git hub or other:     ")

# data type
try:
    AcceptanceRate = int(AcceptanceRate)
    SAT = int(SAT)
    ACT = int(ACT)
    Olevel = int(Olevel)
    TechnicalProjects = int(TechnicalProjects)
    AlevelSubjects = int(AlevelSubjects)
except ValueError:
    print("Error: Please enter only numbers for scores and rates.")


#initialising to zero
FinalScore = 0
technicalportfolio = 0
Alvlsscore = 0
Olvlsscore = 0
englishstatus = 0
entrytestscore = 0

# main program

if AcceptanceRate <= 5:
    
    if SAT >= 1550 or ACT >= 33:
        entrytestscore = 10
    elif SAT >= 1500 or ACT >= 30:
        entrytestscore = 7
    elif SAT >= 1450 or ACT >= 28:
        entrytestscore = 5
    else:
        entrytestscore = 0
    
    
    if AlevelSubjects < 3:
        Alvlsscore = 0
    elif AlevelsMath == "0" or AlevelsPhysics == "0":
        Alvlsscore = 0
    elif Alvlavg == "a*":
        Alvlsscore = 10
    elif Alvlavg == "a":
        Alvlsscore = 7
    else:
        Alvlsscore = 0
    

    
    if Olevel >= 5 and Olvlavg == "a*":
        Olvlsscore = 5
    elif Olevel >= 5 and Olvlavg == "a":
        Olvlsscore = 4
    else:
        Olvlsscore = 0

    
    if TechnicalProjects == 0:
        technicalportfolio = 0
    elif TechnicalProjects >= 1 and TechnicalProjects <= 5:
        technicalportfolio = 5
    else:
        technicalportfolio = 10
    
    if EnglishProficency == "yes":
        englishstatus = 5

    FinalScore = entrytestscore + englishstatus + Alvlsscore + Olvlsscore + technicalportfolio
    
    
    if FinalScore >= 36:
        print("Your Chance of Getting Admitted in ", NameOfUniversity," is Above 90 Percent")
    elif FinalScore >= 33:
        print("your chance of getting admitted in ", NameOfUniversity, "is around 75 percent")
    elif FinalScore >= 28:
        print("Your chance of getting admitted in ", NameOfUniversity," is around 55 percent")
    elif FinalScore >= 22:
        print("your chance of getting admitted in" , NameOfUniversity, "is around 35 percent")
    else:
        print("Your chances of getting in", NameOfUniversity, "are too low")
    

elif AcceptanceRate > 5 and AcceptanceRate <= 15:
    
    if SAT >= 1520 or ACT >= 32:
        entrytestscore = 10
    elif SAT >= 1480 or ACT >= 28:
        entrytestscore = 8
    elif SAT >= 1430 or ACT >= 26:
        entrytestscore = 6
    elif SAT > 1400 or ACT >= 24:
        entrytestscore = 4
    
    
    if AlevelSubjects < 3:
        Alvlsscore = 0
    elif AlevelsMath == "0" or AlevelsPhysics == "0":
        Alvlsscore = 0
    elif Alvlavg == "a*":
        Alvlsscore = 10
    elif Alvlavg == "a":
        Alvlsscore = 8
    elif Alvlavg == 'b':
        Alvlsscore = 6
    else:
        Alvlsscore = 0
    

    
    if Olevel >= 5 and Olvlavg == "a*":
        Olvlsscore = 5
    elif Olevel >= 5 and Olvlavg == "a":
        Olvlsscore = 5
    elif Olevel >= 4 and Olvlavg == "a":
        Olvlsscore = 4
    elif Olevel >= 4 and Olvlavg == "b":
        Olvlsscore = 3
    elif Olevel >= 4 and Olvlavg == "c":
        Olvlsscore = 2
    else:
        Olvlsscore = 0

    
    if TechnicalProjects == 0:
        technicalportfolio = 0
    elif TechnicalProjects >= 1 and TechnicalProjects <= 3:
        technicalportfolio = 5
    else:
        technicalportfolio = 10
    
    if EnglishProficency == "yes":
        englishstatus = 5

    FinalScore = entrytestscore + englishstatus + Alvlsscore + Olvlsscore + technicalportfolio

    if FinalScore >= 34:
        print("Your Chance of Getting Admitted in ", NameOfUniversity," is Above 90 Percent")
    elif FinalScore >= 31:
        print("your chance of getting admitted in ", NameOfUniversity, "is around 75 percent")
    elif FinalScore >= 27:
        print("Your chance of getting admitted in ", NameOfUniversity," is around 60 percent")
    elif FinalScore >= 24:
        print("your chance of getting admitted in" , NameOfUniversity, "is around 40 percent")
    else:
        print("Your chances of getting in", NameOfUniversity, " are too low")
    

elif AcceptanceRate > 15 and AcceptanceRate <= 25:
    
    if SAT >= 1480 or ACT >= 29:
        entrytestscore = 10
    elif SAT >= 1420 or ACT >= 26:
        entrytestscore = 8
    elif SAT >= 1300 or ACT >= 23:
        entrytestscore = 5
    else:
        entrytestscore = 0
    
    
    if AlevelSubjects < 3:
        Alvlsscore = 0
    elif AlevelsMath == "0" or AlevelsPhysics == "0":
        Alvlsscore = 0
    elif Alvlavg == "a*":
        Alvlsscore = 10
    elif Alvlavg == "a":
        Alvlsscore = 8
    elif Alvlavg == 'b':
        Alvlsscore = 6
    elif Alvlavg == 'c':
        Alvlsscore = 3
    else:
        Alvlsscore = 0
    

    
    if Olevel >= 5 and Olvlavg == "a*":
        Olvlsscore = 5
    elif Olevel >= 5 and Olvlavg == "a":
        Olvlsscore = 5
    elif Olevel >= 4 and Olvlavg == "a":
        Olvlsscore = 4
    elif Olevel >= 4 and Olvlavg == "b":
        Olvlsscore = 3
    elif Olevel >= 4 and Olvlavg == "c":
        Olvlsscore = 1
    else:
        Olvlsscore = 0

    
    if TechnicalProjects == 0:
        technicalportfolio = 0
    elif TechnicalProjects >= 1 and TechnicalProjects <= 2:
        technicalportfolio = 5
    else:
        technicalportfolio = 10
    
    if EnglishProficency == "yes":
        englishstatus = 5

    FinalScore = entrytestscore + englishstatus + Alvlsscore + Olvlsscore + technicalportfolio

    if FinalScore >= 32:
        print("Your Chance of Getting Admitted in", NameOfUniversity," is Above 90 Percent")
    elif FinalScore >= 30:
        print("your chance of getting admitted in", NameOfUniversity, "is around 75 percent")
    elif FinalScore >= 26:
        print("Your chance of getting admitted in", NameOfUniversity, "is around 60 percent")
    elif FinalScore >= 22:
        print("your chance of getting admitted in" , NameOfUniversity, "is around 40 percent")
    else:
        print("Your chances of getting in", NameOfUniversity, "are too low")
