

import pytest
from classes.user import User
from classes.topic import Topic
from classes.informative_alert import InformativeAlert
from datetime import datetime,timedelta

class TestUser:
    
    user = User("Test User", "a@a.com")
    topic_included_1=Topic("Test Topic 1", "Test Description 1")
    topic_included_2=Topic("Test Topic 2", "Test Description 2")
    topic_not_included=Topic("Test Topic 3", "This topic is not included by the user")
    expired_alert=InformativeAlert("birthday",user,topic_included_1,datetime.now()-timedelta(days=1))
    unexpired_alert_older=InformativeAlert("birthday",user,topic_included_1,datetime.now()+timedelta(days=2))
    unexpired_alert_younger=InformativeAlert("birthday",user,topic_included_1,datetime.now()+timedelta(days=2))
        
    def test_adding_alerts(self):
        self.user.add_alert(self.unexpired_alert_older)
        self.user.add_alert(self.expired_alert)
        self.user.add_alert(self.unexpired_alert_younger)
        assert self.unexpired_alert_older in self.user.alerts and self.expired_alert in self.user.alerts

    def test_add_interested_topic(self):
        self.user.create_topic_notification(self.topic_included_1)
        self.user.create_topic_notification(self.topic_included_2)
        assert self.topic_included_1 in self.user.topics and self.topic_included_2 in self.user.topics
    
    def test_can_recieve_from_topic(self):
        assert self.user.can_can_recieve_from_topic(self.topic_included_2) == True and self.user.can_can_recieve_from_topic(self.topic_not_included) == False
    
    def test_unread_alerts(self):
        assert self.user.unread_alerts() == [self.unexpired_alert_younger,self.unexpired_alert_older]
        self.user.mark_as_read(self.unexpired_alert_older)
        assert self.user.unread_alerts() == [self.unexpired_alert_younger]
