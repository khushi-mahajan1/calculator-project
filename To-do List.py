FILE_NAME="task.txt"
def load_tasks():
    try:
        with open(FILE_NAME,"r") as file:
            return [task.strip() for task in file .readlines()]
    except FileNotFoundError:
        return[]
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        for task in tasks:
            file.write(task+"\n")
tasks=load_tasks()
while True:
    print("\n-----To-DO LIST APP----") 
    print("1.View task")
    print("2.Add task") 
    print("3.Delete task")
    print("4.Exit")
    choice=input("Enter the choice:") 
    if choice=="1":
        if not tasks:
            print("No tasks Available.")
        else:
            print("\nYour Tasks:")    
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}") 
    elif choice=="2":
        task=input("Enter task:")
        tasks.append(task)
        save_tasks(task)
        print("Task Added successfully!")
    elif choice=="3":
        if not tasks:
            print("No need to delete.")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            try:
                num=int(input("Enter the task number to delete:"))
                if 1<=num <=len(tasks):
                    removed=tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"'{removed}' deleted successfully !")
                else:
                    print("Invalid task number:") 
            except ValueError:
                print("please enter the valid number.")
    elif choice=="4":
        print("Thank you for using the TO-DO list App !")
        break
    else:
        print("Invalid choice. please try again.")         