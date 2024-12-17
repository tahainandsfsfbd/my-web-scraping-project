import time
import random

# TODOLİST

todolist = []

#add a task
def add_task(task):
    print("Task is adding...")
    time.sleep(1)
    todolist.append(task)
    print("Task has added")

#delete a task
def delete_task(task):
    print("Task is deleting...")
    time.sleep(1)
    todolist.remove(task)
    print("Task has deleted.")

#show all tasks
def show_tasks():
    """sayac = 1
    for i in todolist:
        print("")
        print(sayac,":",i.upper())
        sayac += 1
        print("")"""
    if len(todolist) == 0:
        print("There is no task.Please add a task.")
        print("")
    
    else:
        sayac = 1 
        for i in todolist:
            print("")
            print(sayac,":",i.upper())
            sayac += 1
        print("")

#task has been completed
def complete_task(task):
    print(task,"has been completed.")
    todolist.remove(task)

#welcome to todolist program
print("""
    Hello! Welcome to todolist!
    
    Add a task: 1 
    Delete a task: 2 
    Show tasks: 3 
    Complete a task: 4
    Quit: 5
                
          """)


while True:
    
    process = input("Enter a process: ")

    if process == "1":
        """task = input("Add a task: ").lower().strip()
        add_task(task)"""
        while True:
            print("Enter 'q' to quit...")
            task = input("Add a task: ")
            if task == "q":
                break
            else:
                add_task(task)
    
    elif process == "2" :
        task = input("Delete a task: ").lower().strip()
        if task in todolist:
            delete_task(task)
    elif process == "3" :
        show_tasks()
    
    elif process == "4":
        task = input("Complete a task: ")
        complete_task(task)

    elif process == "5" :
        break
    else:
        print("Invalid process!")


def start_study():
    counter = 1
    for i in todolist:
        print(counter,":",random.randint(30,40),"minutes for",i)
        counter += 1

print("")
start_study()
print("")







    
   