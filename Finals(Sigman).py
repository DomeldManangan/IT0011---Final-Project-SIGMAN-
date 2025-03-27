import tkinter as tk
from tkinter import messagebox, ttk
import json

# File for data persistence
DATA_FILE = "users.json"

# Load existing records
try:
    with open(DATA_FILE, "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

def on_hover(event):
    event.widget.config(bg="#0b5394")

def on_leave(event, color):
    event.widget.config(bg=color)

def create_button(parent, text, command):
    btn = tk.Button(parent, text=text, width=30, bg="#2196F3", fg="white", font=("Helvetica", 14), command=command, relief=tk.FLAT, bd=0)
    btn.bind("<Enter>", lambda event: on_hover(event))
    btn.bind("<Leave>", lambda event: on_leave(event, "#2196F3"))
    return btn

def sign_up():
    def submit():
        try:
            first = entry_first.get()
            middle = entry_middle.get()
            last = entry_last.get()
            bday = entry_bday.get()
            gender = gender_var.get()
            
            if not (first and last and bday and gender):
                raise ValueError("Please fill in all required fields.")
            
            users.append({
                "first_name": first,
                "middle_name": middle,
                "last_name": last,
                "birthday": bday,
                "gender": gender
            })
            save_data()
            messagebox.showinfo("Success", "Record added successfully!")
            sign_up_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("1920x1080")
    sign_up_window.configure(bg="#2c2c2c")
    
    frame = tk.Frame(sign_up_window, padx=50, pady=50, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
    frame.pack(expand=True)
    
    tk.Label(frame, text="First Name:", bg="#ffffff", font=("Helvetica", 14)).grid(row=0, column=0, pady=5)
    entry_first = tk.Entry(frame, font=("Helvetica", 14))
    entry_first.grid(row=0, column=1, pady=5)
    
    tk.Label(frame, text="Middle Name:", bg="#ffffff", font=("Helvetica", 14)).grid(row=1, column=0, pady=5)
    entry_middle = tk.Entry(frame, font=("Helvetica", 14))
    entry_middle.grid(row=1, column=1, pady=5)
    
    tk.Label(frame, text="Last Name:", bg="#ffffff", font=("Helvetica", 14)).grid(row=2, column=0, pady=5)
    entry_last = tk.Entry(frame, font=("Helvetica", 14))
    entry_last.grid(row=2, column=1, pady=5)
    
    tk.Label(frame, text="Birthday (YYYY-MM-DD):", bg="#ffffff", font=("Helvetica", 14)).grid(row=3, column=0, pady=5)
    entry_bday = tk.Entry(frame, font=("Helvetica", 14))
    entry_bday.grid(row=3, column=1, pady=5)
    
    tk.Label(frame, text="Gender:", bg="#ffffff", font=("Helvetica", 14)).grid(row=4, column=0, pady=5)
    gender_var = tk.StringVar()
    ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female"], font=("Helvetica", 14)).grid(row=4, column=1, pady=5)
    
    submit_btn = create_button(frame, "Submit", submit)
    submit_btn.grid(row=5, column=1, pady=20)

def view_records():
    view_window = tk.Toplevel(root)
    view_window.title("All Records")
    view_window.geometry("1920x1080")
    view_window.configure(bg="#2c2c2c")
    
    frame = tk.Frame(view_window, padx=50, pady=50, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
    frame.pack(expand=True)
    
    for idx, record in enumerate(users):
        record_text = f"Last Name: {record['last_name']}\nMiddle Name: {record['middle_name']}\nFirst Name: {record['first_name']}\nBirthday: {record['birthday']}\nGender: {record['gender']}"
        tk.Label(frame, text=record_text, bg="#ffffff", font=("Helvetica", 14), justify=tk.LEFT, anchor="w").grid(row=idx, column=0, pady=5, sticky="w")

def search_record():
    def search():
        last_name = entry_search.get()
        result = next((user for user in users if user["last_name"] == last_name), None)
        if result:
            messagebox.showinfo("Result", f"Last Name: {result['last_name']}\nMiddle Name: {result['middle_name']}\nFirst Name: {result['first_name']}\nBirthday: {result['birthday']}\nGender: {result['gender']}")
        else:
            messagebox.showerror("Error", "No record found!")
    
    search_window = tk.Toplevel(root)
    search_window.title("Search Record")
    search_window.geometry("1920x1080")
    search_window.configure(bg="#2c2c2c")
    
    frame = tk.Frame(search_window, padx=50, pady=50, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
    frame.pack(expand=True)
    
    tk.Label(frame, text="Enter Last Name:", bg="#ffffff", font=("Helvetica", 14)).grid(row=0, column=0, pady=5)
    entry_search = tk.Entry(frame, font=("Helvetica", 14))
    entry_search.grid(row=0, column=1, pady=5)
    search_btn = create_button(frame, "Search", search)
    search_btn.grid(row=1, column=1, pady=20)

root = tk.Tk()
root.title("User Management System")
root.geometry("1920x1080")
root.configure(bg="#2c2c2c")

frame_main = tk.Frame(root, padx=50, pady=50, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
frame_main.pack(expand=True)

tk.Label(frame_main, text="User Management System", font=("Helvetica", 24, "bold"), bg="#ffffff").pack(pady=20)
tk.Label(frame_main, text="By Sigman", font=("Helvetica", 16), bg="#ffffff").pack(pady=5)
tk.Label(frame_main, text=" ", bg="#ffffff").pack(pady=5)

for text, command in [("Sign Up", sign_up), ("View All Records", view_records), ("Search Record", search_record), ("Exit", root.quit)]:
    btn = create_button(frame_main, text, command)
    btn.pack(pady=10)

root.mainloop()


