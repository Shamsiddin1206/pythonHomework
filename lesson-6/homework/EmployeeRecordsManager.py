import os

FILE_NAME = "employees.txt"


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")

    print("Employee record added successfully!")


def view_employees():
    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        print("No employee records found.")
        return

    with open(FILE_NAME, "r") as file:
        print("\nEmployee Records:")
        for line in file:
            print(line.strip())


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            record = line.strip().split(", ")
            if record[0] == emp_id:
                print("Employee Found:", line.strip())
                found = True
                break

    if not found:
        print("Employee not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            record = line.strip().split(", ")
            if record[0] == emp_id:
                print(f"Current Record: {line.strip()}")
                name = input("Enter new Name (leave blank to keep current): ") or record[1]
                position = input("Enter new Position (leave blank to keep current): ") or record[2]
                salary = input("Enter new Salary (leave blank to keep current): ") or record[3]
                updated_lines.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_lines.append(line)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)
        print("Employee record updated successfully!")
    else:
        print("Employee ID not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            record = line.strip().split(", ")
            if record[0] == emp_id:
                print(f"Deleting Record: {line.strip()}")
                found = True
            else:
                updated_lines.append(line)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)
        print("Employee record deleted successfully!")
    else:
        print("Employee ID not found.")


def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Choose an option: ")

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
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
