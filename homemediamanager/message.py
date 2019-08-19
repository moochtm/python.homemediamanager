__author__ = 'matt_barr'

# from pushbullet import PushBullet

class PushBulletMessage:
    def __init__(self):
        self.subject = ""
        self.body = ""

    def send(self, account_id=None):

        # sending a pushbullet message
        if not account_id == None:
            # pb = PushBullet(account_id)
            # success, push = pb.push_note(self.subject, self.body)
            return success