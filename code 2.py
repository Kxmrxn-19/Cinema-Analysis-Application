import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import operator
import webbrowser

# Load the data
df = pd.read_csv('cinema_sales.csv')

# Set window dimensions
HEIGHT = 600
WIDTH = 800

# Initialize the main window
window = tk.Tk()
window.title("Cinema Analysis")

# Create canvas
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# Main frame
main_frame = tk.Frame(canvas, bg="#2c3e50", bd=5)
main_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.1, anchor='n')

main_label = tk.Label(main_frame, text="Hello, what can I do for you?", font=('Helvetica', 16), bg="#2c3e50", fg="white")
main_label.pack()

# Analysis frame
analysis_frame = tk.Frame(window, bg="#34495e", bd=10)
analysis_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.6, anchor='n')

# Button frame
button_frame = tk.Frame(window, bg="#2c3e50", bd=10)
button_frame.place(relx=0.5, rely=0.85, relwidth=0.9, relheight=0.1, anchor='n')

def choice_2_1():
    d4 = {}
    for i in df.index:
        if df['cinema_code'].loc[i] not in d4.keys():
            d4[df['cinema_code'].loc[i]] = df['total_sales'].loc[i]
        else:
            d4[df['cinema_code'].loc[i]] += df['total_sales'].loc[i]
    k4 = list(d4.keys())
    v4 = list(d4.values())
    max4 = max(v4)
    min4 = min(v4)
    i4 = v4.index(max4)
    i_4 = v4.index(min4)

    plt.bar(d4.keys(), d4.values())
    plt.xlabel('Cinema Code')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Cinema Code')
    plt.show()

    win_2_1 = tk.Toplevel()
    H_2_1 = 100
    W_2_1 = 600
    c_2_1 = tk.Canvas(win_2_1, height=H_2_1, width=W_2_1)
    c_2_1.pack()
    t_2_1_1 = f"Cinema no {k4[i4]} has the highest earnings of {max4}"
    t_2_1_2 = f"Cinema no {k4[i_4]} has the lowest earnings of {min4}"
    l_2_1_1 = tk.Label(c_2_1, text=t_2_1_1, font=60)
    l_2_1_1.place(relx=0.5, rely=0.1, anchor='n')
    l_2_1_2 = tk.Label(c_2_1, text=t_2_1_2, font=60)
    l_2_1_2.place(relx=0.5, rely=0.4, anchor='n')

def choice_2_2():
    d5 = {}
    for i in df.index:
        if df['cinema_code'].loc[i] not in d5.keys():
            d5[df['cinema_code'].loc[i]] = df['tickets_sold'].loc[i]
        else:
            d5[df['cinema_code'].loc[i]] += df['tickets_sold'].loc[i]
    k5 = list(d5.keys())
    v5 = list(d5.values())
    max5 = max(v5)
    min5 = min(v5)
    i5 = v5.index(max5)
    i_5 = v5.index(min5)

    plt.bar(d5.keys(), d5.values())
    plt.xlabel('Cinema Code')
    plt.ylabel('Tickets Sold')
    plt.title('Tickets Sold by Cinema Code')
    plt.show()

    win_2_2 = tk.Toplevel()
    H_2_2 = 100
    W_2_2 = 600
    c_2_2 = tk.Canvas(win_2_2, height=H_2_2, width=W_2_2)
    c_2_2.pack()
    t_2_2_1 = f"Cinema no {k5[i5]} has the highest no of tickets sold {max5}"
    t_2_2_2 = f"Cinema no {k5[i_5]} has the lowest no of tickets sold {min5}"
    l_2_2_1 = tk.Label(c_2_2, text=t_2_2_1, font=60)
    l_2_2_1.place(relx=0.5, rely=0.1, anchor='n')
    l_2_2_2 = tk.Label(c_2_2, text=t_2_2_2, font=60)
    l_2_2_2.place(relx=0.5, rely=0.4, anchor='n')

def choice_2_3():
    d6 = {}
    for i in df.index:
        if df['cinema_code'].loc[i] not in d6.keys():
            d6[df['cinema_code'].loc[i]] = df['occu_perc'].loc[i]
        else:
            d6[df['cinema_code'].loc[i]] += df['occu_perc'].loc[i]

    plt.bar(d6.keys(), d6.values())
    plt.xlabel('Cinema Code')
    plt.ylabel('Occupancy Percentage')
    plt.title('Occupancy Percentage by Cinema Code')
    plt.show()

def choice_2():
    c_2 = tk.Toplevel()
    c_2.title("Cinema Analysis")
    canvas_2 = tk.Canvas(c_2, height=500, width=600)
    canvas_2.pack()

    f_2 = tk.Frame(canvas_2, bg='#34495e', bd=5)
    f_2.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

    l_2 = tk.Label(f_2, text="What do you want?", font=10, bg='#34495e', fg='white')
    l_2.place(relx=0.2, rely=0.1)

    b_2_1 = tk.Button(f_2, text="1. Comparison of cinemas based on earnings.", command=choice_2_1, bg="#e74c3c", fg="white")
    b_2_2 = tk.Button(f_2, text="2. Comparison based on tickets sold.", command=choice_2_2, bg="#3498db", fg="white")
    b_2_3 = tk.Button(f_2, text="3. Comparison based on occupancy percentage.", command=choice_2_3, bg="#2ecc71", fg="white")

    b_2_1.place(relx=0.1, rely=0.3)
    b_2_2.place(relx=0.1, rely=0.5)
    b_2_3.place(relx=0.1, rely=0.7)

def choice_1_1():
    d = {}
    for i in df.index:
        if df['film_code'].loc[i] not in d.keys():
            d[df['film_code'].loc[i]] = df['total_sales'].loc[i]
        else:
            d[df['film_code'].loc[i]] += df['total_sales'].loc[i]
    v1 = list(d.values())
    k1 = list(d.keys())
    max1 = max(v1)
    min1 = min(v1)
    i1 = v1.index(max1)
    i_1 = v1.index(min1)

    plt.bar(d.keys(), d.values())
    plt.xlabel('Film Code')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Film Code')
    plt.show()

    win_1_1 = tk.Toplevel()
    H_1_1 = 100
    W_1_1 = 600
    c_1_1 = tk.Canvas(win_1_1, height=H_1_1, width=W_1_1)
    c_1_1.pack()
    t1 = f"Movie no {k1[i1]} has the highest earnings of {max1}"
    t2 = f"Movie no {k1[i_1]} has the lowest earnings of {min1}"
    l_1_1 = tk.Label(c_1_1, text=t1, font=60)
    l_1_1.place(relx=0.5, rely=0.1, anchor='n')
    l_1_2 = tk.Label(c_1_1, text=t2, font=60)
    l_1_2.place(relx=0.5, rely=0.4, anchor='n')

def choice_1_2():
    d1 = {}
    for i in df.index:
        if df['film_code'].loc[i] not in d1.keys():
            d1[df['film_code'].loc[i]] = df['tickets_sold'].loc[i]
        else:
            d1[df['film_code'].loc[i]] += df['tickets_sold'].loc[i]
    v2 = list(d1.values())
    k2 = list(d1.keys())
    max2 = max(v2)
    min2 = min(v2)
    i2 = v2.index(max2)
    i_2 = v2.index(min2)

    plt.bar(d1.keys(), d1.values())
    plt.xlabel('Film Code')
    plt.ylabel('Tickets Sold')
    plt.title('Tickets Sold by Film Code')
    plt.show()

    win_1_2 = tk.Toplevel()
    H_1_2 = 100
    W_1_2 = 600
    c_1_2 = tk.Canvas(win_1_2, height=H_1_2, width=W_1_2)
    c_1_2.pack()
    t_1_1 = f"Movie no {k2[i2]} has the highest no of tickets sold {max2}"
    t_1_2 = f"Movie no {k2[i_2]} has the lowest no of tickets sold {min2}"
    l_1_1 = tk.Label(c_1_2, text=t_1_1, font=60)
    l_1_1.place(relx=0.5, rely=0.1, anchor='n')
    l_1_2 = tk.Label(c_1_2, text=t_1_2, font=60)
    l_1_2.place(relx=0.5, rely=0.4, anchor='n')

def choice_1_3():
    d2 = {}
    for i in df.index:
        if df['film_code'].loc[i] not in d2.keys():
            d2[df['film_code'].loc[i]] = df['occu_perc'].loc[i]
        else:
            d2[df['film_code'].loc[i]] += df['occu_perc'].loc[i]

    plt.bar(d2.keys(), d2.values())
    plt.xlabel('Film Code')
    plt.ylabel('Occupancy Percentage')
    plt.title('Occupancy Percentage by Film Code')
    plt.show()

def choice_1_4():
    d3 = {}
    for i in df.index:
        if df['film_code'].loc[i] not in d3.keys():
            d3[df['film_code'].loc[i]] = df['total_sales'].loc[i]
        else:
            d3[df['film_code'].loc[i]] += df['total_sales'].loc[i]
    v3 = list(d3.values())
    k3 = list(d3.keys())
    t = sorted(d3.items(), key=operator.itemgetter(1), reverse=True)

    win_1_4 = tk.Toplevel()
    H_1_4 = 400
    W_1_4 = 600
    c_1_4 = tk.Canvas(win_1_4, height=H_1_4, width=W_1_4)
    c_1_4.pack()
    t_1_4 = "Movie Codes  -  Earnings\n\n" + "\n".join([f"{i[0]} - {i[1]}" for i in t])
    l_1_4 = tk.Label(c_1_4, text=t_1_4, font=60)
    l_1_4.place(relx=0.5, rely=0.1, anchor='n')

def choice_1():
    c_1 = tk.Toplevel()
    c_1.title("Movie Analysis")
    canvas_1 = tk.Canvas(c_1, height=500, width=600)
    canvas_1.pack()

    f_1 = tk.Frame(canvas_1, bg='#34495e', bd=5)
    f_1.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

    l_1 = tk.Label(f_1, text="What do you want?", font=10, bg='#34495e', fg='white')
    l_1.place(relx=0.2, rely=0.1)

    b_1_1 = tk.Button(f_1, text="1. Comparison of movies based on earnings.", command=choice_1_1, bg="#e74c3c", fg="white")
    b_1_2 = tk.Button(f_1, text="2. Comparison based on tickets sold.", command=choice_1_2, bg="#3498db", fg="white")
    b_1_3 = tk.Button(f_1, text="3. Comparison based on occupancy percentage.", command=choice_1_3, bg="#2ecc71", fg="white")
    b_1_4 = tk.Button(f_1, text="4. Movies sorted based on earnings.", command=choice_1_4, bg="#f1c40f", fg="white")

    b_1_1.place(relx=0.1, rely=0.3)
    b_1_2.place(relx=0.1, rely=0.5)
    b_1_3.place(relx=0.1, rely=0.7)
    b_1_4.place(relx=0.1, rely=0.9)

def open_url():
    webbrowser.open("https://www.google.com")

# Add buttons to the button frame
button1 = tk.Button(button_frame, text="1. Movie Analysis", command=choice_1, bg="#e74c3c", fg="white")
button2 = tk.Button(button_frame, text="2. Cinema Analysis", command=choice_2, bg="#3498db", fg="white")
button3 = tk.Button(button_frame, text="Open Google", command=open_url, bg="#2ecc71", fg="white")

button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)

# Run the main loop
window.mainloop()
