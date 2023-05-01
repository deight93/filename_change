import tkinter as tk
import os

root = tk.Tk()
root.geometry("300x300")
root.title("File Explorer")

label = tk.Label(root, text="파일 경로:")
label.pack()

file_listbox = tk.Listbox(root)
file_listbox.pack(expand=True, fill='both')

entry = tk.Entry(root)
entry.pack()

def update_file_list():
    file_listbox.delete(0, tk.END)
    path = entry.get()
    if os.path.exists(path):
        for file_name in os.listdir(path):
            file_listbox.insert(tk.END, file_name)

button = tk.Button(root, text="목록 업데이트", command=update_file_list)
button.pack()

root.mainloop()