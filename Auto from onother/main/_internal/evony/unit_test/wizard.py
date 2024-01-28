#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        frame1 = ttk.Frame(master)
        frame1.configure(height=400, width=600)
        self.port_label = ttk.Label(frame1)
        self.port_label.configure(
            font="{Cambria} 12 {}",
            padding=5,
            text='Port Number')
        self.port_label.grid(column=0, row=0)
        self.port_number = ttk.Entry(frame1)
        self.port_number.configure(width=20)
        self.port_number.grid(column=1, row=0)
        self.city_coords = ttk.Label(frame1)
        self.city_coords.configure(
            font="{Cambria} 12 {}",
            padding=5,
            relief="flat",
            text='City Coords')
        self.city_coords.grid(column=0, row=1)
        self.x = ttk.Entry(frame1)
        self.x.configure(width=5)
        self.x.grid(
            column=1,
            columnspan=2,
            padx=0,
            row=1,
            rowspan=1,
            sticky="w")
        self.y = ttk.Entry(frame1)
        self.y.configure(font="TkTextFont", state="normal", width=5)
        self.y.grid(column=1, columnspan=1, padx=50, row=1, rowspan=2)
        self.preset_1 = ttk.Button(frame1)
        self.preset_1.configure(state="normal", text='Preset 1')
        self.preset_1.grid(
            column=0,
            columnspan=1,
            ipadx=0,
            pady=20,
            row=3,
            sticky="w")
        frame1.grid(column=0, row=0)

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()

