import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pickle

class Employee:
    def __init__(self, emp_id, name, department, job_title, manager_id, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.manager_id = manager_id
        self.basic_salary = basic_salary

class House:
    def __init__(self, house_id, name, declared_price, house_type, built_up_area, status, selling_price, salesperson_id):
        self.house_id = house_id
        self.name = name
        self.declared_price = declared_price
        self.house_type = house_type
        self.built_up_area = built_up_area
        self.status = status
        self.selling_price = selling_price
        self.salesperson_id = salesperson_id

class RealEstateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BrickCages Real Estate Management System")

        # Create variables to store employee and house data
        self.employees = []
        self.houses = []

        self.root.configure(bg="#24C7DE") 
        # Load existing data from binary files
        self.load_data()

      # Configure a style for modern buttons
        style = ttk.Style()
        style.configure("TButton", padding=(6, 10), relief="flat",width=15,height=5, background="#24DE73", foreground="black")

        # Create buttons for employees and houses
        employee_button = ttk.Button(root, text="Employee", command=self.employee_functions, style="TButton")
        house_button = ttk.Button(root, text="House", command=self.house_functions, style="TButton")

        # Place buttons
        employee_button.place(relx=0.4, rely=0.5, anchor='center')
        house_button.pack(side='right', padx=500, anchor='center')

       
    def load_data(self):
        try:
            with open("employees.dat", "rb") as emp_file:
                self.employees = pickle.load(emp_file)
        except FileNotFoundError:
            pass

        try:
            with open("houses.dat", "rb") as house_file:
                self.houses = pickle.load(house_file)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("employees.dat", "wb") as emp_file:
            pickle.dump(self.employees, emp_file)

        with open("houses.dat", "wb") as house_file:
            pickle.dump(self.houses, house_file)

    def employee_functions(self):
         # Disable the main window
        self.root.withdraw()

        while True:
            choice = self.input_dialog("Choose an action for Employees:\n"
                                       "1. Add Employee\n"
                                       "2. Delete Employee\n"
                                       "3. Modify Employee\n"
                                       "4. Display Employee Details\n"
                                       "5. Exit")
            if choice == "1":
                self.add_employee(self.root)
            elif choice == "2":
                self.delete_employee()
            elif choice == "3":
                self.modify_employee()
            elif choice == "4":
                self.display_employee_details()
            elif choice == "5":
                break
            else:
                self.show_message("Invalid choice. Please enter a valid option.")

       # Re-enable the main window
        self.root.deiconify()
    def house_functions(self):
        # Disable the main window
        self.root.withdraw()

        while True:
            choice = self.input_dialog("Choose an action for Houses:\n"
                                       "1. Add House\n"
                                       "2. Delete House\n"
                                       "3. Modify House\n"
                                       "4. Display House Details\n"
                                       "5. Exit")
            if choice == "1":
                self.add_house(self.root)
            elif choice == "2":
                self.delete_house()
            elif choice == "3":
                self.modify_house()
            elif choice == "4":
                self.display_house_details()
            elif choice == "5":
                break
            else:
                self.show_message("Invalid choice. Please enter a valid option.")

        # Re-enable the main window
        self.root.deiconify()

    def add_employee(self,parent_window):
        # Create a new window for employee details
        employee_window = tk.Toplevel(parent_window)
        employee_window.title("Employee Details")

        # Configure background color
        employee_window.configure(bg="#24C7DE")

        # Add Entry widgets for employee details
        tk.Label(employee_window, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        tk.Label(employee_window, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        tk.Label(employee_window, text="Department:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        tk.Label(employee_window, text="Job Title:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        tk.Label(employee_window, text="Manager ID:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        tk.Label(employee_window, text="Basic Salary:").grid(row=5, column=0, padx=10, pady=5, sticky='e')

        entry_emp_id = tk.Entry(employee_window)
        entry_emp_id.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        entry_name = tk.Entry(employee_window)
        entry_name.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        entry_department = tk.Entry(employee_window)
        entry_department.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        entry_job_title = tk.Entry(employee_window)
        entry_job_title.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        entry_manager_id = tk.Entry(employee_window)
        entry_manager_id.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        entry_basic_salary = tk.Entry(employee_window)
        entry_basic_salary.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        # Create a button to save the employee details
        save_button = tk.Button(employee_window, text="Save", command=lambda: self.save_employee_details(
            entry_emp_id.get(), entry_name.get(), entry_department.get(), entry_job_title.get(),
            entry_manager_id.get(), entry_basic_salary.get(), employee_window
        ))
        save_button.grid(row=6, column=0, columnspan=2,pady=10)
        # Center the window
        self.center_window(employee_window)


       


    def save_employee_details(self, emp_id, name, department, job_title, manager_id, basic_salary, window):
        # Validate input (add your validation logic here)
        if not emp_id or not name or not department or not job_title or not manager_id or not basic_salary:
            self.show_message("Please enter all employee details.")
            return

        # Create a new employee and add it to the list
        new_employee = Employee(emp_id, name, department, job_title, manager_id, basic_salary)
        self.employees.append(new_employee)
        self.save_data()
        self.show_message("Employee added successfully!")

        # Close the employee details window
        window.destroy()

    def delete_employee(self):
        emp_id = self.input_dialog("Enter employee ID to delete:")
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                self.save_data()
                self.show_message(f"Employee with ID {emp_id} deleted successfully!")
                return
        self.show_message(f"Employee with ID {emp_id} not found.")

    def modify_employee(self):
        emp_id = self.input_dialog("Enter employee ID to modify:")
        for employee in self.employees:
            if employee.emp_id == emp_id:
                # Disable the modify employee window
                self.root.withdraw()

                # Create a new window for modifying employee details
                modify_window = tk.Toplevel(self.root)
                modify_window.title("Modify Employee Details")

                # Add Entry widgets for the selected part of the employee details
                tk.Label(modify_window, text="Modify selected part of employee details:").grid(row=0, column=0, columnspan=2)
                tk.Label(modify_window, text="1. Name").grid(row=1, column=0)
                tk.Label(modify_window, text="2. Department").grid(row=2, column=0)
                tk.Label(modify_window, text="3. Job Title").grid(row=3, column=0)
                tk.Label(modify_window, text="4. Manager ID").grid(row=4, column=0)
                tk.Label(modify_window, text="5. Basic Salary").grid(row=5, column=0)

                modify_choice = self.input_dialog("Enter your choice:")
                if modify_choice == "1":
                    employee.name = self.input_dialog("Enter new employee name:")
                elif modify_choice == "2":
                    employee.department = self.input_dialog("Enter new employee department:")
                elif modify_choice == "3":
                    employee.job_title = self.input_dialog("Enter new employee job title:")
                elif modify_choice == "4":
                    employee.manager_id = self.input_dialog("Enter new manager ID:")
                elif modify_choice == "5":
                    employee.basic_salary = self.input_dialog("Enter new employee basic salary:")
                else:
                    self.show_message("Invalid choice. Please enter a valid option.")

                self.save_data()
                self.show_message(f"Employee with ID {emp_id} modified successfully!")

                # Close the modify employee window
                modify_window.destroy()

                # Re-enable the main window
                self.root.deiconify()
                return
        self.show_message(f"Employee with ID {emp_id} not found.")

    def display_employee_details(self):
        emp_id = self.input_dialog("Enter employee ID to display details:")
        for employee in self.employees:
            if employee.emp_id == emp_id:
                details = (f"\nEmployee Details\n"
                           f"ID: {employee.emp_id}\n"
                           f"Name: {employee.name}\n"
                           f"Department: {employee.department}\n"
                           f"Job Title: {employee.job_title}\n"
                           f"Manager ID: {employee.manager_id}\n"
                           f"Basic Salary: {employee.basic_salary}\n")
                self.show_message(details)
                return
            self.show_message(f"Employee with ID {emp_id} not found.")

    
    def add_house(self, parent_window):
        # Create a new window for house details
        house_window = tk.Toplevel(parent_window)
        house_window.title("House Details")

        # Configure background color
        house_window.configure(bg="#24C7DE")

        # Add Entry widgets for house details
        tk.Label(house_window, text="House ID:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="Declared Price:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="House Type:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="Built-up Area:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="Status:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="Selling Price:").grid(row=6, column=0, padx=10, pady=5, sticky='e')
        tk.Label(house_window, text="Salesperson ID:").grid(row=7, column=0, padx=10, pady=5, sticky='e')

        entry_house_id = tk.Entry(house_window)
        entry_house_id.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        entry_name = tk.Entry(house_window)
        entry_name.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        entry_declared_price = tk.Entry(house_window)
        entry_declared_price.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        entry_house_type = tk.Entry(house_window)
        entry_house_type.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        entry_built_up_area = tk.Entry(house_window)
        entry_built_up_area.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        entry_status = tk.Entry(house_window)
        entry_status.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        entry_selling_price = tk.Entry(house_window)
        entry_selling_price.grid(row=6, column=1, padx=10, pady=5, sticky='w')
        entry_salesperson_id = tk.Entry(house_window)
        entry_salesperson_id.grid(row=7, column=1, padx=10, pady=5, sticky='w')

        # Create a button to save the house details
        save_button = tk.Button(house_window, text="Save", command=lambda: self.save_house_details(
        entry_house_id.get(), entry_name.get(), entry_declared_price.get(), entry_house_type.get(),
        entry_built_up_area.get(), entry_status.get(), entry_selling_price.get(), entry_salesperson_id.get(), house_window
        ))
        save_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Center the window
        self.center_window(house_window)

    def save_house_details(self, house_id, name, declared_price, house_type, built_up_area, status, selling_price, salesperson_id, window):
       # Validate input (add your validation logic here)
       if not house_id or not name or not declared_price or not house_type or not built_up_area or not status or not selling_price or not salesperson_id:
          self.show_message("Please enter all house details.")
          return

       # Create a new house and add it to the list
       new_house = House(house_id, name, declared_price, house_type, built_up_area, status, selling_price, salesperson_id)
       self.houses.append(new_house)
       self.save_data()
       self.show_message("House added successfully!")

       # Close the house details window
       window.destroy()

    def delete_house(self):
        house_id = self.input_dialog("Enter house ID to delete:")
        for house in self.houses:
            if house.house_id == house_id:
                self.houses.remove(house)
                self.save_data()
                self.show_message(f"House with ID {house_id} deleted successfully!")
                return
        self.show_message(f"House with ID {house_id} not found.")

    def modify_house(self):
        house_id = self.input_dialog("Enter house ID to modify:")
        for house in self.houses:
            if house.house_id == house_id:
                house.name = self.input_dialog("Enter new house name:")
                house.declared_price = self.input_dialog("Enter new declared price:")
                house.house_type = self.input_dialog("Enter new house type:")
                house.built_up_area = self.input_dialog("Enter new built-up area:")
                house.status = self.input_dialog("Enter new status:")
                house.selling_price = self.input_dialog("Enter new selling price:")
                house.salesperson_id = self.input_dialog("Enter new salesperson ID:")
                self.save_data()
                self.show_message(f"House with ID {house_id} modified successfully!")
                return
        self.show_message(f"House with ID {house_id} not found.")

    def display_house_details(self):
        house_id = self.input_dialog("Enter house ID to display details:")
        for house in self.houses:
            if house.house_id == house_id:
                details = (f"\nHouse Details\n"
                           f"ID: {house.house_id}\n"
                           f"Name: {house.name}\n"
                           f"Declared Price: {house.declared_price}\n"
                           f"Type: {house.house_type}\n"
                           f"Built-up Area: {house.built_up_area}\n"
                           f"Status: {house.status}\n"
                           f"Selling Price: {house.selling_price}\n"
                           f"Salesperson ID: {house.salesperson_id}\n")
                self.show_message(details)
                return
        self.show_message(f"House with ID {house_id} not found.")

    def input_dialog(self, prompt):
        return simpledialog.askstring("Input", prompt)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = RealEstateApp(root)
    root.mainloop()
