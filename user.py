import files
import os


class UserSettings:

    USER_SETTINGS_FILE = 'user.json'

    __settings_object = dict()

    def __init__(self):
        if os.path.exists(files.get_data_folder() + self.USER_SETTINGS_FILE):
            self.__settings_object = files.read(self.USER_SETTINGS_FILE)

    def get_email(self):
        return self.__settings_object['email']

    def get_telegram_chat_id(self):
        return self.__settings_object['telegram_id']

    def set_email(self, email):
        self.__settings_object['email'] = email

    def set_telegram_chat_id(self, cid):
        self.__settings_object['telegram_id'] = cid

    def save(self):
        files.save(self.__settings_object, self.USER_SETTINGS_FILE)
