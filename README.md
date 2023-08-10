# Students Database Manager

This project is a simple Python program to manage a student database using SQLite3. It performs basic CRUD operations and demonstrates efficient database handling with Python.

## Features
1. Creates a new SQLite3 table named `python_programming`.
2. Inserts predefined rows of student data into the table.
3. Displays data with formatted tables.
4. Performs select operations with conditions.
5. Updates specific records based on conditions.
6. Deletes specific rows based on conditions.
7. Has proper exception handling for database operations.

## Dependencies
- Python
- SQLite3 (comes bundled with Python's standard library)
- `tabulate` package for table formatting. Install via pip:
  ```bash
  pip install tabulate
  ```

## Usage
1. Ensure that Python is installed.
2. Clone the repository:
   ```bash
   git clone (https://github.com/cipobt/sqlite_dtbase)
   ```
3. Navigate to the repository's directory:
   ```bash
   cd sqlite_dtbase
   ```
4. Run the program:
   ```bash
   python database_manip.py
   ```

## Notes
- The database path is constructed using the `os` module to adapt to different environments and avoid path-related issues.
- A helper function named `print_db` is used to print the database contents for various queries.
- Proper exception handling has been implemented to rollback any changes in case of a database operation failure.

## Contributing
Contributions, issues, and feature requests are welcome!

## License
This project is [MIT] licensed.

## Acknowledgements
- Thanks to SQLite3 for a robust and lightweight database management system.
- Thanks to the `tabulate` package for beautiful table formatting in the terminal.
