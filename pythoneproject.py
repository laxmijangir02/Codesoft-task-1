class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.name}"
import os

class ToDoApp:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, completed = line.strip().split(" | ")
                    task = Task(name)
                    if completed == "True":
                        task.mark_completed()
                    self.tasks.append(task)

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name} | {task.completed}\n")

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, task_index):
        task = self.tasks[task_index - 1]
        task.mark_completed()
        self.save_tasks()

    def delete_task(self, task_index):
        del self.tasks[task_index - 1]
        self.save_tasks()

    def show_menu(self):
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                task_name = input("Enter the task name: ")
                self.add_task(task_name)
            elif choice == "3":
                task_index = int(input("Enter task number to mark as completed: "))
                self.mark_task_completed(task_index)
            elif choice == "4":
                task_index = int(input("Enter task number to delete: "))
                self.delete_task(task_index)
            elif choice == "5":
                print("Exiting To-Do list application...")
                break
            else:
                print("Invalid choice, please try again.")
if __name__ == "__main__":
    app = ToDoApp()
    app.run()
