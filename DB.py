import sqlite3

connection = sqlite3.connect('todo.db')  # Connect to the Database or Create new connection

cursor = connection.cursor()  # Create Cursor object that makes changes in the db

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL UNIQUE
            )
    ''')  # Create a table script

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS TaskTable (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            User_id INTEGER NOT NULL,
            Task TEXT NOT NULL,
            AddDate TEXT NOT NULL,
            DueDate TEXT,
            Priority TEXT, 
            status TEXT DEFAULT 'Incomplete',
            FOREIGN KEY (User_id) REFERENCES Users(Id)
        )
    '''
)  # Create a second table script with on to many connection in it

connection.commit()  # Commit to save changes
connection.close()  # Close not to take any more memory | also for security

