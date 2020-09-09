# import datetime
# from plyer import notification
# print("sexy leone")

# today = datetime.datetime.now().strftime("%d-%m-%y")
# Year = datetime.datetime.now().strftime("%y")
# print(today)
# print(Year)

# if __name__ == "__main__":
#     notification.notify(
#         title="Time to Have sex",
#         message="its better to have sex than to seleep",
#         app_icon="/Users/tarushj.reddy/Desktop/Water/pngfuel.com-19.png",
#         timeout=3
#     )

'''this is an example system '''
# import os


# def notify(title, text):
#     os.system("""
#             osascript -e 'display notification "{Thsis jcsdojcosd}" with title "{}" sound name
#             {}'""".format(text, title))


# notify("Title", "Heres an alert")
import pync
import os
from pync import Notifier
pync.notify('Hello World')
# pync.notify('Hello World', title='Python')
# pync.notify('Hello World', group=os.getpid())
# pync.notify('Hello World', activate='com.apple.Safari')
# pync.notify('Hello World', open='http://github.com/')
# pync.notify('Hello World', execute='say "OMG"')


Notifier.remove(os.getpid())

Notifier.list(os.getpid())
