import tkinter as tk
from tkinter import ttk

def toggle_check_all(button, checkboxes_group):
    # Check all if at least one checkbox is unchecked
    if any(var.get() == 0 for var in checkboxes_group):
        for var in checkboxes_group:
            var.set(1)
        button.config(text="Uncheck All")
    # Uncheck all if all checkboxes are checked
    else:
        for var in checkboxes_group:
            var.set(0)
        button.config(text="Check All")

def create_checkbox_group(root, group_num, column_weight=1, num_checkboxes=10):
    checkboxes_group = []
    group_frame = tk.Frame(root, relief="groove", borderwidth=2)
    group_frame.grid(row=0, column=group_num, padx=10, pady=10, sticky="nsew")
    group_frame.grid_columnconfigure(0, weight=column_weight)

    group_label = tk.Label(group_frame, text=f"List Devices")
    group_label.grid(row=0, column=0, columnspan=2)

    check_all_button = tk.Button(group_frame, text="Check All")
    check_all_button.grid(row=1, column=0, sticky="w")  # Align to the left
    check_all_button.config(command=lambda button=check_all_button: toggle_check_all(button, checkboxes_group))

    for i in range(num_checkboxes):
        var = tk.IntVar()
        checkboxes_group.append(var)
        checkbox = tk.Checkbutton(group_frame, text=f"Checkbox {i + 1}", variable=var)
        checkbox.grid(row=i + 2, column=0, sticky="w")  # Align to the left

    return checkboxes_group

def create_button(root, text, row, column, width=None, height=None, fg=None, font=None):
    button = tk.Button(root, text=text, width=width, height=height, padx=2, pady=2, fg=fg, font=font)
    button.grid(row=row, column=column, padx=2, pady=2)  # Set the same pady for all buttons
    return button

def start_button_click():
    start_button.config(state="disabled")  # Disable the Start button
    stop_button.config(state="normal")  # Enable the Stop button

def stop_button_click():
    stop_button.config(state="disabled")  # Disable the Stop button
    start_button.config(state="normal")  # Enable the Start button

root = tk.Tk()
root.title("Checkbox Example")

# Set the width and height of the main window
window_width = 800
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Create the first group of checkboxes
checkboxes_group1 = create_checkbox_group(root, 0, num_checkboxes=10)

# Create the "Load Devices" button below Group 1 with a specified height
load_devices_button = create_button(root, "Load Devices", 1, 0, width=10, height=1, fg="blue", font=("Helvetica", 10))

# Create a frame for Group 2 with a tab control and four times the width of Group 1
group_frame2 = tk.Frame(root, relief="groove", borderwidth=2)
group_frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
group_frame2.grid_columnconfigure(0, weight=4)  # Four times wider

group_frame3 = tk.Frame(root, relief="groove")
group_frame3.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Create the tab control inside Group 2
tab_control = ttk.Notebook(group_frame2)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
# option solo or rally
tab_control.add(tab1, text=" Setting")
# tab_control.add(tab2, text="Rally Boss")
# tab_control.add(tab3, text="Troop")
tab_control.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Create IntVar to hold the selected radio button value
selected_option = tk.IntVar()

# Create a frame to hold the radio buttons
radio_frame = tk.Frame(tab1)
radio_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Create the "Solo" radio button
solo_radio = tk.Radiobutton(radio_frame, text="Solo", variable=selected_option, value=1, width=5)
solo_radio.grid(row=0, column=0, padx=(0, 10), sticky="w")
solo_radio.select()

# Create the "Rally" radio button
rally_radio = tk.Radiobutton(radio_frame, text="Rally", variable=selected_option, value=2, width=5)
rally_radio.grid(row=0, column=1, padx=(0, 10), sticky="w")


# Create a new group of checkboxes for "Ymir" and "Cerberus" in the "Setting" tab
ymir_cerberus_frame = tk.Frame(tab1, relief="groove", borderwidth=2)
ymir_cerberus_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Create lists to hold Ymir and Cerberus checkboxes
ymir_checkboxes = []
cerberus_checkboxes = []

# Create a "Check All" checkbox for Ymir
ymir_check_all_var = tk.IntVar()
ymir_check_all_var.set(0)  # Initialize the "Check All" checkbox to unchecked

# Function to check/uncheck all Ymir checkboxes
def check_all_ymir():
    all_checked = all(var.get() == 1 for var in ymir_checkboxes)
    new_state = 0 if all_checked else 1  # Toggle the state
    ymir_check_all_var.set(new_state)  # Update the "Check All" checkbox state
    for var in ymir_checkboxes:
        var.set(new_state)  # Set all items to the new state

ymir_check_all_checkbox = tk.Checkbutton(ymir_cerberus_frame, text="Check All (Ymir)", variable=ymir_check_all_var, command=check_all_ymir)
ymir_check_all_checkbox.grid(row=0, column=0, sticky="w")

# Create Ymir checkboxes in a horizontal layout
for i in range(6):
    var = tk.IntVar()
    ymir_checkboxes.append(var)
    checkbox = tk.Checkbutton(ymir_cerberus_frame, text=f"Ymir {i + 1}", variable=var)
    checkbox.grid(row=i+1, column=0, sticky="w")

# Create a "Check All" checkbox for Cerberus
cerberus_check_all_var = tk.IntVar()
cerberus_check_all_var.set(0)  # Initialize the "Check All" checkbox to unchecked

# Function to check/uncheck all Cerberus checkboxes
def check_all_cerberus():
    all_checked = all(var.get() == 1 for var in cerberus_checkboxes)
    new_state = 0 if all_checked else 1  # Toggle the state
    cerberus_check_all_var.set(new_state)  # Update the "Check All" checkbox state
    for var in cerberus_checkboxes:
        var.set(new_state)  # Set all items to the new state

cerberus_check_all_checkbox = tk.Checkbutton(ymir_cerberus_frame, text="Check All (Cerberus)", variable=cerberus_check_all_var, command=check_all_cerberus)
cerberus_check_all_checkbox.grid(row=0, column=1, sticky="w")

# Create Cerberus checkboxes in a horizontal layout
for i in range(4):
    var = tk.IntVar()
    cerberus_checkboxes.append(var)
    checkbox = tk.Checkbutton(ymir_cerberus_frame, text=f"Cerberus {i + 1}", variable=var)
    checkbox.grid(row=i+1, column=1, sticky="w")



# Create "Start" button with a specified height
start_button = create_button(group_frame3, "Start", 1, 2, width=10, height=1, fg="blue", font=("Helvetica", 14))
start_button.config(command=start_button_click)

# Create "Stop" button with a specified height and initially disabled
stop_button = create_button(group_frame3, "Stop", 1, 3, width=10, height=1, fg="red", font=("Helvetica", 14))
stop_button.config(state="disabled")
stop_button.config(command=stop_button_click)

# Create "Save" button with a specified height
save_button = create_button(group_frame3, "Save", 1, 1, width=10, height=1, font=("Helvetica", 14))

# Configure grid column and row weights to make the groups and buttons expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)  # Group 2 is four times wider
root.grid_rowconfigure(0, weight=1)

root.mainloop()