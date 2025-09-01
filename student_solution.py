
def generate_bulletin_board(students, marks):
    """
    Function to generate the Student Bulletin Board.

    Parameters:
        students (list): A list of student names.
        marks (list of tuples): A list where each tuple contains the marks of a student.

    Returns:
        list: A nested list where each sublist contains:
              [Rank, Name, Average, Grade, GraceApplied]
    """
    # Valid Marks Condition - Checking whether every student has 5 different subjects marks
    student_data = []
    for mark in range(len(marks)):
        if len(marks[mark]) == 5:
            student_data.append((students[mark], marks[mark]))
    
    
    # Calculate the Average Marks of each student
    student_averages = []
    for student, mark in student_data:
        average = round(sum(mark) / 5, 2)
        student_averages.append([student, average])
      
        
    # Check for Grace Marks
    updated_student_averages = []
    for student_average in student_averages:
        student, avg_mark = student_average[0], student_average[1]
        if 59 <= avg_mark <= 60:
            avg_mark += 1
            grace_applied = "Yes"
        else:
            grace_applied = "No"
        updated_student_averages.append([student, avg_mark, grace_applied])
        
    
    # Assign Grade Bands
    graded_students = []
    for student in updated_student_averages:
        avg_mark = student[1]
        grade_band = ""
        if avg_mark < 60:
            grade_band = "Fail"
        elif 60 <= avg_mark < 65:
            grade_band = "Pass"
        elif 65 <= avg_mark < 75:
            grade_band = "Credit"
        elif 75 <= avg_mark < 85:
            grade_band = "Distinction"
        elif 85 <= avg_mark <= 100:
            grade_band = "High Distinction"
        graded_students.append([student[0], avg_mark, grade_band, student[2]])

    
    # Sorting the students in descending order by avg mark
    sorted_students = sorted(graded_students, key=lambda x: x[1], reverse=True)
    
    
    # Adding the relevant rank numbers
    final_students = []
    for index in range(1, len(sorted_students)+1):
        final_students.append([index] + sorted_students[index-1])
    
    for index in range(len(final_students)):
        current_student = final_students[index]
        if index == 0:
            current_student[0] = "1st rank"
        elif index == 1:
            current_student[0] = "2nd rank"
        elif index == 2:
            current_student[0] = "3rd rank"
        else:
            current_student[0] = str(current_student[0])
    
    return final_students