import csv
import json
import os
from abc import ABC, abstractmethod
from datetime import datetime



class Task:
    def __init__(self, t_id, title, description, due_date, status):
        self.t_id = t_id
        self.title = title
        self.des = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.t_id,
            "title": self.title,
            "description": self.des,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data["due_date"], data["status"])

class Storage(ABC):
    @abstractmethod
    def save_tasks(self, tasks):
        pass

    @abstractmethod
    def load_tasks(self):
        pass


class CSVStorage(Storage):
    FILE_NAME = "tasks.csv"

    def __init__(self, filename=FILE_NAME):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["task_id", "title", "description", "due_date", "status"])

    def load_tasks(self):
        tasks = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
        return tasks

    def save_tasks(self, tasks):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            writer.writerows(tasks)


class JSONStorage(Storage):
    FILE_NAME = "tasks.json"
    def __init__(self, filename=FILE_NAME):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file)

    def load_tasks(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump(tasks, file, indent=4)


class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self):
        task_id = input("Enter Task ID: ")
        if any(task["task_id"] == task_id for task in self.tasks):
            print("Task ID already exists! Try again.")
            return

        title = input("Enter Title: ")
        description = input("Enter Description: ")

        while True:
            due_date = input("Enter Due Date (YYYY-MM-DD) or press Enter to skip: ")
            if due_date == "" or self.validate_date(due_date):
                break
            print("Invalid date format! Please enter in YYYY-MM-DD format.")

        while True:
            status = input("Enter Status (Pending/In Progress/Completed): ").capitalize()
            if status in ["Pending", "In Progress", "Completed"]:
                break
            print("Invalid status! Choose from Pending, In Progress, or Completed.")

        self.tasks.append(
            {"task_id": task_id, "title": title, "description": description, "due_date": due_date, "status": status})
        self.storage.save_tasks(self.tasks)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task["task_id"] == task_id:
                task["title"] = input(f"Enter new title [{task['title']}]: ") or task["title"]
                task["description"] = input(f"Enter new description [{task['description']}]: ") or task["description"]
                while True:
                    new_due_date = input(f"Enter new Due Date [{task['due_date']}] or press Enter to keep: ")
                    if new_due_date == "" or self.validate_date(new_due_date):
                        task["due_date"] = new_due_date or task["due_date"]
                        break
                    print("Invalid date format!")
                while True:
                    new_status = input(
                        f"Enter new status (Pending/In Progress/Completed) [{task['status']}]: ").capitalize()
                    if new_status in ["Pending", "In Progress", "Completed"]:
                        task["status"] = new_status
                        break
                    print("Invalid status!")
                self.storage.save_tasks(self.tasks)
                print("Task updated successfully!")
                return
        print("Task ID not found!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task["task_id"] != task_id]
        self.storage.save_tasks(self.tasks)
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter status to filter (Pending/In Progress/Completed): ").capitalize()
        filtered = [task for task in self.tasks if task["status"] == status]
        if not filtered:
            print("No tasks found for this status.")
        for task in filtered:
            print(task)

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def menu(self):
        while True:
            print("\nTo-Do Application")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Filter Tasks")
            print("6. Exit")

            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    self.add_task()
                case 2:
                    self.view_tasks()
                case 3:
                    self.update_task()
                case 4:
                    self.delete_task()
                case 5:
                    self.filter_tasks()
                case 6:
                    print("Exiting... Goodbye!"); break
                case _:
                    print("Invalid choice! Try again.")


if __name__ == "__main__":
    while True:
        storage_type = input("Choose storage type (json/csv): ").strip().lower()
        if storage_type == "json":
            storage = JSONStorage()
            break
        elif storage_type == "csv":
            storage = CSVStorage()
            break
        else:
            print("Invalid storage type! Please enter 'json' or 'csv'.")

    manager = TaskManager(storage)
    manager.menu()


