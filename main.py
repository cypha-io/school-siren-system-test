import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pickle

class BellScheduleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # set window properties
        self.title("Bell Schedule App")
        self.geometry("400x400")
        self.resizable(False, False)
        
        # create login screen
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(expand=True)
        tk.Label(self.login_frame, text="Username: ").grid(row=0, column=0)
        tk.Entry(self.login_frame).grid(row=0, column=1)
        tk.Label(self.login_frame, text="Password: ").grid(row=1, column=0)
        tk.Entry(self.login_frame, show="*").grid(row=1, column=1)
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=1)

    def login(self):
        # handle login here
        # if successful, show main window
        self.login_frame.pack_forget()
        self.create_main_window()

    def create_main_window(self):
        # create main window
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True)
        
        # display current bell schedule
        tk.Label(self.main_frame, text="Current Bell Schedule:").grid(row=0, column=0)
        self.schedule_label = tk.Label(self.main_frame, text="")
        self.schedule_label.grid(row=1, column=0)

        # add button to add new bell
        tk.Button(self.main_frame, text="Add Bell", command=self.add_bell).grid(row=2, column=0)

        # add button to save schedule
        tk.Button(self.main_frame, text="Save Schedule", command=self.save_schedule).grid(row=3, column=0)

    def add_bell(self):
        # create form to add new bell
        self.add_bell_window = tk.Toplevel(self)
        self.add_bell_window.title("Add Bell")
        self.add_bell_window.geometry("300x150")
        tk.Label(self.add_bell_window, text="Start Time (hh:mm): ").grid(row=0, column=0)
        self.start_time_entry = tk.Entry(self.add_bell_window)
        self.start_time_entry.grid(row=0, column=1)
        tk.Label(self.add_bell_window, text="End Time (hh:mm): ").grid(row=1, column=0)
        self.end_time_entry = tk.Entry(self.add_bell_window)
        self.end_time_entry.grid(row=1, column=1)
        tk.Label(self.add_bell_window, text="Chime Sound: ").grid(row=2, column=0)
        self.chime_sound_entry = tk.Entry(self.add_bell_window)
        self.chime_sound_entry.grid(row=2, column=1)
        tk.Button(self.add_bell_window, text="Upload File", command=self.upload_file).grid(row=2, column=2)

        # add button to save new bell
        tk.Button(self.add_bell_window, text="Save Bell", command=self.save_bell).grid(row=3, column=1)

    def upload_file(self):
        # open file dialog to upload chime sound file
        self.chime_sound_file = filedialog.askopenfilename()

    def save_bell(self):
        # get input values and add new bell to schedule
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
