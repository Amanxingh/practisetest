import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Load saved tasks from tasks.json."""
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks so they remain available after restarting the app."""
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one to get started.")
        return

    print("\n--- YOUR TASKS ---")
    for task in tasks:
        status = "✓ Done" if task["done"] else "Pending"
        print(f'{task["id"]}. [{status}] {task["title"]} (created {task["created_at"]})')


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({
        "id": next_id,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_tasks(tasks)
    print("Task added successfully.")


def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print("That task is already complete.")
            else:
                task["done"] = True
                save_tasks(tasks)
                print("Task marked as complete.")
            return
    print("Task ID not found.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f'Deleted: {removed["title"]}')
            return
    print("Task ID not found.")


def main():
    tasks = load_tasks()
    while True:
        print("\n====== PYTHON TASK MANAGER ======")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
