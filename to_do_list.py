from prettytable import PrettyTable

def loadTasks():
    mylist = []
    try:
        with open("mylist.txt", "r") as file:
            for line in file.readlines():
                mylist_type, completed_str = line.strip().split(",")
                completed = completed_str == "True"
                mylist.append({"task": mylist_type, "completed": completed})
    except FileNotFoundError:
        pass
    return mylist

def saveTasks(mylist):
    with open("mylist.txt", "w") as file:
        for task in mylist:
            file.write(f"{task['task']},{task['completed']}\n")

def addTask(mylist):
    task = input("Enter your task: ").strip()
    if task:
        mylist.append({"task": task, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def viewTasks(mylist):
    my_table = PrettyTable(["S.no", "Status", "Task"])
    if not mylist:
        print("No Tasks found")
    else:
        for i, task in enumerate(mylist, 1):
            if task["completed"]:
                status = "done"
            else:
                status="not done"
            my_table.add_row([i, status, task["task"]])
        print(my_table)

def completeTask(mylist):
    index = int(input("Enter task number to mark as complete: "))
    if 1 <= index <= len(mylist):
        mylist[index - 1]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def deleteTask(mylist):
    index = int(input("Enter task number to delete: "))
    if 1 <= index <= len(mylist):
        del mylist[index - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def deleteAllTasks(mylist):
    confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
    if confirm == "yes":
        mylist.clear()
        saveTasks(mylist)
        print("All tasks deleted successfully!")
    elif confirm == "no":
        print("Operation canceled.")
    else:
        print("Invalid input. Operation canceled.")

def main():
    mylist = loadTasks()
    while True:
        print("\n--To Do List--")
        print("--------------")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark as Complete")
        print("4. View Tasks")
        print("5. Delete all tasks")
        print("6. Exit\n")

        try:
            ch = int(input("Enter your choice: "))
            print("\n")

            if ch == 1:
                addTask(mylist)
                saveTasks(mylist)
            elif ch == 2:
                deleteTask(mylist)
                saveTasks(mylist)
            elif ch == 3:
                completeTask(mylist)
                saveTasks(mylist)
            elif ch == 4:
                viewTasks(mylist)
            elif ch == 5:
                deleteAllTasks(mylist)
            elif ch == 6:
                print("Closing......")
                break
            else:
                print("Invalid choice. Enter your choice again\n")
        except ValueError:
            print("Invalid choice. Enter a number.\n")

if __name__ == "__main__":
    main()
