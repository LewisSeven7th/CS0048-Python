def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print("Task added.")

def remove_task(todo_list):
    task = input("Enter the task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed.")
    else:
        print("Task not found in the list.")

def view_tasks(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your tasks:")
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            remove_task(todo_list)
        elif choice == '3':
            view_tasks(todo_list)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()