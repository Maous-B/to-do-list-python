from tkinter import *
import tkinter

root = Tk()
root.title("TO-DO List")
root.geometry("650x400")
root.resizable(False, False)

task_list = []

def openTaskFile():
    try:
        global task_list 
        global listbox   
        with open("taskfile.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('taskfile.txt', "w")
        file.close()
def delete_task():
    global task_list
    global listbox
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("taskfile.txt", "w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)

def add_task():
    global task_list
    global listbox
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("taskfile.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


label1 = Label(root, text="TO-DO List by Maous-B with the help of Youtube !")
label1.pack(side=TOP)

frame= Frame(root, width=400, height=50, bg="white")
frame.place(x=650/5, y=100)
task = StringVar()
task_entry = Entry(frame, width=19, font="Arial", bd=0)
task_entry.place(x=10, y=5)
task_entry.focus()


add_task_button = Button(root, text="Add Task", command=add_task)
add_task_button.pack(side=TOP)

delete_task_button = Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(side=TOP)


frame1 = Frame(root, width=700, height=250, bg="#949494")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('arial', 20), width=50, height=20, fg="white", cursor='hand2', bg='#ff7d7d', selectbackground='#6b6b6b')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)


openTaskFile()

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


root.mainloop()