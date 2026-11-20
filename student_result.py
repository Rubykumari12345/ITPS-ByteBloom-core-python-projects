import json
import os

FILE_NAME = "results.json"
SUBJECTS = ["Maths", "Science", "English", "Computer"]

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def calc_grade_status(pct, all_pass):
    if not all_pass or pct < 33:
        return "F", "Fail"
    if pct >= 80: return "A", "Pass"
    if pct >= 60: return "B", "Pass"
    if pct >= 45: return "C", "Pass"
    return "D", "Pass"

def add_student(students):
    roll = input("Roll Number: ").strip()
    name = input("Student Name: ").strip().title()
    marks = {}
    all_pass = True
    try:
        for sub in SUBJECTS:
            m = float(input(f"{sub} marks (0-100): "))
            marks[sub] = m
            if m < 33:
                all_pass = False
    except ValueError:
        print("Marks sirf numbers mein dalein.")
        return

    total = sum(marks.values())
    pct = round(total / len(SUBJECTS), 2)
    grade, status = calc_grade_status(pct, all_pass)
    students.append({"roll": roll, "name": name, "marks": marks, "pct": pct, "grade": grade, "status": status})
    save_data(students)
    print("Student result save ho gaya!")

def search_student(students):
    roll = input("Search Roll Number: ").strip()
    for s in students:
        if s["roll"] == roll:
            print(f"\n{s['name']} ({s['roll']}) -> {s['pct']}% | Grade: {s['grade']} | {s['status']}")
            print("Marks:", s["marks"])
            return
    print("Record nahi mila.")

def all_report(students):
    print("\n--- All Students Report ---")
    for s in students:
        print(f"{s['roll']} | {s['name']} | {s['pct']}% | Grade: {s['grade']} | {s['status']}")

def main():
    students = load_data()
    while True:
        print("\n1. Add Student  2. Search by Roll No  3. All Report  4. Exit")
        ch = input("Choice: ").strip()
        if ch == "1": add_student(students)
        elif ch == "2": search_student(students)
        elif ch == "3": all_report(students)
        elif ch == "4": break
        else: print("Galat choice!")

if __name__ == "__main__":
    main()