import os.path

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w"): pass

    def add(self, new):
        state = True
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(new.employee_id) + ","):
                    state = False
                    break

        if state:
            with open(self.FILE_NAME, "a") as file:
                file.write(str(new) + "\n")
            print("Successfully added!")
        else:
            print("Employee with the same ID already exists!")

    def delete(self, e_id):
        state = False
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for record in records:
                if not record.startswith(str(e_id) + ","):
                    file.write(record)
                else:
                    state = True

        if state:
            print("Deleted successfully!")
        else:
            print("No data found!")

    def view(self):
        with open(self.FILE_NAME, "r") as file:
            data = file.readlines()

        if data:
            print("Employee Records:")
            for record in data:
                print(record.strip())
        else:
            print("No data found")

    def search(self, e_id):
        with open(self.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(str(e_id) + ","):
                    print("Employee Found:")
                    print(record.strip())
                    return
        print("Employee not found!")

    def update(self, e_id, name=None, position=None, salary=None):
        state = False
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(", ")
                if data[0] == str(e_id):
                    if name:
                        data[1] = name
                    if position:
                        data[2] = position
                    if salary:
                        data[3] = str(salary)
                    record = ", ".join(data) + "\n"
                    state = True
                file.write(record)

        if state:
            print("Employee data successfully updated!")
        else:
            print("Employee not found!")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                e_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")

                if not e_id.isdigit() or not salary.isdigit():
                    print("Invalid input! Employee ID and Salary must be numbers.")
                    continue

                self.add(Employee(int(e_id), name, position, int(salary)))

            elif choice == "2":
                self.view()

            elif choice == "3":
                e_id = input("Enter Employee ID to search: ")
                if not e_id.isdigit():
                    print("Invalid input! Employee ID must be a number.")
                    continue
                self.search(int(e_id))

            elif choice == "4":
                e_id = input("Enter Employee ID to update: ")
                if not e_id.isdigit():
                    print("Invalid input! Employee ID must be a number.")
                    continue

                name = input("Enter new name (press Enter to skip): ") or None
                position = input("Enter new position (press Enter to skip): ") or None
                salary = input("Enter new salary (press Enter to skip): ")
                salary = int(salary) if salary.isdigit() else None

                self.update(int(e_id), name, position, salary)

            elif choice == "5":
                e_id = input("Enter Employee ID to delete: ")
                if not e_id.isdigit():
                    print("Invalid input! Employee ID must be a number.")
                    continue
                self.delete(int(e_id))

            elif choice == "6":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
