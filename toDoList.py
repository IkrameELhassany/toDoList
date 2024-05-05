import tkinter as tk
from tkinter import *

def add_task():
    task=entry.get()
    if(task):
        tasks.append(task)
        tasks_listbox.insert(tk.END, task)
        entry.delete(0,tk.END)

def delete_selected_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        deleted_task = tasks.pop(selected_task_index)
        tasks_listbox.delete(selected_task_index)

def delete_all_tasks():
    tasks_listbox.delete(0, tk.END)
    tasks.clear()

m=tk.Tk()
m.title("To-Do-Liste")

m.geometry("400x300")
tasks=[]

label=Label(m,text=' Enter Your Task',fg='Blue')
label.pack(pady=10)

entry = tk.Entry(m, width=30)
entry.pack(pady=10)

tasks_listbox = tk.Listbox(m, selectmode=tk.MULTIPLE, height=5, width=50)
tasks_listbox.pack()

scrollbar = tk.Scrollbar(m, command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)

button=tk.Button(m,text='Add',width=20,command=add_task,activebackground='green')
button1=tk.Button(m,text='Delete',width=20,command=delete_selected_task,activebackground='orange')
button2=tk.Button(m,text='Delete All Tasks',width=20,command=delete_all_tasks,activebackground='red')

button.pack(padx=5,pady=10)
button1.pack(padx=5,pady=10)
button2.pack(padx=5,pady=10)

m.mainloop()