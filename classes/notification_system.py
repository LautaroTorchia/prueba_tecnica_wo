from classes.urgent_alert import UrgentAlert
from classes.informative_alert import InformativeAlert
from datetime import datetime,timedelta
from classes.user import User
from classes.topic import Topic


class NotificationSystem:
    def __init__(self):
        self.users = set()
        self.topics = set()
    
    def register_user(self,name,email):
        user=User(name,email)
        self.users.add(user)
        return user
    
    def register_topic(self, title,description):
        topic=Topic(title,description)
        self.topics.add(topic)
        return topic
    
    def send_urgent_alert(self, text,topic, reciever=None, expiration_date=datetime.now()+timedelta(days=7)):
        if reciever:
            UrgentAlert(text,reciever,topic,expiration_date).send_alert()
        else:
            reciever = self.users
            for user in reciever:
                UrgentAlert(text,user,topic,expiration_date).send_alert()
            
        
    def send_informative_alert(self, text,topic,reciever=None,expiration_date=datetime.now()+timedelta(days=7)):
        if reciever:
            InformativeAlert(text,reciever,topic,expiration_date).send_alert()
        else:
            reciever = self.users
            for user in reciever:
                InformativeAlert(text,user,topic,expiration_date).send_alert()


    def get_topics(self):
        return self.topics
    
    def get_users(self):
        return self.users

    def __str__(self) -> str:
        return "Notification System"