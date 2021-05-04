from mycroft import MycroftSkill, intent_file_handler


class VirtualDoctor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('doctor.virtual.intent')
    def handle_doctor_virtual(self, message):
        self.speak_dialog('doctor.virtual')


def create_skill():
    return VirtualDoctor()

