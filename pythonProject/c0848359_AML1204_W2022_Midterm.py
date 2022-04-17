# Final grade Calculator function to calculate the percentage of each exam and sum all the grades
def final_grade_calculator (studentNumber, assignmentGrade, midtermGrade, finaltermGrade, projectGrade):
        finalGrade = percentage_Calculator(assignmentGrade, 30) + \
                     percentage_Calculator(midtermGrade, 20) + \
                     percentage_Calculator(finaltermGrade, 20) + \
                     percentage_Calculator(projectGrade, 30)
        print(f"The student with the student number {studentNumber} has a final grade of {int(finalGrade)}")
        print(f"Student number {studentNumber}  has achieved the final grade of {int(finalGrade)} which is equivalent to {mark_assigner('c0848359', int(finalGrade))}")

# Mark assigner function to assign grade based on final grade
def mark_assigner (studentNumber, finalGrade):
    if (finalGrade < 0):
        return "Incorrect grade"
    if finalGrade > 95:
        return 'A+'
    elif finalGrade >= 90 and finalGrade < 95:
        return 'A'
    elif finalGrade >= 85 and finalGrade < 90:
        return 'A-'
    elif finalGrade >= 80 and finalGrade < 85:
        return 'B+'
    elif finalGrade >= 75 and finalGrade < 80:
        return 'B'
    elif finalGrade >= 70 and finalGrade < 75:
        return 'B-'
    elif finalGrade >= 65 and finalGrade < 70:
        return 'C+'
    elif finalGrade >= 60 and finalGrade < 65:
        return 'C'
    elif finalGrade >= 55 and finalGrade < 60:
        return 'C-'
    elif finalGrade >= 50 and finalGrade < 55:
        return 'D+'
    elif finalGrade >= 45 and finalGrade < 50:
        return 'D'
    elif finalGrade >= 40 and finalGrade < 45:
        return 'D-'
    elif finalGrade < 40:
        return 'Fail'

#instead of applying else if ladder and making function long its better to use dictionary to simplify it
def mark_assigner_better(studentNumber, finalGrade):
    grades = {
        8: 'D-',
        9: 'D',
        10: 'D+',
        11: 'C-',
        12: 'C',
        13: 'C+',
        14: 'B-',
        15: 'B',
        16: 'B+',
        17: 'A-',
        18: 'A',
        19: 'A+'
    }
    return grades[finalGrade // 5]


# helper function to calculate the percentage based on share of that exam to the total percentage
def percentage_Calculator(marks, percent_share):
    return percent_share * marks / 100


final_grade_calculator("C0848359", 80, 90, 60, 90)