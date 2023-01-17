from datetime import datetime

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.topics= set()
        self.alerts= []
    
    def create_topic_notification(self, topic):
        self.topics.add(topic)
    
    def add_alert(self, alert):
        self.alerts.append(alert)
        
    def can_can_recieve_from_topic(self, topic):
        return topic in self.topics
    
    def unread_alerts(self):
        unread_alerts=list(filter(lambda alert: alert.read == False and alert.expiration_date > datetime.now(), self.alerts))
        unread_alerts.sort(key=lambda alert: alert.date, reverse=True) #descending order
        return unread_alerts
    
    def mark_as_read(self, alert): #the alert recieved is the alert the user clicked on in the page
        alert.mark_as_read()
    
    def __str__(self) -> str:
        return self.name
    