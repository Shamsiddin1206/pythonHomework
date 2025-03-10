import os

EMPLOYEE_FILE = "employees.txt"

def ensure_file_exists():
    if not os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "w", encoding="utf-8"):
            pass  # Create an empty file

def load_employees():
    employees = []
    with open(EMPLOYEE_FILE, "r", encoding="utf-8") as file:
        for line in file:
            employees.append(line.strip().split(", "))
    return employees

def save_employees(employees):
    with open(EMPLOYEE_FILE, "w", encoding="utf-8") as file:
        for emp in employees:
            file.write(", ".join(emp) + "\n")

def validate_numeric_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Invalid input! Please enter a numeric value.")

def add_employee():
    employees = load_employees()
    emp_id = validate_numeric_input("Enter Employee ID: ")
    name = input("Enter Name: ").strip()
    position = input("Enter Position: ").strip()
    salary = validate_numeric_input("Enter Salary: ")
    employees.append([emp_id, name, position, salary])
    save_employees(employees)
    print("Employee record added successfully!\n")

def view_employees():
    employees = load_employees()
    if not employees:
        print("No employee records found.\n")
        return
    print("\nEmployee Records:")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}")
    print()

def search_employee():
    employees = load_employees()
    emp_id = validate_numeric_input("Enter Employee ID to search: ")
    for emp in employees:
        if emp[0] == emp_id:
            print(f"Found: ID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}\n")
            return
    print("Employee not found.\n")

def update_employee():
    employees = load_employees()
    emp_id = validate_numeric_input("Enter Employee ID to update: ")
    for emp in employees:
        if emp[0] == emp_id:
            emp[1] = input("Enter new name (leave blank to keep current): ") or emp[1]
            emp[2] = input("Enter new position (leave blank to keep current): ") or emp[2]
            new_salary = input("Enter new salary (leave blank to keep current): ").strip()
            emp[3] = new_salary if new_salary.isdigit() else emp[3]
            save_employees(employees)
            print("Employee record updated successfully!\n")
            return
    print("Employee not found.\n")

def delete_employee():
    employees = load_employees()
    emp_id = validate_numeric_input("Enter Employee ID to delete: ")
    new_employees = [emp for emp in employees if emp[0] != emp_id]
    if len(new_employees) == len(employees):
        print("Employee not found.\n")
    else:
        save_employees(new_employees)
        print("Employee record deleted successfully!\n")

def main():
    ensure_file_exists()
    while True:
        print("""
        Employee Records Manager
        1. Add new employee record
        2. View all employee records
        3. Search for an employee by Employee ID
        4. Update an employee's information
        5. Delete an employee record
        6. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
