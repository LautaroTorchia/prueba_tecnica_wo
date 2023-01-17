from datetime import datetime

class Alert:
    def __init__(self,text,user,topic,expiration_date):
        self.text=text
        self.user=user
        self.date=datetime.now()
        self.topic=topic
        self.read=False
        self.expiration_date=expiration_date    #datetime field
        
    def send_alert(self):
        pass  #polimorfic method
    
    def mark_as_read(self):
        self.read=True
    
    def __str__(self) -> str:
        return f"Alert for {self.user} about {self.topic}"