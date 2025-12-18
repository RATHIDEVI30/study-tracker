class Task:
    def __init__(self, subject, status="Not Started"):  # Fixed constructor
        self.subject = subject
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

class StudyTracker:
    def __init__(self):  # Fixed constructor
        self.tasks = []

    def add_task(self):
        subject = input("Enter Subject/Topic: ")
        self.tasks.append(Task(subject))
        print("Task Added\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet\n")
            return
        print("Tasks List:")
        for i, t in enumerate(self.tasks, 1):
            print(f"{i}. {t.subject} - {t.status}")
        print()

    def update_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter task number: ")) - 1
            if 0 <= index < len(self.tasks):
                print("1. Not Started")
                print("2. In Progress")
                print("3. Completed")
                choice = int(input("Choose status: "))
                status = ["Not Started", "In Progress", "Completed"]
                if 1 <= choice <= 3:
                    self.tasks[index].update_status(status[choice - 1])
                    print("Status Updated\n")
                else:
                    print("Invalid option\n")
            else:
                print("Invalid task number\n")
        except ValueError:
            print("Enter a valid number\n")

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
                print("Task Deleted\n")
            else:
                print("Invalid number\n")
        except ValueError:
            print("Enter a valid number\n")

    def show_progress(self):
        if not self.tasks:
            print("No tasks to calculate\n")
            return
        total = len(self.tasks)
        completed = sum(t.status == "Completed" for t in self.tasks)
        print("Progress Report")
        print(f"Total Tasks: {total}")
        print(f"Completed Tasks: {completed}\n")

# Main loop
tracker = StudyTracker()

while True:
    print("Study Tracker")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Show Progress")
    print("6. Exit")
    try:
        choice = int(input("Choose option: "))
        if choice == 1:
            tracker.add_task()
        elif choice == 2:
            tracker.view_tasks()
        elif choice == 3:
            tracker.update_task()
        elif choice == 4:
            tracker.delete_task()
        elif choice == 5:
            tracker.show_progress()
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Invalid option\n")
    except ValueError:
        print("Enter numbers only\n")