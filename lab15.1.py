import json
import tkinter as tk
from tkinter import messagebox

try:
    with open("baza.json", "r", encoding="utf-8") as file:
        employees = json.load(file)
except FileNotFoundError:
    messagebox.showerror("Помилка", "Файл baza.json не знайдено.")
    employees = []

def find_birth_year():
    surname = surname_entry.get().strip()
    for employee in employees:
        if employee["surname"].lower() == surname.lower():
            birth_year_entry.delete(0, tk.END)
            birth_year_entry.insert(0, str(employee["year_of_birth"]))
            return
    messagebox.showinfo("Результат", "Робітника з таким прізвищем не знайдено.")

def display_all_employees():
    employees_text.delete(1.0, tk.END)
    for employee in employees:
        employees_text.insert(tk.END, f"{employee['surname']}: {employee['year_of_birth']}\n")

root = tk.Tk()
root.title("Дані про співробітників")
root.geometry("450x350")
root.configure(bg="blue")

tk.Label(root, text="Введіть прізвище робітника:", bg="blue", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
surname_entry = tk.Entry(root)
surname_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Рік народження:", bg="blue", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
birth_year_entry = tk.Entry(root)
birth_year_entry.grid(row=1, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Знайти", command=find_birth_year)
search_button.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Список усіх робітників:", bg="blue", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
employees_text = tk.Text(root, width=40, height=10)
employees_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
display_all_employees()

root.mainloop()
