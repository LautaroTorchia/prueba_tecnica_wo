
from classes.user import User
from classes.topic import Topic
from classes.informative_alert import InformativeAlert
from datetime import datetime,timedelta

class TestTopic:
    
    user = User("Test User2", "a@a.com")
    topic=Topic("Test Topic 1", "Test Description 1")
    expired_alert=InformativeAlert("birthday",user,topic,datetime.now()-timedelta(days=1))
    unexpired_alert=InformativeAlert("birthday",user,topic,datetime.now()+timedelta(days=2))
    topic.alerts.append(expired_alert)


    def test_adding_alerts(self):
        self.topic.add_alert(self.unexpired_alert)
        assert self.unexpired_alert in self.topic.alerts
    
    def test_get_unexpired_alerts(self):
        assert self.unexpired_alert in self.topic.get_unexpired_alerts()
        assert self.expired_alert not in self.topic.get_unexpired_alerts()
