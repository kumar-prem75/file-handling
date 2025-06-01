# Task manager using File handling
def add_task():
    task = input("Enter you task: ")
    
    priority = input("Enter Priority (High/Medium/Low): ").strip().capitalize()
    category = input("Enter Category (Work/Personal/Others): ").strip().capitalize()
    due_date = input("Enter Due Date (DD/MM/YY): ").strip()
    
    with open("task.txt","a") as f:
        f.write(f"[ ] {task} | Priority: {priority} | Category: {category} | Due: {due_date}\n")
    print("Task successfully added!")
    
def view_task():
    with open("task.txt","r") as f:
        tasks = f.readlines()
        
    if not tasks:
        print("No taks found.")
        return
    
    print("\nChoose sorting order")
    print("1. Completed First")
    print("2. Incompleted First")
    print("3. Alphabetically First")
    
    choice = input("Enter your choice: ")
    sorted_task = tasks
    
    completed_task = [t.strip() for t in tasks if t.startswith("[✓]")]
    incompleted_task = [t.strip() for t in tasks if t.startswith("[ ]")]
    
    if choice == "1":
        sorted_tasks = completed_task + incompleted_task
    elif choice == "2":
        sorted_task = incompleted_task + completed_task
    elif choice == "3":
        sorted_tasks = sorted(tasks, key=lambda t: t.strip("[✓] [ ]").lower())
    else:
        print("Invlaid option!")
        return
    
    print("\n-----Sorted Tasks-----")
    for i,task in enumerate(sorted_tasks,start = 1):
        print(f"{i}. {task}")
        
def incomplete():
    print("\n-----INCOMPLETE TASKS-----")
    try:
        with open("task.txt","r") as f:
            tasks = f.readlines()
            for task in tasks:
                if task.strip().startswith("[ ]"):
                    print(task.strip())
    except FileNotFoundError:
        print("Task is not found!")
        
def complete():
    print("\n-----COMPLETED TASK-----")
    try:
        with open("task.txt","r") as f:
            tasks = f.readlines()
            for task in tasks:
                if task.strip().startswith("[✓]"):
                    print(task.strip())
    except FileNotFoundError:
        print("Task is not found!")
        
def mark_complete():
    with open("task.txt","r") as f:
        tasks = f.readlines()
        
    print("\n---ALL TASK---")
    for i,task in enumerate(tasks,start = 1):
        print(f"{i}. {task.strip()}")
        
    task_num = int(input("Enter the task number to marks as complete: "))
    if "[ ]" in tasks[task_num -1]:
        tasks[task_num -1] = tasks[task_num -1].replace("[ ]","[✓]",1)
        print("Task marked!")
    else:
        print("Task is already marked as complete")
        
    with open("task.txt","w")as f:
        f.writelines(tasks)
        
def delete_task():
    with open("task.txt", "r") as f:
        tasks = f.readlines()
        
    if not tasks:
        print("Task not found.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")

    task_num = int(input("Enter the task number to delete: "))
    deleted_task = tasks.pop(task_num - 1) 
    
    with open("backup.txt","a") as f:
        f.write(deleted_task)

    with open("task.txt", "w") as f:
        f.writelines(tasks)

    print("Task deleted and saved for Recovery!")
    
def edit_tasks():
    with open("task.txt","r") as f:
        tasks = f.readlines()
        
    for i,task in enumerate(tasks,start = 1):
        print(f"{i}.{task.strip()}")
        
    task_num = int(input("Enter the task no. to be edited: "))
    new_task = input("Enter the task description: ")
    new_status = input("Mark as complete? (yes/no): ").strip().lower()

    # Update status based on user input
    if new_status == "yes":
        tasks[task_num - 1] = f"[✓] {new_task}\n"
    else:
        tasks[task_num - 1] = f"[ ] {new_task}\n"
        
    with open("task.txt","w") as f:
        f.writelines(tasks)
        
    print("Task Edited successfully!")
    
def search():
    with open("task.txt","r") as f:
        tasks = f.readlines()
        
    if not tasks:
        print("No tasks found in the file.")
        return
    
    print("\n*****Choose a serach fillter*****")
    print("1.Seach by Keyword")
    print("2.Search by Priority")
    print("3.Search by Category")
    print("4.Search by Due Date")
    
    choice = input("Enter your choice: ")
    found = False
    
    if choice == "1":
        search_task = input("Enter the keyword: ").strip().lower()
        for i,task in enumerate(tasks,start=1):
            if search_task.lower() in task.lower():
                print(f"{i}. {task.strip()}")
                found = True
                
    elif choice == "2":
        priority = input("Enter Priority (High/Medium/Low): ").strip().lower()
        for i,task in enumerate(tasks,start=1):
            if f"Priority: {priority}" in task:
                print(f"{i}. {task.strip()}")
                found = True
                
    elif choice == "3":
        category = input("Enter Category (Work/Personal/Other): ").strip().lower()
        for i,task in enumerate(tasks,start=1):
            if f"Category: {category}" in task:
                print(f"{i}. {task.strip()}")
                found = True
                
    elif choice == "4":
        due_date = input("Enter Due Date (DD/MM/YY): ").strip()
        for i,task in enumerate(tasks,start=1):
            if f"Due Date: {due_date}" in task:
                print(f"{i}. {task.strip()}")
                found = True
    else:
        print("Invalid choice!")
        return
            
    if not found:
        print("No Matching tasks found.")
        
def sort_tasks():
    with open("task.txt", "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("No tasks to sort!")
        return

    print("\nChoose Sorting Option:")
    print("1. High Priority First")
    print("2. Low Priority First")
    print("3. Closest Due Date First")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        sorted_tasks = sorted(tasks, key=lambda t: ("High" not in t, "Medium" not in t, "Low" not in t))
    elif choice == "2":
        sorted_tasks = sorted(tasks, key=lambda t: ("Low" not in t, "Medium" not in t, "High" not in t))
    elif choice == "3":
        sorted_tasks = sorted(tasks, key=lambda t: t.split("Due: ")[1] if "Due: " in t else "99/99/9999")  # Sorting by due date
    else:
        print("Invalid choice!")
        return

    print("\n----- Sorted Tasks -----")
    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task.strip()}")
    
while True:
    print("\n*****To Do List Menu*****")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. View Incomplete Tasks")
    print("5. View Completed Tasks")
    print("6. Mark the completed Tasks")
    print("7. Edit Tasks")
    print("8. Search Tasks")
    print("9. Sort Tasks")
    print("10. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        incomplete()
    elif choice == "5":
        complete()
    elif choice == "6":
        mark_complete()
    elif choice == "7":
        edit_tasks()
    elif choice == "8":
        search()
    elif choice == "9":
        sort_tasks()
    elif choice == "10":
        break
    else:
        print("Invalid option!")