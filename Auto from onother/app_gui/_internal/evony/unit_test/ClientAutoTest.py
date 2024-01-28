import tkinter as tk

def get_selected_checkboxes():
    selected_values = [text_var[checkbox] for checkbox in checkboxes if checkbox_var[checkbox].get() == 1]
    print("Selected Checkboxes:", selected_values)

root = tk.Tk()
root.title("Checkbox Example")

# Create a dictionary to store the IntVar for each checkbox
checkbox_var = {}

# Create a dictionary to store the text for each checkbox
text_var = {}

# Create a list of checkbox widgets
checkboxes = []

# Create and add checkboxes to the dictionary and list
for i in range(1, 6):
    var = tk.IntVar()
    text = f"Checkbox {i}"
    checkbox_var[text] = var
    text_var[text] = text  # Fix: Store text in text_var dictionary
    checkbox = tk.Checkbutton(root, text=text, variable=var)
    checkboxes.append(checkbox)
    checkbox.pack()

# Create a button to get the selected checkboxes
get_value_button = tk.Button(root, text="Get Selected Checkboxes", command=get_selected_checkboxes)
get_value_button.pack()

root.mainloop()