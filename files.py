import json


def create_site_list():
    file = open('siteList.json', 'w')
    file.write('{\n}')
    file.close()


def get_site_list():
    file = open('siteList.json', 'r')
    return json.loads(file)


def save_site_list_obj(json_obj):
    file = open('sileList.json', 'w')
    file.write(json.dumps(json_obj))


def get_user_data():
    file = open('userData.json', 'r')
    return json.loads(file)


def save_user_data(json_obj):
    file = open('userData.json', 'w')
    file.write(json.dumps(json_obj))
