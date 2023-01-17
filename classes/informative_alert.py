from classes.alert import Alert

class InformativeAlert(Alert):
    
    def send_alert(self):
        if self.user.can_can_recieve_from_topic(self.topic):
            self.user.add_alert(self)
            return True
        return False