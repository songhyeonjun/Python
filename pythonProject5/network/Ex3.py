from tkinter import *
from tkinter.ttk import *
import random
import time
import threading


# 클래스 선언 부분
class ThreadProgressBar():
    thread = None
    progress = None

    def __init__(self, parent):
        self.progress = Progressbar(parent, orient=HORIZONTAL, length=500)
        self.progress.pack(side=TOP, fill=x, ipadx=10, ipady=10, padx=10, pady=10)
        self.thread = threading.Thread(target=self.runProgress, args = (self.progress,))
        self.thread.start()

    def runProgress(self, progress):
