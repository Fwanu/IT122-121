def switch_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Satisfactory"
    elif score >= 60:
        return "Needs Improvement"
    elif score >= 0:
        return "Fail"
    else:
        return "Invalid score"


score = int(input("Enter your score: "))
print("Your grade is:", switch_grade(score))
