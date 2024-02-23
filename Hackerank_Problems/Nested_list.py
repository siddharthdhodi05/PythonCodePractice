if __name__ == '__main__':
    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # === My code starts on line 7 ===
        student_grades.append([name, score])
        
    # Sorting the student_grades list by score
    student_grades.sort(key=lambda x: x[1])
    
    # Finding the minimum score
    min_grade = student_grades[0][1]
    
    # Finding the second minimum score
    second_min_grade = None
    for i in range(1, len(student_grades)):
        if student_grades[i][1] > min_grade:
            second_min_grade = student_grades[i][1]
            break
        
    # Collecting names of students with the second minimum grade
    second_min_names = []
    for student in student_grades:
        if student[1] == second_min_grade:
            second_min_names.append(student[0])
    
    # Printing names in alphabetical order
    for name in sorted(second_min_names):
        print(name)
    
