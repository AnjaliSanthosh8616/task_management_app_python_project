def task():
    tasks=[]#empty list
    print("___WELCOME TO THE TASK MANAGEMENT APP__")
    total_task=int(input("Enter the number of tasks you want to add:")) 

    for i in range(total_task+1):
        task_name=input(f"Enter the task {i}=")
        tasks.append(task_name)

    print(f"Today's tasks are \n {tasks}")

    while True:
        operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        if operation==1:
            add=input("Enter the task you want to add:")
            tasks.append(add)
            print(f"Task {add} has been successfully added....")

        elif operation==2:
            update_val=input("Enter the task name you want to update")
            if update_val in tasks:
                up=input("Enter new Task:")
                ind=tasks.index(update_val)
                tasks[ind]=up
                print(f"Task {update_val} has been updated successfully....")

        elif operation==3:
            del_val=input("Enter the task you want to delete:")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been successfully removed...")

        elif operation==4:
            print(f"Total tasks are={tasks}")

        elif operation==5:
            print("Closing the program.........")
            break
            
        else:
            print("Invalid entry")

task()