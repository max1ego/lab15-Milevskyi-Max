import tkinter as tk
from collections import Counter
import re

def find_top_words():
    try:
        with open("mytext.txt", "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        label_result.config(text="Файл mytext.txt не знайдено.")
        return

    words = re.findall(r'\b\w+\b', text)
    
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(3)

    for i, (word, _) in enumerate(most_common_words):
        entries[i].delete(0, tk.END)
        entries[i].insert(0, word)

root = tk.Tk()
root.title("Найчастіші слова")

label_instruction = tk.Label(root, text="Найчастіші слова в тексті:")
label_instruction.grid(row=0, column=0, columnspan=3)

entries = [tk.Entry(root, width=20) for _ in range(3)]
for i, entry in enumerate(entries):
    entry.grid(row=1, column=i)

button_find = tk.Button(root, text="Знайти слова", command=find_top_words)
button_find.grid(row=2, column=0, columnspan=3)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=3)

root.mainloop()
