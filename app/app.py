from appJar import gui
from PIL import Image, ImageTk
from threading import Thread

from app.mail import Inbox

import time
import glob
import random


class DigitalFrameApp:
    def __init__(self, full_screen=False):
        self.full_screen = full_screen
        self.app = gui()
        self.current_picture = False
        self.check_mails_thread = Thread(target=self.check_mails).start()
        self.select_image_thread = Thread(target=self.select_image).start()

    def check_mails(self):
        while True:
            print("Sprawdzam maile")
            mail = Inbox('imap.gmail.com', '', '', 993)
            mail.check_mails()
            time.sleep(30)

    def select_image(self):
        while True:
            images = glob.glob('*.JPG')

            selected_image = random.choice(images)

            print(selected_image)

            photo = Image.open(selected_image)
            photo.thumbnail((800, 480), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)

            if not self.current_picture:
                self.app.addImageData("pic", photo, fmt="PhotoImage")

                self.current_picture = True
            else:
                self.app.setImageData("pic", photo, fmt="PhotoImage")

            time.sleep(5)

    def run(self):
        self.app.addLabel("title", "Welcome to appJar")

        if self.full_screen:
            self.app.tk.attributes('-fullscreen', True)


        #
        #


        self.app.go()