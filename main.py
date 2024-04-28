


# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from tkcalendar import Calendar
# from datetime import datetime
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# # Sample data structure to store daily data
# daily_data = {'High': {}, 'Low': {}}
#
# # Dictionary to hold canvas references
# canvas_refs = {}
#
#
# # Function to save daily data
# def save_daily_data():
#     date = date_entry.get()
#     systolic_bp = systolic_bp_entry.get()
#     diastolic_bp = diastolic_bp_entry.get()
#     blood_sugar = blood_sugar_entry.get()
#     medicines = [medicines_entry[i].get() for i in range(len(medicines_entry))]
#
#     if date and systolic_bp and diastolic_bp and blood_sugar:
#         try:
#             systolic_bp = int(systolic_bp)
#             diastolic_bp = int(diastolic_bp)
#             blood_sugar = float(blood_sugar)
#             date_obj = datetime.strptime(date, "%Y-%m-%d")
#             daily_data[date] = {'systolic_bp': systolic_bp, 'diastolic_bp': diastolic_bp, 'blood_sugar': blood_sugar,
#                                 'medicines': medicines}
#             messagebox.showinfo("Success", "Data saved successfully!")
#         except ValueError:
#             messagebox.showerror("Error",
#                                  "Invalid input! Blood pressure must be integers and blood sugar must be numeric.")
#     else:
#         messagebox.showerror("Error", "Please fill in all fields.")
#
#
# # Function to plot blood pressure levels
# def plot_blood_pressure():
#     dates = list(daily_data.keys())
#     systolic_bp_values = [daily_data[date].get('systolic_bp', None) for date in dates]
#     diastolic_bp_values = [daily_data[date].get('diastolic_bp', None) for date in dates]
#
#     fig, ax = plt.subplots(figsize=(8, 4))
#
#     ax.plot(dates, systolic_bp_values, marker='o', color='r', label='Systolic BP')
#     ax.plot(dates, diastolic_bp_values, marker='o', color='b', label='Diastolic BP')
#     ax.set_title('Blood Pressure Levels')
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Blood Pressure')
#     ax.legend()
#     ax.set_xticks(range(len(dates)))
#     ax.set_xticklabels(dates, rotation=45, ha='right')
#
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
#
#     # Store canvas reference
#     canvas_refs['blood_pressure'] = canvas
#
#     # Bind event handler for mouse click
#     canvas.mpl_connect('button_press_event', on_plot_click)
#
#
# # Function to plot blood sugar levels
# def plot_blood_sugar():
#     dates = list(daily_data.keys())
#     blood_sugar_values = [daily_data[date].get('blood_sugar', None) for date in dates]
#
#     fig, ax = plt.subplots(figsize=(8, 4))
#
#     ax.plot(dates, blood_sugar_values, marker='o', color='g', label='Blood Sugar')
#     ax.set_title('Blood Sugar Levels')
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Blood Sugar')
#     ax.legend()
#     ax.set_xticks(range(len(dates)))
#     ax.set_xticklabels(dates, rotation=45, ha='right')
#
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
#
#     # Store canvas reference
#     canvas_refs['blood_sugar'] = canvas
#
#     # Bind event handler for mouse click
#     canvas.mpl_connect('button_press_event', on_plot_click)
#
#
# # Event handler for plot click
# def on_plot_click(event):
#     if event.inaxes:
#         x_date = event.xdata
#         dates = list(daily_data.keys())
#         closest_date_index = min(range(len(dates)), key=lambda i: abs(i - x_date))
#         selected_date = dates[closest_date_index]
#         display_data(selected_date)
#
#
# # Function to display data for a specific date
# def display_data(selected_date):
#     if selected_date in daily_data:
#         data = daily_data[selected_date]
#         messagebox.showinfo("Data for {}".format(selected_date),
#                             "Systolic BP: {}\nDiastolic BP: {}\nBlood Sugar: {}\nMedicines: {}".format(
#                                 data.get('systolic_bp', 'N/A'),
#                                 data.get('diastolic_bp', 'N/A'),
#                                 data.get('blood_sugar', 'N/A'),
#                                 '\n'.join(data.get('medicines', ['N/A']))
#                             ))
#     else:
#         messagebox.showinfo("No Data", "No data available for {}".format(selected_date))
#
#
# # Function to close the plot window
# def close_plot():
#     for canvas_ref in canvas_refs.values():
#         canvas_ref.get_tk_widget().destroy()
#     canvas_refs.clear()
#
#
# # Function to record today's date
# def record_today_date():
#     today_date = datetime.now().strftime("%Y-%m-%d")
#     date_entry.delete(0, tk.END)
#     date_entry.insert(0, today_date)
#
#
# # Function to choose a specific date using a calendar widget
# def choose_specific_date():
#     def on_date_select():
#         selected_date = cal.get_date()
#         date_entry.delete(0, tk.END)
#         date_entry.insert(0, selected_date)
#         top.destroy()
#
#     top = tk.Toplevel(root)
#     cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd", font=('Helvetica', 12))
#     cal.pack(fill="both", expand=True, padx=20, pady=20)
#     ok_button = ttk.Button(top, text="OK", command=on_date_select, style="TButton")
#     ok_button.pack()
#
#
# # Function to add more medicine fields
# def add_more_medicine():
#     next_row = len(medicines_entry) + 4
#     new_medicine_label = ttk.Label(main_frame, text=f"Medicine {next_row - 3}:")
#     new_medicine_label.grid(row=next_row, column=0, padx=5, pady=5, sticky="w")
#     new_medicine_entry = ttk.Entry(main_frame)
#     new_medicine_entry.grid(row=next_row, column=1, padx=5, pady=5)
#     medicines_entry.append(new_medicine_entry)
#
#
# # Create main window
# root = tk.Tk()
# root.title("Health Tracker")
#
# # UI Elements
# main_frame = ttk.Frame(root, padding=(20, 10))
# main_frame.grid(row=0, column=0, sticky="nsew")
#
# date_label = ttk.Label(main_frame, text="Date (YYYY-MM-DD):")
# date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
# date_entry = ttk.Entry(main_frame)
# date_entry.grid(row=0, column=1, padx=5, pady=5)
#
# record_today_button = ttk.Button(main_frame, text="Record Today's Date", command=record_today_date)
# record_today_button.grid(row=0, column=2, padx=5, pady=5)
#
# choose_date_button = ttk.Button(main_frame, text="Choose Specific Date", command=choose_specific_date)
# choose_date_button.grid(row=0, column=3, padx=5, pady=5)
#
# systolic_bp_label = ttk.Label(main_frame, text="Systolic Blood Pressure:")
# systolic_bp_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
# systolic_bp_entry = ttk.Entry(main_frame)
# systolic_bp_entry.grid(row=1, column=1, padx=5, pady=5)
#
# diastolic_bp_label = ttk.Label(main_frame, text="Diastolic Blood Pressure:")
# diastolic_bp_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
# diastolic_bp_entry = ttk.Entry(main_frame)
# diastolic_bp_entry.grid(row=2, column=1, padx=5, pady=5)
#
# blood_sugar_label = ttk.Label(main_frame, text="Blood Sugar:")
# blood_sugar_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
# blood_sugar_entry = ttk.Entry(main_frame)
# blood_sugar_entry.grid(row=3, column=1, padx=5, pady=5)
#
# medicines_label = ttk.Label(main_frame, text="Medicines:")
# medicines_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
# medicines_entry = [ttk.Entry(main_frame)]
# medicines_entry[0].grid(row=4, column=1, padx=5, pady=5)
#
# add_more_button = ttk.Button(main_frame, text="Add More Medicine", command=add_more_medicine)
# add_more_button.grid(row=5, column=1, padx=5, pady=5)
#
# save_button = ttk.Button(main_frame, text="Save", command=save_daily_data)
# save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
#
# plot_bp_button = ttk.Button(main_frame, text="Plot Blood Pressure", command=plot_blood_pressure)
# plot_bp_button.grid(row=7, column=0, padx=5, pady=5)
#
# plot_sugar_button = ttk.Button(main_frame, text="Plot Blood Sugar", command=plot_blood_sugar)
# plot_sugar_button.grid(row=7, column=1, padx=5, pady=5)
#
# close_plot_button = ttk.Button(main_frame, text="Close Plot", command=close_plot)
# close_plot_button.grid(row=8, column=0, columnspan=2, pady=5)
#
# # Column and row weights
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# main_frame.columnconfigure((0, 1), weight=1)
#
# root.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data structure to store daily data
daily_data = {'High': {}, 'Low': {}}

# Dictionary to hold canvas references
canvas_refs = {}


# Function to save daily data
def save_daily_data():
    date = date_entry.get()
    systolic_bp = systolic_bp_entry.get()
    diastolic_bp = diastolic_bp_entry.get()
    blood_sugar = blood_sugar_entry.get()
    medicines = [medicines_entry[i].get() for i in range(len(medicines_entry))]

    if date and systolic_bp and diastolic_bp and blood_sugar:
        try:
            systolic_bp = int(systolic_bp)
            diastolic_bp = int(diastolic_bp)
            blood_sugar = float(blood_sugar)
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            daily_data[date] = {'systolic_bp': systolic_bp, 'diastolic_bp': diastolic_bp, 'blood_sugar': blood_sugar,
                                'medicines': medicines}
            messagebox.showinfo("Success", "Data saved successfully!")
        except ValueError:
            messagebox.showerror("Error",
                                 "Invalid input! Blood pressure must be integers and blood sugar must be numeric.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


# Function to plot blood pressure levels
def plot_blood_pressure():
    dates = list(daily_data.keys())
    systolic_bp_values = [daily_data[date].get('systolic_bp', None) for date in dates]
    diastolic_bp_values = [daily_data[date].get('diastolic_bp', None) for date in dates]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(dates, systolic_bp_values, marker='o', color='r', label='Systolic BP')
    ax.plot(dates, diastolic_bp_values, marker='o', color='b', label='Diastolic BP')
    ax.set_title('Blood Pressure Levels')
    ax.set_xlabel('Date')
    ax.set_ylabel('Blood Pressure')
    ax.legend()
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(dates, rotation=45, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Store canvas reference
    canvas_refs['blood_pressure'] = canvas

    # Bind event handler for mouse click
    canvas.mpl_connect('button_press_event', on_plot_click)


# # Function to plot blood sugar levels
# def plot_blood_sugar():
#     dates = list(daily_data.keys())
#     blood_sugar_values = [daily_data[date].get('blood_sugar', None) for date in dates]
#
#     fig, ax = plt.subplots(figsize=(8, 4))
#
#     ax.plot(dates, blood_sugar_values, marker='o', color='g', label='Blood Sugar')
#     ax.set_title('Blood Sugar Levels')
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Blood Sugar')
#     ax.legend()
#     ax.set_xticks(range(len(dates)))
#     ax.set_xticklabels(dates, rotation=45, ha='right')
#
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
#
#     # Store canvas reference
#     canvas_refs['blood_sugar'] = canvas
#
#     # Bind event handler for mouse click
#     canvas.mpl_connect('button_press_event', on_plot_click)

# Function to plot blood sugar levels
def plot_blood_sugar():
    dates = list(daily_data.keys())
    blood_sugar_values = [daily_data[date].get('blood_sugar', None) for date in dates]

    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot blood sugar values
    ax.plot(dates, blood_sugar_values, marker='o', color='g', label='Blood Sugar')

    # Highlight normal, too high, and too low areas
    for date, value in zip(dates, blood_sugar_values):
        if value is not None:
            if value < 80:
                ax.axhspan(0, 80, facecolor='red', alpha=0.3)
            elif value > 120:
                ax.axhspan(120, 300, facecolor='red', alpha=0.3)
            else:
                ax.axhspan(80, 120, facecolor='green', alpha=0.3)

    ax.set_title('Blood Sugar Levels')
    ax.set_xlabel('Date')
    ax.set_ylabel('Blood Sugar')
    ax.legend()
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(dates, rotation=45, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Store canvas reference
    canvas_refs['blood_sugar'] = canvas

    # Bind event handler for mouse click
    canvas.mpl_connect('button_press_event', on_plot_click)


# Event handler for plot click
def on_plot_click(event):
    if event.inaxes:
        x_date = event.xdata
        dates = list(daily_data.keys())
        closest_date_index = min(range(len(dates)), key=lambda i: abs(i - x_date))
        selected_date = dates[closest_date_index]
        display_data(selected_date)


# Function to display data for a specific date
def display_data(selected_date):
    if selected_date in daily_data:
        data = daily_data[selected_date]
        messagebox.showinfo("Data for {}".format(selected_date),
                            "Systolic BP: {}\nDiastolic BP: {}\nBlood Sugar: {}\nMedicines: {}".format(
                                data.get('systolic_bp', 'N/A'),
                                data.get('diastolic_bp', 'N/A'),
                                data.get('blood_sugar', 'N/A'),
                                '\n'.join(data.get('medicines', ['N/A']))
                            ))
    else:
        messagebox.showinfo("No Data", "No data available for {}".format(selected_date))


# # Function to close the plot window
# def close_plot():
#     for canvas_ref in canvas_refs.values():
#         canvas_ref.get_tk_widget().destroy()
#     canvas_refs.clear()
# Function to close the plot window
def close_plot():
    print("Closing plot...")
    for canvas_ref in canvas_refs.values():
        canvas_ref.get_tk_widget().destroy()
    canvas_refs.clear()



# Function to record today's date
def record_today_date():
    today_date = datetime.now().strftime("%Y-%m-%d")
    date_entry.delete(0, tk.END)
    date_entry.insert(0, today_date)


# Function to choose a specific date using a calendar widget
def choose_specific_date():
    def on_date_select():
        selected_date = cal.get_date()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, selected_date)
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd", font=('Helvetica', 12))
    cal.pack(fill="both", expand=True, padx=20, pady=20)
    ok_button = ttk.Button(top, text="OK", command=on_date_select, style="TButton")
    ok_button.pack()


# Function to add more medicine fields
def add_more_medicine():
    next_row = len(medicines_entry) + 4
    new_medicine_label = ttk.Label(main_frame, text=f"Medicine {next_row - 3}:")
    new_medicine_label.grid(row=next_row, column=0, padx=5, pady=5, sticky="w")
    new_medicine_entry = ttk.Entry(main_frame)
    new_medicine_entry.grid(row=next_row, column=1, padx=5, pady=5)
    medicines_entry.append(new_medicine_entry)



# Validation function for blood sugar entry
def validate_blood_sugar(value):
    if not value:
        blood_sugar_validation_label.config(text="")
        return True

    try:
        blood_sugar = float(value)
        if 80 <= blood_sugar <= 120:
            blood_sugar_validation_label.config(text="Normal", foreground="green")
        elif blood_sugar < 80:
            blood_sugar_validation_label.config(text="Too Low", foreground="red")
        else:
            blood_sugar_validation_label.config(text="Too High", foreground="red")
        return True
    except ValueError:
        blood_sugar_validation_label.config(text="Invalid Input", foreground="red")
        return False


# Create main window
root = tk.Tk()
root.title("Health Tracker")

# UI Elements
main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.grid(row=0, column=0, sticky="nsew")

date_label = ttk.Label(main_frame, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
date_entry = ttk.Entry(main_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)

record_today_button = ttk.Button(main_frame, text="Record Today's Date", command=record_today_date)
record_today_button.grid(row=0, column=2, padx=5, pady=5)

choose_date_button = ttk.Button(main_frame, text="Choose Specific Date", command=choose_specific_date)
choose_date_button.grid(row=0, column=3, padx=5, pady=5)

systolic_bp_label = ttk.Label(main_frame, text="Systolic Blood Pressure:")
systolic_bp_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
systolic_bp_entry = ttk.Entry(main_frame)
systolic_bp_entry.grid(row=1, column=1, padx=5, pady=5)

diastolic_bp_label = ttk.Label(main_frame, text="Diastolic Blood Pressure:")
diastolic_bp_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
diastolic_bp_entry = ttk.Entry(main_frame)
diastolic_bp_entry.grid(row=2, column=1, padx=5, pady=5)

blood_sugar_label = ttk.Label(main_frame, text="Blood Sugar:")
blood_sugar_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
blood_sugar_entry = ttk.Entry(main_frame, validate="all", validatecommand=(root.register(validate_blood_sugar), "%P"))
blood_sugar_entry.grid(row=3, column=1, padx=5, pady=5)
blood_sugar_validation_label = ttk.Label(main_frame, text="", foreground="green")
blood_sugar_validation_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

medicines_label = ttk.Label(main_frame, text="Medicines:")
medicines_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
medicines_entry = [ttk.Entry(main_frame)]
medicines_entry[0].grid(row=4, column=1, padx=5, pady=5)

add_more_button = ttk.Button(main_frame, text="Add More Medicine", command=add_more_medicine)
add_more_button.grid(row=5, column=1, padx=5, pady=5)

save_button = ttk.Button(main_frame, text="Save", command=save_daily_data)
save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

plot_bp_button = ttk.Button(main_frame, text="Plot Blood Pressure", command=plot_blood_pressure)
plot_bp_button.grid(row=7, column=0, padx=5, pady=5)

plot_sugar_button = ttk.Button(main_frame, text="Plot Blood Sugar", command=plot_blood_sugar)
plot_sugar_button.grid(row=7, column=1, padx=5, pady=5)

close_plot_button = ttk.Button(main_frame, text="Close Plot", command=close_plot)
close_plot_button.grid(row=8, column=0, columnspan=2, pady=5)

# Column and row weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure((0, 1), weight=1)

root.mainloop()
