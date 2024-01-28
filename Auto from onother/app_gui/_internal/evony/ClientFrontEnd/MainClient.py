import tkinter as tk
from tkinter import ttk
import subprocess

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
root.title("Evony Auto")

# Set the width and height of the main window
window_width = 1200
window_height = 600
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
# option solo or rally
tab_control.add(tab1, text=" Setting")
tab_control.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Create "Start" button with a specified height
start_button = create_button(group_frame3, "Start", 1, 2, width=10, height=1, fg="blue", font=("Helvetica", 14))
start_button.config(command=start_button_click)

# Create "Stop" button with a specified height and initially disabled
stop_button = create_button(group_frame3, "Stop", 1, 3, width=10, height=1, fg="red", font=("Helvetica", 14))
stop_button.config(state="disabled")
stop_button.config(command=stop_button_click)

# Create "Save" button with a specified height
save_button = create_button(group_frame3, "Save", 1, 1, width=10, height=1, font=("Helvetica", 14))

def toggle_preset_state(preset_var, preset_button):
    preset_button.config(state="normal" if preset_var.get() == 1 else "disabled")

# Function to open the DetailPreset window
def open_detail_preset_popup(preset_var):
    # preset_name = preset_var["text"]  # Get the text of the button
    # subprocess.Popen(["python", "DetailPresetClient.py", "--preset_name", preset_name])
    preset_name = preset_var.cget("text")  # Get the text of the button
    subprocess.Popen(["python", "DetailPresetClient.py", "--preset_name", preset_name])

# Create the "Preset 1" checkbox and button in Tab 1
preset1_var = tk.IntVar()
preset1_var.trace_add("write", lambda *args: toggle_preset_state(preset1_var, preset1_button))
preset1_checkbox = tk.Checkbutton(tab1, text="Use Preset 1", variable=preset1_var)
preset1_checkbox.grid(row=1, column=1, sticky="w")
preset1_button = tk.Button(tab1, text="Preset 1", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset1_button))
preset1_button.grid(row=2, column=1, padx=2, pady=2, sticky="w")

# Create the "Preset 2" checkbox and button in Tab 1
preset2_var = tk.IntVar()
preset2_var.trace_add("write", lambda *args: toggle_preset_state(preset2_var, preset2_button))
preset2_checkbox = tk.Checkbutton(tab1, text="Use Preset 2", variable=preset2_var)
preset2_checkbox.grid(row=1, column=2, sticky="w")
preset2_button = tk.Button(tab1, text="Preset 2", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset2_button))
preset2_button.grid(row=2, column=2, padx=2, pady=2, sticky="w")

# Create the "Preset 3" checkbox and button in Tab 1
preset3_var = tk.IntVar()
preset3_var.trace_add("write", lambda *args: toggle_preset_state(preset3_var, preset3_button))
preset3_checkbox = tk.Checkbutton(tab1, text="Use Preset 3", variable=preset3_var)
preset3_checkbox.grid(row=1, column=3, sticky="w")
preset3_button = tk.Button(tab1, text="Preset 3", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset3_button))
preset3_button.grid(row=2, column=3, padx=2, pady=2, sticky="w")

# Create the "Preset 4" checkbox and button in Tab 1
preset4_var = tk.IntVar()
preset4_var.trace_add("write", lambda *args: toggle_preset_state(preset4_var, preset4_button))
preset4_checkbox = tk.Checkbutton(tab1, text="Use Preset 4", variable=preset4_var)
preset4_checkbox.grid(row=1, column=4, sticky="w")
preset4_button = tk.Button(tab1, text="Preset 4", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset4_button))
preset4_button.grid(row=2, column=4, padx=2, pady=2, sticky="w")


# Create the "Preset 5" checkbox and button in Tab 1
preset5_var = tk.IntVar()
preset5_var.trace_add("write", lambda *args: toggle_preset_state(preset5_var, preset5_button))
preset5_checkbox = tk.Checkbutton(tab1, text="Use Preset 5", variable=preset5_var)
preset5_checkbox.grid(row=1, column=5, sticky="w")
preset5_button = tk.Button(tab1, text="Preset 5", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset5_button))
preset5_button.grid(row=2, column=5, padx=2, pady=2, sticky="w")

# Create the "Preset 6" checkbox and button in Tab 1
preset6_var = tk.IntVar()
preset6_var.trace_add("write", lambda *args: toggle_preset_state(preset6_var, preset6_button))
preset6_checkbox = tk.Checkbutton(tab1, text="Use Preset 6", variable=preset6_var)
preset6_checkbox.grid(row=1, column=6, sticky="w")
preset6_button = tk.Button(tab1, text="Preset 6", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset6_button))
preset6_button.grid(row=2, column=6, padx=2, pady=2, sticky="w")

# Create the "Preset 7" checkbox and button in Tab 1
preset7_var = tk.IntVar()
preset7_var.trace_add("write", lambda *args: toggle_preset_state(preset7_var, preset7_button))
preset7_checkbox = tk.Checkbutton(tab1, text="Use Preset 7", variable=preset7_var)
preset7_checkbox.grid(row=1, column=7, sticky="w")
preset7_button = tk.Button(tab1, text="Preset 7", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset7_button))
preset7_button.grid(row=2, column=7, padx=2, pady=2, sticky="w")

# Create the "Preset 8" checkbox and button in Tab 1
preset8_var = tk.IntVar()
preset8_var.trace_add("write", lambda *args: toggle_preset_state(preset8_var, preset8_button))
preset8_checkbox = tk.Checkbutton(tab1, text="Use Preset 8", variable=preset8_var)
preset8_checkbox.grid(row=1, column=8, sticky="w")
preset8_button = tk.Button(tab1, text="Preset 8", width=10, height=1, fg="blue", font=("Helvetica", 10), state="disabled", command=lambda: open_detail_preset_popup(preset8_button))
preset8_button.grid(row=2, column=8, padx=2, pady=2, sticky="w")

# Configure grid column and row weights to make the groups and buttons expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)  # Group 2 is four times wider
root.grid_rowconfigure(0, weight=1)

root.mainloop()