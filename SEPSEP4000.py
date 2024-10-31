import csv
import os
import math
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog, messagebox

def main(path,count):
    """
    path -> is the file
    count -> split intervals
    """
    head_tail=os.path.split(path)
    file_name=head_tail[-1].rstrip(".csv")

    csv_lines=list(csv.reader(open(path,'r')))
    rows=len(csv_lines)
    a,b,count=0,count,count #start-finish-step
    file_number=math.ceil(rows/count)
    header=""

    #looking for header
    for line in csv_lines:
        if 'Elements' in line:
            header=line

    #printing stuff
    for i in range(1,file_number+1,1):
        with open(f'{file_name}_{a}-{b}.csv','w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            if a!=0: writer.writerow(header)
            writer.writerows(csv_lines[a:b])
        
        #stepping
        a=b
        b+=count


def browse_file():
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:  # Check if a file was selected
        app.file_path = file_path  # Store the full file path in the app's attribute
        file_path_entry.delete(0, tk.END)  # Clear existing entry
        file_path_entry.insert(0, file_path)  # Insert the selected file path


def submit():
    try:
        count = int(split_number_entry.get())
        #if not hasattr(app, "file_path") or not app.file_path:
            #messagebox.showwarning("Warning", "Please select a CSV file.")
            #return
        #if count <= 0:
            #messagebox.showwarning("Warning", "Count should be a positive integer.")
            #return
        main(app.file_path, count)
        result_label.config(text="*** DONE ***")

    except ValueError:
        #messagebox.showwarning("Warning", "Please enter a valid integer for the count.")
        result_label.config(text="ERROR !")


# Initialize the GUI
app = tk.Tk()
app.title("SEPSEP4000")
app.geometry("450x200")
app.configure(bg="black")  # Set background color to gray
app.resizable(False,False)
app.eval('tk::PlaceWindow . center') # middle pop up

font1 = font.Font(family="Consolas", size=10)
font2 = font.Font(family="Consolas", size=11, weight="bold")
font3 = font.Font(family="Consolas", size=11)

# File selection label and entry
file_label = tk.Button(app, text="Select File :", command=browse_file, width=15,font=font1, bg="#444", fg="#00FF00")
file_label.place(x=20, y=20)  # Adjust x and y as needed

# Retrieve the button's height
button_height = file_label.winfo_reqheight()

file_path_entry = tk.Entry(app, width=45)
file_path_entry.place(x=150, y=20, height=button_height)

# Split count label and entry
count_label = tk.Label(app, text="Split No :",width=15,font=font1, fg="#00FF00", bg="black")
count_label.place(x=20, y=75)

split_number_entry = tk.Entry(app, width=6)
split_number_entry.place(x=150, y=73, height=button_height)

# Result label
result_label = tk.Label(app, text="waiting...", bg="black", fg="#00FF00",width=20, font=font3)
result_label.place(x=240, y=75)

# Split button
split_btn = tk.Button(app, text="SPLIT", command=submit, width=40, height=2, font=font2, bg="#444", fg="#00FF00")
split_btn.place(x=65, y=132)

app.mainloop()