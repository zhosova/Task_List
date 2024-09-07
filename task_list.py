task_list = []

def add_task(task_list, task):
    task_list.append(task)

def view_tasks(task_list):
    for index, task in enumerate(task_list, 1):
        print(f"{index}. {task}")

def mark_complete(task_list, task_number):
    if 0 < task_number <= len(task_list):
        task_list.pop(task_number - 1)

def remove_task(task_list, task_number):
    if 0 < task_number <= len(task_list):
        task_list.pop(task_number - 1)

def menu():
    print("#")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("#")

while True:
    menu()
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task_list, task)
    elif choice == "2":
        view_tasks(task_list)
    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))
        remove_task(task_list, task_number)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

#Edit a task: Allow the user to modify existing tasks.
#Priorities: Assign priorities (e.g., low, medium, high) to tasks.
#1Due dates: Add due dates to tasks using Python’s datetime module.
#Refining the features: adding task deadlines, priorities, or categories.
#Enhancing the user interface: making the app more interactive, or adding a simple text-based UI.
#Adding data persistence: saving tasks to a file or a database so that they persist between runs.
#Debugging: fixing any issues in your code.
#More unit testing: covering additional edge cases and improving test coverage.
#Error Handling: Handle invalid inputs gracefully so that the program doesn’t crash (e.g., when a user enters a wrong option).