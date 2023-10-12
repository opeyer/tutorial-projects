# Letter Grade
# Pre-alpha version
# by Otto William Peyer IV

# Header
print('========================')
print('    LETTER     GRADE    ')
print('by   opeyer @ opeyer.com')
print('========================')

# Function
gradeScore = input("Enter your score (accepted range: 0.0-1.0): ")

try:
    gradeScoreFloat = float(gradeScore)
except:
    print("Bad score")
    
def computegrade(gradeScoreFloat):
    try:
        if gradeScoreFloat < 0.0:
            print("Your value is under 0.0! Please enter a numeric value from 0.0 to 1.0.")
        elif gradeScoreFloat > 1.0:
            print("Your value is over 1.0! Please enter a numeric value from 0.0 to 1.0.")
        elif gradeScoreFloat >= 0.9:
            print("A")
        elif gradeScoreFloat >= 0.8:
            print("B")
        elif gradeScoreFloat >= 0.7:
            print("C")
        elif gradeScoreFloat >= 0.6:
            print("D")
        elif gradeScoreFloat < 0.6:
            print("F")
    except:
        print("Your value is not a numeric value! Please enter a numeric value from 0.0 to 1.0.")

computegrade(gradeScore)
