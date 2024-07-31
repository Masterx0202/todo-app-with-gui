import customtkinter as ctk

root = ctk.CTk()
root.title("To-Do App")
root.geometry("300x400")

def add_task():
    task = entry.get()
    task_label = ctk.CTkLabel(frame, text=task)
    task_label.pack(pady=2)




button = ctk.CTkButton(root, text="submit", command=add_task)
entry = ctk.CTkEntry(root, placeholder_text="input task")
button.pack()
entry.pack()



frame = ctk.CTkFrame(root)
frame.pack()

root.mainloop()