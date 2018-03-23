from PIL import ImageDraw
from PIL import ImageFont
from appJar import gui
from PIL import Image, ImageTk
from threading import Thread

from digitalframe.mail import Inbox

import time
import glob
import random


class DigitalFrameApp:
    def __init__(self, configuration, full_screen=False):
        self.config = configuration.data['config']
        self.full_screen = full_screen
        self.app = gui()
        self.current_picture = False
        self.check_mails_thread = Thread(name='check_mail_thread', target=self.check_mails).start()
        self.select_image_thread = Thread(name='select_image_thread', target=self.select_image).start()

    def check_mails(self):
        while True:
            print("Sprawdzam maile")
            mail = Inbox(self.config['mail_host'], self.config['mail_username'], self.config['mail_password'], 993)
            mail.check_mails()
            time.sleep(30)

    def select_image(self):
        while True:
            images = glob.glob('data/*.JPG')

            if len(images) == 0:
                print("Nie znalazłem zdjec... Sprobuje za 60 sekund...")
                time.sleep(60)
                continue

            selected_image = random.choice(images)

            print(selected_image)

            photo = Image.open(selected_image)
            photo.thumbnail((800, 480), Image.ANTIALIAS)

            draw = ImageDraw.Draw(photo)
            font = ImageFont.truetype('./Arial.ttf', size=23)

            with open(selected_image + '.txt', 'r') as text_file:
                text = text_file.read()
                w, h = draw.textsize(text, font=font)
                draw.text(((photo.width - w) / 2, 440), text, (255, 255, 0), font=font)

            photo = ImageTk.PhotoImage(photo)

            if not self.current_picture:
                self.app.addImageData("pic", photo, fmt="PhotoImage")

                self.current_picture = True
            else:
                self.app.setImageData("pic", photo, fmt="PhotoImage")

            # self.app.addLabel("title", "Welcome to appJar")

            time.sleep(5)

    def run(self):
        if self.full_screen:
            self.app.fullscreen = True
            # self.app.hideTitleBar()
            self.app.hideToolbar()

        self.app.go()