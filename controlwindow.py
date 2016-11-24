import threading
from server import Server
import rule
import bta3

class Controlwindow:
    """will hold the bluetooth serch class, back ground server and have an array of running rules,
    will take result from the search check it for changes then pass the change to all rule threads.
    will only make the search thread itself, all other threads will be made in main and passed to this class to manage."""
    backserver = None

