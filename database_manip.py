import sqlite3
import os
from tabulate import tabulate

db_path = os.path.join(os.getcwd(), 'students_db')  # I had some issues accessing the database, so after some
db = sqlite3.connect(db_path)                       # research, I decided to use the os module to construct
cursor = db.cursor()                                # the path to the current working directory


# I've created a function to print the database that accepts an optional query and query parameters,
# allowing me to use the same function for different queries throughout the program
def print_db(query=None, params=None):
    headers = ['ID', 'NAME', 'GRADE']
    if query is None:
        query = '''SELECT id, name, grade FROM python_programming'''
    cursor.execute(query, params if params else ())
    rows = cursor.fetchall()
    print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))


try:
    # Creating the table python_programming
    cursor.execute('''
        CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
    ''')
    db.commit()  # Commit the changes to the database

    # Inserting the following new rows into the python_programming table
    students_grades = [(55, 'Carl Davis', 61),
                    (66, 'Dennis Fredrickson', 88),
                    (77, 'Jane Richards', 78),
                    (12, 'Peyton Sawyer', 45),
                    (2, 'Lucas Brooke', 99)]

    cursor.executemany(''' INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''', students_grades)

    db.commit()

    print("\nTable python_programming:")
    print_db()  # Calling the function to display the database contents

    # Selecting all records with a grade between 60 and 80
    print('\nSELECT all students with grades between 60 and 80:')
    query = '''SELECT id, name, grade FROM python_programming  WHERE grade BETWEEN 60 AND 80'''
    print_db(query)

    # Changing Carl Davis’s grade to 65
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ? ''', (65, 'Carl Davis'))
    db.commit()
    print('\nCarl Davis grade has been changed')
    query = '''SELECT id, name, grade FROM python_programming WHERE name = ? '''
    params = ('Carl Davis',)
    print_db(query, params)  # Calling the function to display the Carl Davis' row

    # Deleting Dennis Fredrickson’s row
    cursor.execute('''DELETE FROM python_programming WHERE name = ? ''', ('Dennis Fredrickson',))
    db.commit()

    print("\nNew table after deleting Dennis Fredrickson’s row")
    print_db()

    # Changing the grade of all people with an id below than 55
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < 55 ''', (100,))
    db.commit()  # Commit the changes to the database

    print("\nNew table after changing grades of all students with an id below 55")
    print_db()

# To catch any exception derived from the base Exception class, use db.rollback() to undo any changes made during the transaction, 
# and raise the caught exception e to allow the user to see the specific error message and handle it accordingly outside the except
# block, if necessary.
except Exception as e:
    db.rollback()
    raise e

finally:
    db.close()
