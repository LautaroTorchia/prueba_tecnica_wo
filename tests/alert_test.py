
from classes.user import User
from classes.topic import Topic
from classes.informative_alert import InformativeAlert
from classes.urgent_alert import UrgentAlert
from datetime import datetime,timedelta


class TestAlert:

    user = User("Test User", "a@a.com")
    topic1=Topic("Test Topic 1", "Test Description 1")
    topic2=Topic("Test Topic 2", "Test Description 2")
    urgent_alert=UrgentAlert("birthday",user,topic1,datetime.now()-timedelta(days=1))
    informative_alert_not_recieved=InformativeAlert("birthday",user,topic1,datetime.now()+timedelta(days=2))
    informative_alert_recieved=InformativeAlert("birthday",user,topic2,datetime.now()+timedelta(days=2))
    user.topics.add(topic2)
    
    def test_mark_as_read(self):
        self.user.mark_as_read(self.urgent_alert)
        assert self.urgent_alert.read == True
    
    def test_send_urgent_alert(self):
        self.urgent_alert.send_alert()
        assert self.urgent_alert in self.user.alerts
    
    def test_send_informative_alert(self):
        respose_not_recieved=self.informative_alert_not_recieved.send_alert()
        response_recieved=self.informative_alert_recieved.send_alert()

        assert response_recieved and not respose_not_recieved

