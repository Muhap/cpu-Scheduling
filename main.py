import tkinter
from tkinter import ttk
import customtkinter
from ttkthemes import ThemedStyle

import fcfs
import round_robin
import sjfnp
import sjfp

q = 1
n = 0
at = []
bt = []
pid = []
pn = []
temp = []
flag = True

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

frame13 = customtkinter.CTkFrame(master=root)
frame12 = customtkinter.CTkFrame(master=root)
frame11 = customtkinter.CTkFrame(master=root)
frame10 = customtkinter.CTkFrame(master=root)
frame9 = customtkinter.CTkFrame(master=root)
frame8 = customtkinter.CTkFrame(master=root)
frame7 = customtkinter.CTkFrame(master=root)
frame6 = customtkinter.CTkFrame(master=root)
frame5 = customtkinter.CTkFrame(master=root)
frame4 = customtkinter.CTkFrame(master=root)
frame3 = customtkinter.CTkFrame(master=root)
frame2 = customtkinter.CTkFrame(master=root)
frame1 = customtkinter.CTkFrame(master=root)
frame0 = customtkinter.CTkFrame(master=root)
frame = customtkinter.CTkFrame(master=root)


def clear_frame_content(f):
    # Remove previous content
    frame_name = "frame" + str(f)
    ff = globals()[frame_name]
    for widget in ff.winfo_children():
        widget.destroy()


def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):

        row = []
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2


def algorithm1_2(n):
    def send(z, zz):
        at.append(z)
        bt.append(zz)

        global n
        n -= 1
        if n > 0:
            clear()
            algorithm1_2(n)
        else:

            final = fcfs.fcfs(at, bt)

            clear()

            frame6.pack(side=tkinter.RIGHT)
            frame6.pack_propagate(False)
            frame6.configure(width=1000, height=800)

            table = ttk.Treeview(master=frame6, columns=("Processes", "burst time", "waiting time", "Turn Around time"),
                                 show='headings')
            b = fcfs.retrieveAverage()
            label = customtkinter.CTkLabel(master=frame6, text="First Come First Served Algorithm", font=("Arial", 30,
                                                                                                          "bold"))
            label.pack(side="top", fill="x", expand=True)
            label = customtkinter.CTkLabel(master=frame6, text=f"Average waiting time = {b[0]}" , font=("Arial", 13,
                                                                                                           "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame6, text=f"Average turn around time = {b[1]}", font=("Arial",
                                                                                                                13,
                                                                                                                "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame6, text="", font=("Arial", 30, "bold"))
            label.pack(side="top", fill="x", expand=True)

            table.heading('Processes', text='AT')
            table.heading('burst time', text='BT')
            table.heading('waiting time', text='WT')
            table.heading('Turn Around time', text='TAT')

            table.column('Processes', width=80)
            table.column('burst time', width=80)
            table.column('waiting time', width=80)
            table.column('Turn Around time', width=80)

            style = ThemedStyle(root)
            style.set_theme("equilux")
            style.configure("Treeview", background="#212121", foreground="white")
            style.configure("Treeview.Heading", background="#212121", foreground="white")

            table.pack(fill='both', expand=True)
            final2 = []
            transpose(final, final2)

            for row in final2:
                table.insert('', 'end', values=row)

    global q
    clear_frame_content(5)
    frame5.pack(side=tkinter.RIGHT)
    frame5.pack_propagate(False)
    frame5.configure(width=1000, height=800)

    l1 = customtkinter.CTkLabel(master=frame5, text="Please Enter Arrival time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l1.pack(side="top", fill="x", expand=True)

    atEnter = customtkinter.CTkEntry(master=frame5)
    atEnter.pack(side="top", fill="x", expand=True)

    l2 = customtkinter.CTkLabel(master=frame5, text="Please Enter Burst time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l2.pack(side="top", fill="x", expand=True)

    btEnter = customtkinter.CTkEntry(master=frame5)
    btEnter.pack(side="top", fill="x")

    enter = customtkinter.CTkButton(master=frame5, text="Enter",
                                    command=lambda: send(int(atEnter.get()), int(btEnter.get())), height=50)
    enter.pack(side="top", fill="x", pady=100)
    q += 1


def algorithm1():
    clear_frame_content(1)

    def send1(x):
        global n
        n = x

        clear()
        algorithm1_2(n)

    clear()

    frame1.pack(side=tkinter.RIGHT)
    frame1.pack_propagate(False)
    frame1.configure(width=1000, height=800)

    label1 = customtkinter.CTkLabel(master=frame1, text="FCFS", font=("Arial", 12, "bold"))
    label1.pack(pady=12, padx=10)

    label = customtkinter.CTkLabel(master=frame1, text="Enter the number of Processes :", font=("Arial", 16, "bold"))
    label.pack(side="top", fill="x", expand=True)

    pNumber = customtkinter.CTkEntry(master=frame1)
    pNumber.pack(side="top", fill="x", expand=True)
    enter = customtkinter.CTkButton(master=frame1, text="Enter", command=lambda: send1(int(pNumber.get())), height=50)
    enter.pack(side="bottom", fill="x", expand=True)


def algorithm2_2(n, y):
    def send(z, zz):
        at.append(z)
        bt.append(zz)

        global n
        n -= 1
        if n > 0:
            clear()
            algorithm2_2(n, y)
        else:

            final = round_robin.rr(at, bt, y)

            clear()

            frame7.pack(side=tkinter.RIGHT)
            frame7.pack_propagate(False)
            frame7.configure(width=1000, height=800)

            table = ttk.Treeview(master=frame7, columns=("Processes", "burst time", "waiting time", "Turn Around time"),
                                 show='headings')
            b = round_robin.retrieveAverage()
            label = customtkinter.CTkLabel(master=frame7, text="Round robin Algorithm",
                                           font=("Arial", 30, "bold"))
            label.pack(side="top", fill="x", expand=True)
            label = customtkinter.CTkLabel(master=frame7, text=f"Average waiting time = {b[0]}", font=("Arial", 13,
                                                                                                       "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame7, text=f"Average turn around time = {b[1]}", font=("Arial",
                                                                                                           13,
                                                                                                           "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame7, text="", font=("Arial", 50, "bold"))
            label.pack(side="top", fill="x", expand=True)

            table.heading('Processes', text='PID')
            table.heading('burst time', text='BT')
            table.heading('waiting time', text='WT')
            table.heading('Turn Around time', text='TAT')

            table.column('Processes', width=80)
            table.column('burst time', width=80)
            table.column('waiting time', width=80)
            table.column('Turn Around time', width=80)

            style = ThemedStyle(root)
            style.set_theme("equilux")
            style.configure("Treeview", background="#212121", foreground="white")
            style.configure("Treeview.Heading", background="#212121", foreground="white")

            table.pack(fill='both', expand=True)

            final2 = []
            transpose(final, final2)
            for row in final2:
                table.insert('', 'end', values=row)

    global q
    clear_frame_content(8)
    frame8.pack(side=tkinter.RIGHT)
    frame8.pack_propagate(False)
    frame8.configure(width=1000, height=800)

    l1 = customtkinter.CTkLabel(master=frame8, text="Please Enter process ID",
                                font=("Arial", 20, "bold"))
    l1.pack(side="top", fill="x", expand=True)

    atEnter = customtkinter.CTkEntry(master=frame8)
    atEnter.pack(side="top", fill="x", expand=True)

    l2 = customtkinter.CTkLabel(master=frame8, text="Please Enter Burst time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l2.pack(side="top", fill="x", expand=True)

    btEnter = customtkinter.CTkEntry(master=frame8)
    btEnter.pack(side="top", fill="x")

    enter = customtkinter.CTkButton(master=frame8, text="Enter",
                                    command=lambda: send(int(atEnter.get()), int(btEnter.get())), height=50)
    enter.pack(side="top", fill="x", pady=100)
    q += 1


def algorithm2():
    clear_frame_content(2)

    def send1(x, y):
        global n
        n = x
        clear()
        algorithm2_2(n, y)

    clear()
    frame2.pack(side=tkinter.RIGHT)
    frame2.pack_propagate(False)
    frame2.configure(width=1000, height=800)
    label1 = customtkinter.CTkLabel(master=frame2, text="Round Robin", font=("Arial", 12, "bold"))
    label1.pack(pady=12, padx=10)

    label = customtkinter.CTkLabel(master=frame2, text="Enter the number of Processes :", font=("Arial", 16, "bold"))
    label.pack(side="top", fill="x", expand=True)
    pNumber = customtkinter.CTkEntry(master=frame2)
    pNumber.pack(side="top", fill="x", expand=True)

    label = customtkinter.CTkLabel(master=frame2, text="Enter Time quantum :", font=("Arial", 16, "bold"))
    label.pack(side="top", fill="x", expand=True)
    qNumber = customtkinter.CTkEntry(master=frame2)
    qNumber.pack(side="top", fill="x", expand=True)

    enter = customtkinter.CTkButton(master=frame2, text="Enter",
                                    command=lambda: send1(int(pNumber.get()), int(qNumber.get())), height=50)
    enter.pack(side="bottom", fill="x", expand=True)


def algorithm3_2(n, pd):
    def send(z, zz):
        at.append(z)
        bt.append(zz)

        global n
        n -= 1
        if n > 0:
            clear()
            algorithm3_2(n, pd)
        else:
            pp = [pd, bt, at]
            p = []
            transpose(pp, p)
            final = sjfp.sjf(p)

            clear()

            frame10.pack(side=tkinter.RIGHT)
            frame10.pack_propagate(False)
            frame10.configure(width=1000, height=800)

            table = ttk.Treeview(master=frame10,
                                 columns=("Processes", "burst time", "waiting time", "Turn Around time"),
                                 show='headings')
            b = sjfp.retrieveAverage()
            label = customtkinter.CTkLabel(master=frame10, text="Preemptive Shortest Job First", font=("Arial", 50,
                                                                                                       "bold"))
            label.pack(side="top", fill="x", expand=True)
            label = customtkinter.CTkLabel(master=frame10, text=f"Average waiting time = {b[0]}", font=("Arial", 13,
                                                                                                       "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame10, text=f"Average turn around time = {b[1]}", font=("Arial",
                                                                                                           13,
                                                                                                           "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame10, text="", font=("Arial", 50, "bold"))
            label.pack(side="top", fill="x", expand=True)

            table.heading('Processes', text='PID')
            table.heading('burst time', text='BT')
            table.heading('waiting time', text='WT')
            table.heading('Turn Around time', text='TAT')

            table.column('Processes', width=80)
            table.column('burst time', width=80)
            table.column('waiting time', width=80)
            table.column('Turn Around time', width=80)

            style = ThemedStyle(root)
            style.set_theme("equilux")
            style.configure("Treeview", background="#212121", foreground="white")
            style.configure("Treeview.Heading", background="#212121", foreground="white")

            table.pack(fill='both', expand=True)
            final2 = []
            transpose(final, final2)

            for row in final2:
                table.insert('', 'end', values=row)

    global q
    clear_frame_content(11)
    frame11.pack(side=tkinter.RIGHT)
    frame11.pack_propagate(False)
    frame11.configure(width=1000, height=800)

    l1 = customtkinter.CTkLabel(master=frame11, text="Please Enter Arrival time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l1.pack(side="top", fill="x", expand=True)

    atEnter = customtkinter.CTkEntry(master=frame11)
    atEnter.pack(side="top", fill="x", expand=True)

    l2 = customtkinter.CTkLabel(master=frame11, text="Please Enter Burst time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l2.pack(side="top", fill="x", expand=True)

    btEnter = customtkinter.CTkEntry(master=frame11)
    btEnter.pack(side="top", fill="x")

    enter = customtkinter.CTkButton(master=frame11, text="Enter",
                                    command=lambda: send(int(atEnter.get()), int(btEnter.get())), height=50)
    enter.pack(side="top", fill="x", pady=100)
    q += 1


def algorithm3():
    clear_frame_content(9)

    def send1(x):
        global n
        n = x
        for i in range(x):
            pid.append(i + 1)
        clear()
        algorithm3_2(n, pid)

    clear()

    frame9.pack(side=tkinter.RIGHT)
    frame9.pack_propagate(False)
    frame9.configure(width=1000, height=800)

    label1 = customtkinter.CTkLabel(master=frame9, text="SJF (preemptive)", font=("Arial", 12, "bold"))
    label1.pack(pady=12, padx=10)

    label = customtkinter.CTkLabel(master=frame9, text="Enter the number of Processes :", font=("Arial", 16, "bold"))
    label.pack(side="top", fill="x", expand=True)

    pNumber = customtkinter.CTkEntry(master=frame9)
    pNumber.pack(side="top", fill="x", expand=True)
    enter = customtkinter.CTkButton(master=frame9, text="Enter", command=lambda: send1(int(pNumber.get())), height=50)
    enter.pack(side="bottom", fill="x", expand=True)


def algorithm4_2(n):
    def send(z, zz):
        at.append(z)
        bt.append(zz)
        global n
        n -= 1
        if n > 0:
            clear()
            algorithm4_2(n)
        else:

            final = sjfnp.sjf_non_preemptive(at, bt)
            clear()

            frame12.pack(side=tkinter.RIGHT)
            frame12.pack_propagate(False)
            frame12.configure(width=1000, height=800)

            table = ttk.Treeview(master=frame12,
                                 columns=("Processes", "completion time", "Turn Around Time", "Waiting Time" , "Burst Time" , "Arrival time"),
                                 show='headings')
            b = sjfnp.retrieveAverage()
            label = customtkinter.CTkLabel(master=frame12, text="Non-Preemptive Shortest Job First", font=("Arial", 30,
                                                                                                           "bold"))
            label.pack(side="top", fill="x", expand=True)
            label = customtkinter.CTkLabel(master=frame12, text=f"Average waiting time = {b[0]}", font=("Arial", 13,
                                                                                                       "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame12, text=f"Average turn around time = {b[1]}", font=("Arial",
                                                                                                           13,
                                                                                                           "bold"))
            label.pack(side="top", fill="x")
            label = customtkinter.CTkLabel(master=frame12, text="", font=("Arial", 30, "bold"))
            label.pack(side="top", fill="x", expand=True)

            table.heading('Processes', text='PID')
            table.heading('completion time', text='CT')
            table.heading('Turn Around Time', text='TAT')
            table.heading('Waiting Time', text='WT')
            table.heading('Burst Time', text='BT')
            table.heading('Arrival time', text='AT')

            table.column('Processes', width=80)
            table.column('completion time', width=80)
            table.column('Turn Around Time', width=80)
            table.column('Waiting Time', width=80)
            table.column('Burst Time', width=80)
            table.column('Arrival time', width=80)

            style = ThemedStyle(root)
            style.set_theme("equilux")
            style.configure("Treeview", background="#212121", foreground="white")
            style.configure("Treeview.Heading", background="#212121", foreground="white")

            table.pack(fill='both', expand=True)
            transpose(final , temp)
            temp.append(bt)
            temp.append(at)
            final = []
            for i in range(len(temp[0])):
                temp[0][i] +=1
            transpose(temp, final)

            sorted_list = sorted(final, key=lambda x: (x[4], x[5]))

            for row in sorted_list:
                table.insert('', 'end', values=row)

    global q
    clear_frame_content(13)
    frame13.pack(side=tkinter.RIGHT)
    frame13.pack_propagate(False)
    frame13.configure(width=1000, height=800)

    l1 = customtkinter.CTkLabel(master=frame13, text="Please Enter Arrival time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l1.pack(side="top", fill="x", expand=True)

    atEnter = customtkinter.CTkEntry(master=frame13)
    atEnter.pack(side="top", fill="x", expand=True)

    l2 = customtkinter.CTkLabel(master=frame13, text="Please Enter Burst time of the process%d :" % q,
                                font=("Arial", 20, "bold"))
    l2.pack(side="top", fill="x", expand=True)

    btEnter = customtkinter.CTkEntry(master=frame13)
    btEnter.pack(side="top", fill="x")

    enter = customtkinter.CTkButton(master=frame13, text="Enter",
                                    command=lambda: send(int(atEnter.get()), int(btEnter.get())), height=50)
    enter.pack(side="top", fill="x", pady=100)
    q += 1


def algorithm4():
    clear_frame_content(4)

    def send1(x):
        global n
        n = x

        clear()
        algorithm4_2(n)

    clear()
    frame4.pack(side=tkinter.RIGHT)
    frame4.pack_propagate(False)
    frame4.configure(width=1000, height=800)
    label4 = customtkinter.CTkLabel(master=frame4, text="SJF (non-preemptive)")
    label4.pack(pady=12, padx=10)
    label = customtkinter.CTkLabel(master=frame4, text="Enter the number of Processes :", font=("Arial", 16, "bold"))
    label.pack(side="top", fill="x", expand=True)

    pNumber = customtkinter.CTkEntry(master=frame4)
    pNumber.pack(side="top", fill="x", expand=True)
    enter = customtkinter.CTkButton(master=frame4, text="Enter", command=lambda: send1(int(pNumber.get())), height=50)
    enter.pack(side="bottom", fill="x", expand=True)


def clear():
    frame0.pack_forget()
    frame13.pack_forget()
    frame12.pack_forget()
    frame11.pack_forget()
    frame10.pack_forget()
    frame9.pack_forget()
    frame8.pack_forget()
    frame7.pack_forget()
    frame6.pack_forget()
    frame5.pack_forget()
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack_forget()
    frame1.pack_forget()


def nav():
    frame.pack(side=tkinter.LEFT)
    frame.pack_propagate(False)
    frame.configure(width=300, height=800)

    label = customtkinter.CTkLabel(master=frame, text="Algorithms : ", font=("Arial", 35, "bold"))
    label.pack(pady=12, padx=10)

    button1 = customtkinter.CTkButton(master=frame, text="First Come First Served", font=("Arial", 15, "bold"),
                                      command=lambda: algorithm1(), height=60)
    button1.pack(pady=30, padx=10)

    button2 = customtkinter.CTkButton(master=frame, text="Round robin", font=("Arial", 15, "bold"),
                                      command=lambda: algorithm2(), height=60)
    button2.pack(pady=30, padx=10)

    button3 = customtkinter.CTkButton(master=frame, text="Shortest Job First (preemptive)", font=("Arial", 15, "bold"),
                                      command=lambda: algorithm3(), height=60)
    button3.pack(pady=30, padx=10)

    button4 = customtkinter.CTkButton(master=frame, text="Shortest Job First (non-preemptive)",
                                      font=("Arial", 15, "bold"), command=lambda: algorithm4(), height=60)
    button4.pack(pady=30, padx=10)


def home():
    frame0.pack(side=tkinter.RIGHT)
    frame0.pack_propagate(False)
    frame0.configure(width=1000, height=800)

    welcome = customtkinter.CTkLabel(master=frame0, text="Welcome to CPU Schedule Algorithms Program ! ",
                                     font=("Arial", 34, "bold"))
    welcome.pack(pady=200, padx=10)
    label = customtkinter.CTkLabel(master=frame0, text="Choose an Algorithm from the Left", font=("Arial", 25, "bold"))
    label.pack(pady=12, padx=10)
    welcome.pack(pady=200, padx=10)


home()
nav()

root.mainloop()
