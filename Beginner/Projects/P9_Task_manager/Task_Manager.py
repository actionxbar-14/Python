






def tasks():
    tasks = []
    task_input =  int(input("Enter How many task:"))
    for i in range(1,task_input+1):
        task_name = input(f"Enter task {i}:")
        tasks.append(task_name)

    print(f"Today total tasks are: {tasks}")


    while True:
        operation = int(input("Enter 1 --> add \n Enter 2 --> update \n Enter 3 --> delete \n Enter 4 --> View Task \n Enter 5 --> Terminate task manager" ))

        if operation == 1:
            add_task = input("Enter the task you want to add")
            tasks.append(add_task)
            print(f"task {add_task} added succusfully, Now total tasks are: {tasks}")



        elif operation == 2:
            updated_task = input("Enter the task you want to update:")
            if updated_task in tasks:
                new_task = input("Enter new task:")
                task_index = tasks.index(updated_task)
                tasks[task_index] = new_task
                print(f"tasks updated succusfully")


        elif operation == 3:
            del_val = input("Enter the task you want to delete:")
            if del_val in tasks:
                del_task_index = tasks.index(del_val)
                del tasks[del_task_index]


        elif operation == 4:
            print(f"your today tasks are : {tasks}")


        elif operation == 5:
            print("terminating the task manager, thanks for using this task manager")

            
        else:
            print("Invalid input")

   
       

tasks()

       
