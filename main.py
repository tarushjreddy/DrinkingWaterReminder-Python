# # import datetime
from plyer import notification


# # today = datetime.datetime.now().strftime("%d-%m-%y")
# # Year = datetime.datetime.now().strftime("%y")
# # print(today)
# # print(Year)

# # if __name__ == "__main__":
# #     notification.notify(
# #         title="Time to Have ",
# #         message="its better to have  than to seleep",
# #         app_icon="/Users/tarushj.reddy/Desktop/Water/pngfuel.com-19.png",
# #         timeout=3
# #     )

# '''this is an example system '''
# # import os


# # def notify(title, text):
# #     os.system("""
# #             osascript -e 'display notification "{Thsis jcsdojcosd}" with title "{}" sound name
# #             {}'""".format(text, title))


# # notify("Title", "Heres an alert")
import pync
import time
import os
from pync import Notifier
import datetime

operatingsystem = input(
    "PRESS W if you are using Windows and U if your using Apple, linux or Unix based operating system\n\n")

today = datetime.datetime.now().strftime("%H")
minutes = datetime.datetime.now().strftime("%M")
seconds = datetime.datetime.now().strftime("%S")
Year = datetime.datetime.now().strftime("%y")

print("The current time is "+f"{int(today)}" +
      ":"+minutes + ":"+seconds + "\n")
# print(Year)
water = input("Enter the when to remind you to drink water after every:\n")
print(f"You will be reminded after {water} hours to drink water\n")
waterr = str(int(water) + int(today))

# print(int(waterr))
# if(today == waterr):
#     print("omsairam")
d = ''
if(int(waterr) == 25) or (int(waterr) > 25):
    d = int(waterr) - 24
    waterr == d

# print(waterr)

if(int(waterr) == int(today)):

    if(operatingsystem == "U"):
        if __name__ == "__main__":
            pync.notify('It is so important to stay hydrated during our day, not only to replenish the water that we lose throughout the day, but drinking more water can aid in weight loss, manage diabetes, essential in pregnancy and also keeps your teeth, skin and gums healthy.',
                        title=f"Time to drink water its already {today}:{minutes}:{seconds} ",
                        activate='com.apple.Safari',
                        subtitle="Sip before every meal.",
                        open='http://github.com/',
                        execute='say "ok but do not forget to drink water"',

                        icon='pngfuel.com-19.png',
                        timeout=1
                        )
    elif(operatingsystem == "W"):
        if __name__ == "__main__":
            notification.notify(
                title=f"Time to drink water its already {today}:{minutes}:{seconds} ",
                message='It is so important to stay hydrated during our day, not only to replenish the water that we lose throughout the day, but drinking more water can aid in weight loss, manage diabetes, essential in pregnancy and also keeps your teeth, skin and gums healthy.',
                app_icon='pngfuel.com-19.png',
                timeout=3
            )

elif(int(waterr) > int(today)):
    time.sleep(int(waterr)*60*60)
    if(operatingsystem == "U"):
        if __name__ == "__main__":
            pync.notify('It is so important to stay hydrated during our day, not only to replenish the water that we lose throughout the day, but drinking more water can aid in weight loss, manage diabetes, essential in pregnancy and also keeps your teeth, skin and gums healthy.',
                        title=f"Time to drink water its already {today}:{minutes}:{seconds} ",
                        activate='com.apple.Safari',
                        subtitle="Sip before every meal.",
                        open='http://github.com/',
                        execute='say "ok but do not forget to drink water"',

                        icon='pngfuel.com-19.png',
                        timeout=1
                        )

    elif(operatingsystem == "W"):
        time.sleep(int(water)*60*60)
        if __name__ == "__main__":
            notification.notify(
                title=f"Time to drink water its already {today}:{minutes}:{seconds} ",
                message='It is so important to stay hydrated during our day, not only to replenish the water that we lose throughout the day, but drinking more water can aid in weight loss, manage diabetes, essential in pregnancy and also keeps your teeth, skin and gums healthy.',
                app_icon='pngfuel.com-19.png',
                timeout=3
            )

    # if __name__ == "__main__":
    #     pync.notify('Hello World',
    #                 title="Omsai",
    #                 subtitle="hello this is developer king pro",

    #                 icon='pngfuel.com-19.png',
    #                 )


# pync.notify('Hello World', title='Python')
# pync.notify('Hello World', group=os.getpid())
# pync.notify('Hello World', activate='com.apple.Safari')
# pync.notify('Hello World', open='http://github.com/')
# pync.notify('Hello World', execute='say "OMG"')

'''
Notifier.remove(os.getpid())

Notifier.list(os.getpid())
'''
# d = input("enter the number\n")
# # print(type
# #       (d))
# numm = int(d)
# # print(type(numm))
# one = (numm * (numm + 1))
# print(one/2)
# a = str(0)
# print(a)
