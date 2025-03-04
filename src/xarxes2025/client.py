import sys 

from tkinter import Tk, Label, Button, W, E, N, S
from tkinter import messagebox
import tkinter as tk


from loguru import logger

from PIL import Image, ImageTk
import io

class Client(object):
    def __init__(self, port):       
        """
        Initialize a new VideoStreaming client.

        :param port: The port to connect to.
        :param filename: The filename to ask for to connect to.
        """

        
    def __init__(self, server_port, filename):
        logger.debug(f"Client created ")
        self.server_port = server_port
        self.create_ui()

        
    def create_ui(self):
        """
        Create the user interface for the client.

        This function creates the window for the client and its
        buttons and labels. It also sets up the window to call the
        close window function when the window is closed.

        :returns: The root of the window.
        """
        self.root = Tk()

        # Set the window title
        self.root.wm_title("RTP Client")

        # On closing window go to close window function
        self.root.protocol("WM_DELETE_WINDOW", self.ui_close_window)


		# Create Buttons
        self.setup = self._create_button("Setup", self.ui_setup_event, 0, 0)
        # self.start = self._create_button("Play", self.ui_play_event, 0, 1)
        # self.pause = self._create_button("Pause", self.ui_pause_event, 0, 2)
        # self.teardown = self._create_button("Teardown", self.ui_teardown_event, 0, 3)

        # Create a label to display the movie
        self.movie = Label(self.root, height=29)
        self.movie.grid(row=1, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5) 

        # Create a label to display text messages
        self.text = Label(self.root, height=3)
        self.text.grid(row=2, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5) 

        return self.root
    
    def _create_button(self, text, command, row=0, column=0, width=20, padx=3, pady=3 ):
        """
        Create a button widget with the given text, command, and layout options.

        :param str text: The text to display on the button.
        :param callable command: The function to call when the button is clicked.
        :param int row: The row number of the button in the grid.
        :param int column: The column number of the button in the grid.
        :param int width: The width of the button.
        :param int padx: The horizontal padding of the button.
        :param int pady: The vertical padding of the button.
        :return: The button widget.
        """
        button = Button(self.root, width=width, padx=padx, pady=pady)
        button["text"] = text
        button["command"] = command
        button.grid(row=row, column=column, padx=2, pady=2)
        return button
    
    
    def ui_close_window(self):
        """
        Close the window.
        """
        self.root.destroy()
        logger.debug("Window closed")
        sys.exit(0)


    def ui_setup_event(self):
        """
        Handle the Setup button click event.
        """
        logger.debug("Setup button clicked")
        self.text["text"] = "Setup button clicked"
        self.updateMovie(None)


    def updateMovie(self, data):
        """Update the video frame in the GUI from the byte buffer we received."""

        # data hauria de tenir el payload de la imatge extreta del paquet RTP
        # Com no en teniu, encara, us poso un exemple de com carregar una imatge
        # des del disc dur. Això ho haureu de canviar per carregar la imatge
        # des del buffer de bytes que rebem del servidor.
        # photo = ImageTk.PhotoImage(Image.open(io.BytesIO(data)))


        photo = ImageTk.PhotoImage(Image.open('rick.webp'))
        self.movie.configure(image = photo, height=380) 
        self.movie.photo_image = photo
