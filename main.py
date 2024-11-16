from functions import (user_status, user_check, add_user, my_tasks, add_task, change_status,
                       show_task, check_incomplete, delete_task)

user_name = input("Enter Your Username: ")

if user_status(user_name) == 0:
    print("You Aren't Registered")
    new_user = input("Enter Your Username: ")

    correct_name = False
    while correct_name is False:
        if len(new_user) <= 3:
            print("Username Is Too Short ")
            new_user = input("Enter The New Username: ")
        elif len(new_user) >= 20:
            print("Username Is Too Long ")
            new_user = input("Enter The New Username: ")
        else:
            correct_name = True

    created = False
    while created is False:

        if user_check(new_user) == 0:
            add_user(new_user)
            created = True
        else:
            print(f"Username {new_user} is taken")
            new_user = input("Enter Different Username: ")

else:
    choice = int(input(
        """
1 --> Change Task Status
2 --> Add Tasks
3 --> Delete Task
4 --> My Tasks
\n"""))
    match choice:
        case 1:
            tasks = my_tasks(username=user_name)
            if tasks:
                in_task = check_incomplete(user_name)
                if in_task:
                    show_task(in_task)
                    task_id = int(input("Enter Task ID: "))
                    change_status(task_id=task_id)
                    tasks = my_tasks(username=user_name)
                    show_task(tasks)
                else:
                    print("All Tasks Are Completed ")
            else:
                print("You Don't Have Any Tasks !")
        case 2:
            task = input("Enter New Task Name: ")
            due = input("Enter Due Date In This Format (YY-MM-DD): ")
            correct_spell = False
            priority = input("Enter Priority Level: ").lower()
            while correct_spell is False:
                if priority in ["low", "medium", "high"]:
                    correct_spell = True
                else:
                    priority = input("Spell Correctly: LOW, MEDIUM, HIGH \n")
            add_task(username=user_name, task=task, due=due, priority=priority)
            tasks = my_tasks(username=user_name)
            if tasks:
                show_task(tasks)
            else:
                print("No Tasks Yet")
        case 3:
            tasks = my_tasks(user_name)
            if tasks:
                show_task(tasks)
                print()
                task_id = int(input("Enter The Task Id To Delete: "))
                delete_task(task_id)
                tasks = my_tasks(username=user_name)
                show_task(tasks)
            else:
                print("You Have No Tasks !")
        case 4:
            tasks = my_tasks(user_name)
            if tasks:
                show_task(tasks)
                print()
            else:
                print("You Have No Tasks !")
