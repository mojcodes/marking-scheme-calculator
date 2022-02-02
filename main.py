# MOJcodes
# Putting it into practice


print("\nMarking scheme | Grade calculator \n"
      "----------------------MOJCODES-------------------------"
      "\n"
      "NOTES: There are 5 practical assessments worth 10% each"
      "\n1 project worth 50%"
      "\n-------------------------------------------------------")

#defining list
assessmentlist = []
#iterator set to 5, for each assessment score entered by user.
iterator = 5

for counter in range(0,iterator):
    response = int(input("Enter scores for assessment " +str(counter + 1) + ": "))
    assessmentlist.append(response)

projectscore = int(input("Enter project score of student: "))

# Function calculating total performance of a student i.e 10% assessments & 50% project
def calculate_total_performance(x,y):
    assessmenttotal = int(sum(x) * 0.1)
    projecttotal  = y * 0.5
    studenttotal = assessmenttotal + projecttotal
    # Return the result based on weightage supplied
    # 10 % from assessmentss
    # 50 % from project
    return(studenttotal)

# Function calculating the grade of the student
def assign_grade(score):
    if score >= 80:
       return "A, Student excellently passed this module"
    elif score >= 70:
       return "B, student passed this module"
    elif score >= 50:
      return "C, student passed this module"
    elif score >= 40:
      return "D, student passed this module but might consider repeating module"
    else:
       return "Student failed module. Please contact course department for repeat module"

print("\n")
print("-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("Student's total score: %s ", calculate_total_performance(assessmentlist, projectscore))
print("Grade: %s" % (assign_grade(calculate_total_performance(assessmentlist, projectscore))))
print("-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("\n")
