import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\n" + "="*50)
    print(f"{'ID':<5} {'Status':<10} {'Priority':<10} {'Task':<25}")
    print("="*50)
    for task in tasks:
        status = "[X]" if task['completed'] else "[ ]"
        print(f"{task['id']:<5} {status:<10} {task['priority']:<10} {task['title']:<25}")
    print("="*50)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    priority = input("Enter priority (high/medium/low): ").strip().lower()
    if priority not in ['high', 'medium', 'low']:
        priority = 'medium'
    task_id = max([t['id'] for t in tasks], default=0) + 1
    new_task = {
        'id': task_id,
        'title': title,
        'priority': priority,
        'completed': False,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def update_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    for task in tasks:
        if task['id'] == task_id:
            print(f"\nCurrent task: {task['title']}")
            new_title = input("Enter new title (or press Enter to keep current): ").strip()
            if new_title:
                task['title'] = new_title
            new_priority = input("Enter new priority (high/medium/low) or Enter to keep: ").strip().lower()
            if new_priority in ['high', 'medium', 'low']:
                task['priority'] = new_priority
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted successfully!")
            return
    print("Task not found.")

def mark_complete(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to mark as complete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"Task '{task['title']}' marked as complete!")
            return
    print("Task not found.")

def show_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    high = sum(1 for t in tasks if t['priority'] == 'high' and not t['completed'])
    print("\n--- Task Statistics ---")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"High priority pending: {high}")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Show Statistics")
        print("7. Exit")
        choice = input("\nEnter your choice (1-7): ").strip()
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_complete(tasks)
        elif choice == '6':
            show_statistics(tasks)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
