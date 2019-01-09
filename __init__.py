from mycroft import MycroftSkill, intent_file_handler


class Gokulakrishnan(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gokulakrishnan.intent')
    def handle_gokulakrishnan(self, message):
        self.speak_dialog('gokulakrishnan')


def create_skill():
    return Gokulakrishnan()

