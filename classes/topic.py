from datetime import datetime 

class Topic:
    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.alerts=[]
    
    
    def add_alert(self,alert):
        self.alerts.append(alert)
    
    def get_unexpired_alerts(self):
        unexpired_topics=list(filter(lambda alert: alert.expiration_date > datetime.now(), self.alerts))
        unexpired_topics.sort(key=lambda alert: alert.date, reverse=True)
        return unexpired_topics
    
    def __str__(self) -> str:
        return self.title