import tkinter as tk
from tkinter import messagebox, font
import pyperclip

class SelectionBox:
    def __init__(self, root):
        self.root = root
        self.rect_start = None
        self.rect_end = None
        self.rectangle = None
        self.coord_font = font.Font(family='Helvetica', size=14, weight='bold')
        self.coord_label = tk.Label(root.canvas, bg='black', fg='dodgerblue', font=self.coord_font)

    def start_rect(self, event):
        self.rect_start = (event.x, event.y)

    def draw_rect(self, event):
        # Delete previous rectangle
        if self.rectangle:
            self.root.canvas.delete(self.rectangle)

        self.rect_end = (event.x, event.y)
        self.rectangle = self.root.canvas.create_rectangle(self.rect_start[0], self.rect_start[1], 
                                                           self.rect_end[0], self.rect_end[1], outline='dodgerblue', fill='white', stipple='gray50')

        # Update and display coordinates
        coords_text = f"{event.x},{event.y}"
        self.coord_label.config(text=coords_text)
        # Calculate center considering the label size
        label_width = self.coord_label.winfo_reqwidth()
        label_height = self.coord_label.winfo_reqheight()
        center_x = (self.rect_start[0] + self.rect_end[0]) // 2 - label_width // 2
        center_y = (self.rect_start[1] + self.rect_end[1]) // 2 - label_height // 2
        self.coord_label.place(x=center_x, y=center_y)

    def end_rect(self, event):
        # Ask user if they want to save current selection or redraw
        if messagebox.askyesno("Confirm selection", "Would you like to save this selection?"):
            if self.rect_start and self.rect_end:
                start_x, start_y = self.rect_start
                end_x, end_y = self.rect_end
                width = end_x - start_x
                height = end_y - start_y
                coords = f"start_x: {start_x}, start_y: {start_y}, width: {width}, height: {height}"
                # Copy coords to clipboard
                pyperclip.copy(coords)
                messagebox.showinfo("Coordinates Copied", "Coordinates have been copied to clipboard.")
                print(coords)
                self.root.master.quit()
        else:
            # Remove current rectangle
            self.root.canvas.delete(self.rectangle)
            self.coord_label.config(text="")

class PyCoordApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.canvas = tk.Canvas(self.master, bg='black', bd=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.gui = SelectionBox(self)
        self.canvas.bind('<Button-1>', self.gui.start_rect)
        self.canvas.bind('<B1-Motion>', self.gui.draw_rect)
        self.canvas.bind('<ButtonRelease-1>', self.gui.end_rect)

    def run(self):
        self.master.mainloop()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.wait_visibility(root)
root.wm_attributes('-alpha',0.7)
app = PyCoordApp(root)
app.run()
