name_of_student = input("Please enter your name: ")
name_of_course = input("Please enter the name of your course: ")
error_statement = "Invalid entry, please try again."

# Section for input of assigned weights.

while True:
    try:
        weight_of_quizzes = float(input("Please input the weight of your quizzes, a number between 0 and 1: "))
        if 0.0 <= weight_of_quizzes <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        weight_of_projects = float(input("Please input the weight of your projects, a number between 0 and 1: "))
        if 0.0 <= weight_of_projects <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        weight_of_activities = float(input("Please input the weight of your activities, a number between 0 and 1: "))
        if 0.0 <= weight_of_activities <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        weight_of_attendance = float(input("Please input the weight of your attendance, a number between 0 and 1: "))
        if 0.0 <= weight_of_attendance <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        weight_of_exams = float(input("Please input the weight of your exams, a number between 0 and 1: "))
        if 0.0 <= weight_of_exams <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

# Section for input of average scores.

while True:
    try:
        average_score_for_quizzes = float(input("Please input your average score for quizzes, a number between 0 and 1: "))
        if 0.0 <= average_score_for_quizzes <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        average_score_for_projects = float(input("Please input your average score for projects, a number between 0 and 1: "))
        if 0.0 <= average_score_for_projects <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        average_score_for_activites = float(input("Please input your average score for activites, a number between 0 and 1: "))
        if 0.0 <= average_score_for_activites <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        average_score_for_attendance = float(input("Please input your average score for attendance, a number between 0 and 1: "))
        if 0.0 <= average_score_for_attendance <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

while True:
    try:
        average_score_for_exams = float(input("Please input your average score for exams, a number between 0 and 1: "))
        if 0.0 <= average_score_for_exams <= 1.0:
            break
        print("Invalid input, please try again.")
    except Exception as error_statement:
        print(error_statement)
    except ValueError:
        print(error_statement)

# This section calculates the scores.

weighted_average_quiz_score = weight_of_quizzes * average_score_for_quizzes
weighted_average_project_score = weight_of_projects * average_score_for_projects
weighted_average_activities_score = weight_of_activities * average_score_for_activites
weighted_average_attendance_score = weight_of_attendance * average_score_for_attendance
weighted_average_exam_score = weight_of_exams * average_score_for_exams

final_grade_in_course = weighted_average_quiz_score + weighted_average_project_score + weighted_average_activities_score + weighted_average_attendance_score + weighted_average_exam_score

final_percent_grade_in_class = final_grade_in_course * 100

print()
print()
print("Hi " + name_of_student + ", thank you for using my calculator! You have a " + str(final_percent_grade_in_class) + " in " + name_of_course + ".")

# This code did not get the tenths percentage as accurately as needed. print("Thank you for the input " + name_of_student + ", you have a " + "{0:.0%}".format(final_grade_in_course) + " in " + name_of_course + ".")