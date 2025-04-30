import json
import os

DATA_FILE = "students.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    subjects = {}
    for sub in ["Math", "Physics", "Chemistry"]:
        mark = float(input(f"Enter marks for {sub}: "))
        subjects[sub] = mark
    total = sum(subjects.values())
    average = total / len(subjects)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": subjects,
        "total": total,
        "average": average,
        "grade": grade
    }

    data = load_data()
    data.append(student)
    save_data(data)
    print("Student added successfully.\n")

def view_students():
    data = load_data()
    if not data:
        print("No student records found.\n")
        return
    for student in data:
        print(f"Name: {student['name']}")
        print(f"Roll: {student['roll']}")
        print("Marks:")
        for sub, mark in student['marks'].items():
            print(f"  {sub}: {mark}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print("-" * 30)

def main():
    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
