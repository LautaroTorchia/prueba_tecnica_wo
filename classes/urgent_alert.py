from classes.alert import Alert

class UrgentAlert(Alert):

    def send_alert(self):
        self.user.add_alert(self)