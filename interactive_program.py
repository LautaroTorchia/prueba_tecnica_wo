from time import sleep
from classes.notification_system import NotificationSystem
import random

center=NotificationSystem()
birthdays=center.register_topic("Birthdays", "This topic is about birthdays ")
cooking=center.register_topic("Cooking", "This topic is about cooking news")
sports=center.register_topic("Sports", "This topic is about sports news")
entertainment=center.register_topic("Entertainment", "This topic is about entertainment news")


print("This is the Notification System, please register yourself as a user")
name=input("Please enter your name: ")
email=input("Please enter your email: ")
your_user=center.register_user(name,email)
print("Welcome to the system, "+name)
print("Please select the number of the topic you want to subscribe to from the list below")

i=0
topics=list(center.get_topics())
for topic in topics:
    print(i+1,") "+topic.title + " - "+topic.description)
    i+=1

selection=int(input())
print("You have selected "+topics[selection-1].title+ " topic, now you can recieve alerts about this topic")
your_user.create_topic_notification(topics[selection-1])

value=""
iterations=0

while value!="exit":
    if iterations==3:
        center.send_urgent_alert(f"Aviso de alerta URGENTE",topics[random.randint(1,len(topics)-1)],your_user)
        iterations=0
    sleep(2)
    random_num=random.randint(1,len(topics)-1)
    center.send_informative_alert(f"Aviso de alerta {topics[selection-1].title}",topics[random_num],your_user)
    if len(your_user.unread_alerts())>0:
        print("This are your current unread alerts: ")
        for i in range (len(your_user.unread_alerts())):
            print(i+1,") "+ your_user.unread_alerts()[i].text)
        print("Please select the number of the alert you want to read or exit to exit")
        value=input()
        if value!="exit":
            value=int(value)
            your_user.mark_as_read(your_user.unread_alerts()[value-1])
            print("successfully read, please write exit to exit or anything else to continue")
    else:      
        print("You dont have unread alerts, please write exit to exit or anything else to continue")
    value=input()
    iterations+=1
    
    



