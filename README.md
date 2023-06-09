# PyCoord
PyCoord is a Python-based utility that allows users to select a rectangular region on their screen and automatically copies the coordinates of the selected region to the clipboard. It provides a GUI which makes it easy and intuitive to select areas directly on the screen.

![](https://i.imgur.com/WQcwRF8.gif)

# Features
- Fullscreen Overlay: PyCoord overlays a transparent layer on the entire screen, allowing users to select areas directly.

- Live Coordinate Display: As users create the selection box, the coordinates of the box are updated and displayed live at the center of the box.

- Interactive Confirmation: After a selection is made, users are prompted to confirm if they want to save the selection or redraw the box.

- Automatic Copy to Clipboard: Upon confirmation, the coordinates of the selection are automatically copied to the system clipboard for easy pasting and use in other applications. Users are also notified of this via a popup message.

- Lightweight and Easy to Use: PyCoord is easy to run and doesn't require any complicated setup or configuration. It's a simple and effective tool for grabbing screen coordinates quickly.

# Requirements
PyCoord requires **Python 3.1 or later**, which includes **tkinter** as part of the standard library.

Additional dependencies are listed in the ***requirements.txt*** file and can be installed with pip using the following command:
```
pip install -r requirements.txt
```
**Here are the main dependencies:**

- **tkinter**: A Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit and is included with Python as a standard library.

- **pyperclip**: A cross-platform Python module for copy and paste clipboard functions. This module is used to copy the coordinates of the selected area to the clipboard for easy use in other applications.

# Usage
To use PyCoord, simply clone the repository and run the pycoord.py script. Draw a box on the screen by clicking and dragging the mouse. Upon release, confirm your selection to have the coordinates automatically copied to your clipboard.
