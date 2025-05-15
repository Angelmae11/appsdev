import customtkinter as ctk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import csv
import datetime
import os


# ------------------ Login and Registration Form ------------------ #
class LoginForm(ctk.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.title('Register / Log In')
        self.geometry('500x300')
        self.on_login_success = on_login_success

        self.label = ctk.CTkLabel(self, text='Register / Log In', font=('Arial', 20))
        self.label.pack(pady=10)

        self.entry_username = ctk.CTkEntry(self, placeholder_text='Username')
        self.entry_username.pack(pady=5)

        self.entry_password = ctk.CTkEntry(self, placeholder_text='Password', show='*')
        self.entry_password.pack(pady=5)

        self.register_button = ctk.CTkButton(self, text='Register', command=self.register_user)
        self.register_button.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text='Log In', command=self.login_user)
        self.login_button.pack(pady=10)

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror('Error', 'All fields are required.')
            return

        # Create users.csv if it doesn't exist
        file_exists = os.path.isfile('users.csv')

        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # Write header if file is new
            if not file_exists:
                writer.writerow(['username', 'password'])
            writer.writerow([username, password])
            messagebox.showinfo('Success', 'Registration Successful!')

        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

    def login_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        try:
            with open('users.csv', 'r') as file:
                reader = csv.reader(file)
                # Skip header row if it exists
                next(reader, None)
                for row in reader:
                    if len(row) >= 2 and row[0] == username and row[1] == password:
                        messagebox.showinfo('Success', 'Login Successful!')
                        self.destroy()
                        self.on_login_success()
                        return
                messagebox.showerror('Error', 'Invalid Credentials.')
        except FileNotFoundError:
            messagebox.showerror('Error', 'No registered users found.')


# ------------------ Pet Adoption Form ------------------ #
class PetAdoptionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pet Adoption")
        self.geometry("800x600")
        self.adoption_data = []
        self.selected_index = None

        self.animal_breeds = {
            "Dog": ["Labrador", "Golden Retriever", "Poodle", "Bulldog", "Beagle"],
            "Cat": ["Persian", "Siamese", "Maine Coon", "Bengal", "Sphynx"],
            "Bird": ["Parrot", "Canary", "Finch", "Cockatiel"],
            "Other": ["Other"]
        }

        self.setup_ui()
        self.load_from_csv()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Make the treeview expandable

        # Main input frame
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.grid(row=0, column=0, padx=30, pady=20, sticky="ew")

        # Configure columns in the input frame
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)
        self.input_frame.grid_columnconfigure(2, weight=1)
        self.input_frame.grid_columnconfigure(3, weight=1)

        # Fields with improved padding and alignment
        self.first_name_entry = self.create_labeled_entry("First Name:", 0, 0)
        self.last_name_entry = self.create_labeled_entry("Last Name:", 0, 2)  # Fixed: placed in column 2
        self.pet_name_entry = self.create_labeled_entry("Pet Name:", 1, 0)

        # Animal type combobox
        self.animal_type_label = ctk.CTkLabel(self.input_frame, text="Type of Animal:")
        self.animal_type_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.animal_type_menu = ctk.CTkComboBox(self.input_frame, values=["Dog", "Cat", "Bird", "Other"])
        self.animal_type_menu.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
        self.animal_type_menu.set("Dog")  # Default value

        # Configure event to update breed options
        self.animal_type_menu.configure(command=self.update_breed_options)

        # Breed combobox
        self.breed_label = ctk.CTkLabel(self.input_frame, text="Type of Breed:")
        self.breed_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.breed_entry = ctk.CTkComboBox(self.input_frame, values=self.animal_breeds["Dog"])  # Default to Dog breeds
        self.breed_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Date entry
        self.date_label = ctk.CTkLabel(self.input_frame, text="Adoption Date:")
        self.date_label.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.adoption_date_entry = DateEntry(self.input_frame, date_pattern='yyyy-mm-dd')
        self.adoption_date_entry.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        # Insert button
        self.insert_button = ctk.CTkButton(self.input_frame, text="Insert Info", command=self.insert_info)
        self.insert_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Treeview for displaying data
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(self.tree_frame,
                                 columns=("First Name", "Last Name", "Pet Name", "Animal Type", "Breed Type",
                                          "Adoption Date"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        # Add scrollbar to treeview
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(expand=True, fill="both")

        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Buttons for saving, editing, and deleting
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, padx=30, pady=10, sticky="ew")

        self.save_button = ctk.CTkButton(self.button_frame, text="Save to CSV", command=self.save_to_csv)
        self.save_button.pack(side="left", expand=True, fill="x", padx=10)

        self.edit_button = ctk.CTkButton(self.button_frame, text="Edit Info", command=self.edit_info)
        self.edit_button.pack(side="left", expand=True, fill="x", padx=10)

        self.delete_button = ctk.CTkButton(self.button_frame, text="Delete Info", command=self.delete_info)
        self.delete_button.pack(side="right", expand=True, fill="x", padx=10)

        # Initialize breed options for default animal type
        self.update_breed_options("Dog")

    def create_labeled_entry(self, label_text, row, column):
        label = ctk.CTkLabel(self.input_frame, text=label_text)
        label.grid(row=row, column=column, padx=10, pady=10, sticky="w")
        entry = ctk.CTkEntry(self.input_frame)
        entry.grid(row=row, column=column + 1, padx=10, pady=10, sticky="ew")
        return entry

    def update_breed_options(self, selection):
        # This will be called when the animal type combobox changes
        if selection in self.animal_breeds:
            self.breed_entry.configure(values=self.animal_breeds[selection])
            self.breed_entry.set("")  # Clear any previous selection

    def on_tree_select(self, event):
        # This will be called when a row in the treeview is selected
        self.selected_index = None
        selected = self.tree.selection()
        if selected:
            self.selected_index = self.tree.index(selected[0])

    def insert_info(self):
        data = self.get_form_data()
        if not self.validate_data(data):
            return

        if self.selected_index is None:
            self.adoption_data.append(data)
        else:
            self.adoption_data[self.selected_index] = data
            self.selected_index = None
            self.insert_button.configure(text="Insert Info")

        self.update_table()
        self.save_to_csv()
        self.clear_form()

    def edit_info(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to edit.")
            return

        index = self.tree.index(selected[0])
        record = self.adoption_data[index]

        if len(record) < 6:  # Ensure record has all required fields
            messagebox.showerror("Error", "Invalid record format")
            return

        self.first_name_entry.delete(0, 'end')
        self.first_name_entry.insert(0, record[0])

        self.last_name_entry.delete(0, 'end')
        self.last_name_entry.insert(0, record[1])

        self.pet_name_entry.delete(0, 'end')
        self.pet_name_entry.insert(0, record[2])

        self.animal_type_menu.set(record[3])
        self.update_breed_options(record[3])  # Update breed options based on animal type
        self.breed_entry.set(record[4])

        try:
            date_obj = datetime.datetime.strptime(record[5], '%Y-%m-%d').date()
            self.adoption_date_entry.set_date(date_obj)
        except (ValueError, TypeError):
            # Handle invalid date formats
            self.adoption_date_entry.set_date(datetime.date.today())

        self.selected_index = index
        self.insert_button.configure(text="Update Info")

    def delete_info(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
            if confirmation:
                del self.adoption_data[index]
                self.update_table()
                self.save_to_csv()
        else:
            messagebox.showerror("Error", "Select a record to delete.")

    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        for record in self.adoption_data:
            self.tree.insert("", "end", values=record)

    def clear_form(self):
        for entry in [self.first_name_entry, self.last_name_entry, self.pet_name_entry]:
            entry.delete(0, 'end')
        self.animal_type_menu.set("Dog")
        self.update_breed_options("Dog")
        self.breed_entry.set("")
        self.adoption_date_entry.set_date(datetime.date.today())
        self.selected_index = None

    def get_form_data(self):
        return (
            self.first_name_entry.get().strip(),
            self.last_name_entry.get().strip(),
            self.pet_name_entry.get().strip(),
            self.animal_type_menu.get().strip(),
            self.breed_entry.get().strip(),
            self.adoption_date_entry.get_date().strftime('%Y-%m-%d')
        )

    def validate_data(self, data):
        if not all(data):
            messagebox.showerror("Error", "All fields are required.")
            return False

        try:
            datetime.datetime.strptime(data[5], '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Date must be in YYYY-MM-DD format.")
            return False

        # Modified validation to allow for hyphenated names
        first_name = data[0].replace('-', '')
        last_name = data[1].replace('-', '')

        if not first_name.isalpha() or not last_name.isalpha():
            messagebox.showerror("Error", "First and last names must only contain letters (hyphens allowed).")
            return False

        return True

    def save_to_csv(self):
        if not self.adoption_data:
            messagebox.showwarning("Warning", "No data to save.")
            return

        try:
            with open('adoption_records.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Pet Name", "Animal Type", "Breed Type", "Adoption Date"])
                writer.writerows(self.adoption_data)

            messagebox.showinfo("Saved", "Data has been saved to adoption_records.csv")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")

    def load_from_csv(self):
        try:
            with open('adoption_records.csv', 'r') as file:
                reader = csv.reader(file)
                # Skip header
                next(reader, None)
                self.adoption_data = list(reader)
                self.update_table()
        except FileNotFoundError:
            # Create empty file with headers
            with open('adoption_records.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Pet Name", "Animal Type", "Breed Type", "Adoption Date"])
            self.adoption_data = []
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
            self.adoption_data = []


# ------------------ App Runner ------------------ #
def main():
    def launch_app():
        app = PetAdoptionApp()
        app.mainloop()

    login = LoginForm(on_login_success=launch_app)
    login.mainloop()


if __name__ == '__main__':
    main()