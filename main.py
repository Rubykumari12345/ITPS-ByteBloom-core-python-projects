import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Task Title: ").strip()
    prio = input("Priority (High/Medium/Low): ").strip().title()
    due = input("Due Date (YYYY-MM-DD): ").strip()
    tid = len(tasks) + 1
    tasks.append({"id": tid, "title": title, "prio": prio, "due": due, "status": "Pending"})
    save_tasks(tasks)
    print("Task added!")

def show_tasks(tasks, status=None):
    for t in tasks:
        if status is None or t["status"] == status:
            print(f"[{t['id']}] {t['title']} | {t['prio']} | Due: {t['due']} | {t['status']}")

def mark_done(tasks):
    try:
        tid = int(input("Completed Task ID: "))
    except ValueError:
        return
    for t in tasks:
        if t["id"] == tid:
            t["status"] = "Completed"
            save_tasks(tasks)
            print("Task completed!")
            return

def del_task(tasks):
    try:
        tid = int(input("Delete Task ID: "))
    except ValueError:
        return
    for i, t in enumerate(tasks):
        if t["id"] == tid:
            tasks.pop(i)
            save_tasks(tasks)
            print("Task deleted!")
            return

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task  2. Pending  3. Completed  4. Mark Done  5. Delete  6. Exit")
        ch = input("Choice: ").strip()
        if ch == "1": add_task(tasks)
        elif ch == "2": show_tasks(tasks, "Pending")
        elif ch == "3": show_tasks(tasks, "Completed")
        elif ch == "4": mark_done(tasks)
        elif ch == "5": del_task(tasks)
        elif ch == "6": break
        else: print("Galat choice!")

if __name__ == "__main__":
    main()