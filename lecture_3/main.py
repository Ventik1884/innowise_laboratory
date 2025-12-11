students = []

def add_student():
    name = input("Enter student name: ").strip()
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists.")
            return
    students.append({"name": name.title(), "grades": []})
    print(f"Student '{name}' added successfully.")

def add_grades():
    name = input("Enter student name to add grades: ").strip()
    for student in students:
        if student["name"].lower() == name.lower():
            print("Enter grades (0-100). Type 'done' to finish.")
            while True:
                grade_input = input("Grade: ").strip()
                if grade_input.lower() == 'done':
                    break
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                        print(f"Grade {grade} added.")
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter an integer between 0 and 100 or 'done'.")
            return
    print(f"Student '{name}' not found.")

def show_report():
    if not students:
        print("No students in the system.")
        return

    has_any_grades = any(s["grades"] for s in students)
    if not has_any_grades:
        print("No grades have been entered yet.")
        return

    print("\n--- Student Report ---")
    averages = []
    for student in students:
        grades = student["grades"]
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)
        else:
            print(f"{student['name']}'s average grade is N/A.")
    if averages:
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages)/len(averages):.1f}")
    print()

def find_top_performer():
    if not students:
        print("No students in the system.")
        return

    # Список студентов с оценками
    students_with_grades = [s for s in students if s["grades"]]
    if not students_with_grades:
        print("No grades have been entered yet.")
        return

    top_student = max(
        students_with_grades,
        key=lambda s: sum(s["grades"]) / len(s["grades"])
    )
    top_average = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_average:.1f}.")

def main():
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report(all students)")
        print("4. Find top student")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grades()
        elif choice == 3:
            show_report()
        elif choice == 4:
            find_top_performer()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()