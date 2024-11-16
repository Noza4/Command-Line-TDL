import sqlite3
import datetime

import tabulate

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()


def user_status(name):

    cursor.execute('''
        SELECT * FROM Users
        WHERE Username = ?
        ''', (name,)
                       )

    user = cursor.fetchone()

    if user is not None:
        return 1
    else:
        return 0


def user_check(username):

    cursor.execute('''
    SELECT * FROM Users
    WHERE Username = ?
    ''', (username,)
                   )

    name = cursor.fetchall()

    return len(name)


def add_user(username):

    cursor.execute('''
    INSERT INTO Users (Username)
    VALUES (?)
    ''', (username,)
                   )
    conn.commit()

    print(f"User {username} Registered Successfully")


def my_tasks(username):

    cursor.execute('''
    SELECT * FROM TaskTable 
    WHERE User_id = (
    SELECT Id FROM Users WHERE Username = ?)
    ''', (username,))

    tasks = cursor.fetchall()

    return tasks


def add_task(username, task, date=datetime.date.today(), due="", priority='low'):

    cursor.execute('''
    SELECT Id FROM Users
    WHERE Username = ?
    ''', (username,))

    user_id = cursor.fetchone()[0]

    cursor.execute('''
    INSERT INTO TaskTable (User_id, Task, AddDate, DueDate, Priority)
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, task, date, due, priority))

    print(f"Task Added successfully\n")

    conn.commit()


def change_status(task_id):

    cursor.execute('''
    UPDATE TaskTable
    SET status = "Complete"
    WHERE Id = ?
    ''', (task_id,))

    conn.commit()
    print("Status Changed Successfully")
    print()


def show_task(tasks):
    headers = ['ID', "User_ID", "Task", "AddDate", "DueDate", "Priority", "Status"]
    print(tabulate.tabulate(tasks, headers, tablefmt='simple'))


def check_incomplete(user):

    cursor.execute('''
    SELECT * FROM TaskTable
    WHERE User_id = (
    SELECT Id FROM Users WHERE Username = ?
    ) AND status = "Incomplete"
    ''', (user,))

    task = cursor.fetchall()

    return task


def delete_task(task_id):

    cursor.execute('''
    DELETE FROM TaskTable
    WHERE Id = ?
    ''', (task_id,))

    conn.commit()

    print("Task Deleted Successfully ")
