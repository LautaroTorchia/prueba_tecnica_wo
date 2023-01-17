

import pytest
from classes.user import User
from classes.topic import Topic
from classes.informative_alert import InformativeAlert
from datetime import datetime,timedelta
from classes.notification_system import NotificationSystem


class TestNotificationSystem:
    
    notificationSystem=NotificationSystem()
    
    topicRegistered=notificationSystem.register_topic("Test Topic 1", "Test Description 1")
    userWithTopic=notificationSystem.register_user("Test User", "@a.com@")
    userWithoutTopic=notificationSystem.register_user("Test User 2", "aaa@a.com")
    
    topicNotRegistered=Topic("Test Topic 3", "This topic is not included by the system")
    userNotRegistered=User("Test User", "notincludedinSystem@a.com")
    
    
    def test_register_user(self):
        self.userWithTopic = self.notificationSystem.register_user("Test User for register function", "a@a.com")
        assert self.userWithTopic in self.notificationSystem.get_users() and self.userNotRegistered not in self.notificationSystem.get_users()
    
    def test_register_topic(self):
        self.topicRegistered=self.notificationSystem.register_topic("Test Topic 1", "Test Description 1")
        assert self.topicRegistered in self.notificationSystem.get_topics() and self.topicNotRegistered not in self.notificationSystem.get_topics()
    
    def test_send_urgent_alert_broadcast(self):
        self.notificationSystem.send_urgent_alert("alerta alerta",self.topicRegistered)
        assert self.userWithTopic.alerts[0].topic == self.topicRegistered and self.userWithoutTopic.alerts[0].topic == self.topicRegistered and self.userNotRegistered.alerts == []
    
    def test_send_urgent_alert_uniq(self):
        self.notificationSystem.send_urgent_alert("alerta,alerta",self.topicRegistered, self.userWithoutTopic)
        assert len(self.userWithTopic.alerts) == 1 and len(self.userWithoutTopic.alerts) == 2
    
    def test_send_informative_alert_broadcast(self):
        self.userWithTopic.create_topic_notification(self.topicRegistered)
        self.notificationSystem.send_informative_alert("alerta,",self.topicRegistered)
        assert len(self.userWithTopic.alerts) == 2 and len(self.userWithoutTopic.alerts) == 2 and self.userNotRegistered.alerts == []
    
    def test_send_informative_alert_uniq(self):
        self.notificationSystem.send_informative_alert("alerta",self.topicRegistered, self.userWithTopic)
        assert len(self.userWithTopic.alerts) == 3 and len(self.userWithoutTopic.alerts) == 2
    
    
    
    