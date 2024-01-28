import tkinter as tk
import json
from tkinter import messagebox
import argparse
import os

# Create a command-line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--preset_name", type=str, help="The preset name")

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the --preset_name argument
preset_name = args.preset_name

def create_checkbox_group(root, group_frame, num_checkboxes=10, label_text="Preset", checkbox_texts=None):
    checkboxes_group = []

    group_label = tk.Label(group_frame, text=label_text, anchor="w")
    group_label.grid(row=0, column=0, columnspan=2, sticky="w")  # Align label to the left

    check_all_button = tk.Button(group_frame, text="Check All")
    check_all_button.grid(row=1, column=0, sticky="w")
    check_all_button.config(command=lambda button=check_all_button: toggle_check_all(button, checkboxes_group))

    if checkbox_texts is None:
        checkbox_texts = [f"Checkbox {i + 1}" for i in range(num_checkboxes)]

    for i, checkbox_text in enumerate(checkbox_texts):
        var = tk.IntVar()
        checkboxes_group.append((var, checkbox_text))  # Store both the variable and text
        checkbox = tk.Checkbutton(group_frame, text=checkbox_text, variable=var, width=20, anchor="w")
        checkbox.grid(row=i + 2, column=0, sticky="w")  # Align checkboxes to the left

    return checkboxes_group


def create_button(root, text, row, column, width=None, height=None, fg=None, font=None):
    button = tk.Button(root, text=text, width=width, height=height, padx=2, pady=2, fg=fg, font=font)
    button.grid(row=row, column=column, padx=2, pady=2)
    return button

def toggle_check_all(button, checkboxes_group):
    if any(var_text[0].get() == 0 for var_text in checkboxes_group):
        for var_text in checkboxes_group:
            var_text[0].set(1)
        button.config(text="Uncheck All")
    else:
        for var_text in checkboxes_group:
            var_text[0].set(0)
        button.config(text="Check All")



root = tk.Tk()
root.title("Preset Detail")

window_width = 985
window_height = 600
root.geometry(f"{window_width}x{window_height}")

main_frame = tk.Frame(root, relief="groove", borderwidth=2)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Create and configure radio buttons inside a frame
radio_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
radio_frame.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
# radio_frame.grid_propagate(False)  # Disable frame propagation

var = tk.StringVar()
solo_radio = tk.Radiobutton(radio_frame, text="Solo", variable=var, value="Solo")
rally_radio = tk.Radiobutton(radio_frame, text="Rally", variable=var, value="Rally")
solo_radio.grid(row=0, column=0, sticky="w")
rally_radio.grid(row=0, column=1, sticky="w")
var.set("Solo")  # Set the default selected radio button


ymir_checkbox_texts = ["Ymir 1", "Ymir 2", "Ymir 3", "Ymir 4", "Ymir 5", "Ymir 6"]
cerberus_checkbox_texts = ["Cerberus 1", "Cerberus 2", "Cerberus 3", "Cerberus 4"]
warlord_checkbox_texts = ["Warlord 1", "Warlord 2", "Warlord 3", "Warlord 4", "Warlord 5", "Warlord 6"]
witch_checkbox_texts = ["Witch 1", "Witch 2", "Witch 3", "Witch 4","Witch 5", "Witch 6"]
hydra_checkbox_texts = ["Hydra 1", "Hydra 2", "Hydra 3", "Hydra 4", "Hydra 5"]
sphinx_checkbox_texts = ["Sphinx 1", "Sphinx 2", "Sphinx 3", "Sphinx 4","Sphinx 5", "Sphinx 6"]
bayard_checkbox_texts = ["Bayard 1", "Bayard 2", "Bayard 3", "Bayard 4"]

# Create and configure Ymir checkbox frame
ymir_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
ymir_checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create and configure Cerberus checkbox frame
cerberus_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
cerberus_checkbox_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Create and configure Warlord checkbox frame
warlord_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
warlord_checkbox_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Create and configure Witch checkbox frame
witch_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
witch_checkbox_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

# Create and configure Hydra checkbox frame
hydra_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
hydra_checkbox_frame.grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

# Create and configure sphinx checkbox frame
sphinx_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
sphinx_checkbox_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Create and configure bayard checkbox frame
bayard_checkbox_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
bayard_checkbox_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Create Ymir checkboxes
ymir_checkbox = create_checkbox_group(root, ymir_checkbox_frame, num_checkboxes=6, label_text="Ymir", checkbox_texts=ymir_checkbox_texts)

# Create Cerberus checkboxes
cerberus_checkbox = create_checkbox_group(root, cerberus_checkbox_frame, num_checkboxes=4, label_text="Cerberus", checkbox_texts=cerberus_checkbox_texts)

# Create Warlord checkboxes
warlord_checkbox = create_checkbox_group(root, warlord_checkbox_frame, num_checkboxes=4, label_text="Warlord", checkbox_texts=warlord_checkbox_texts)

# Create Witch checkboxes
witch_checkbox = create_checkbox_group(root, witch_checkbox_frame, num_checkboxes=4, label_text="Witch", checkbox_texts=witch_checkbox_texts)

# Create Hydra checkboxes
hydra_checkbox = create_checkbox_group(root, hydra_checkbox_frame, num_checkboxes=4, label_text="Hydra", checkbox_texts=hydra_checkbox_texts)

# Create Hydra checkboxes
sphinx_checkbox = create_checkbox_group(root, sphinx_checkbox_frame, num_checkboxes=4, label_text="Sphinx", checkbox_texts=sphinx_checkbox_texts)

# Create Hydra checkboxes
bayard_checkbox = create_checkbox_group(root, bayard_checkbox_frame, num_checkboxes=4, label_text="Bayard", checkbox_texts=bayard_checkbox_texts)


def save_to_json(checkbox_groups, checkbox_group_names):
    data = {
        preset_name: {
            "bosses": [],
            "mode": var.get(),
            "priority": 1,
            "active": True
        }
    }
    # Specify the directory path
    directory = 'config'
    # Create the directory if it doesn't exist
    if not os.path.exists(f'../{directory}'):
        os.makedirs(f'../{directory}')

    # Save the state of each checkbox group
    selected_items =[]
    for group, group_name in zip(checkbox_groups, checkbox_group_names):
        selected_items.append([text for var, text in group if var.get() == 1])
        data[preset_name]["bosses"] = [item for sublist in selected_items for item in sublist]

    file_name = preset_name.replace('Preset ', 'Preset_')
    # Save the data to a JSON file
    # Now, you can safely open and write to the file
    with open(f'../{directory}/{file_name}.json', 'w') as file:
        # Write your data to the file
        json.dump(data, file)

def save_callback():
    checkbox_groups = [ymir_checkbox, cerberus_checkbox, warlord_checkbox, witch_checkbox, hydra_checkbox,
                       sphinx_checkbox, bayard_checkbox]
    checkbox_group_names = ["Ymir", "Cerberus", "Warlord", "Witch", "Hydra", "Sphinx", "Bayard"]
    save_to_json(checkbox_groups, checkbox_group_names)
    messagebox.showinfo("Success", "Data saved successfully!")

# Create "Save" button
# save_button = create_button(root, "Save", 1, 0, width=10, height=1, font=("Helvetica", 14), command=save_callback)
save_button = create_button(root, "Save", 1, 0, width=10, height=1, font=("Helvetica", 14))
save_button.config(command=save_callback)


root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4, uniform="group_frame")

root.mainloop()