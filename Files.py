import json


def create_site_list():
    file = open('siteList.json', 'w')
    file.write("{\n}")
    file.close()


def get_site_list():
    file = open('siteList.json', 'r')
    return json.loads(file)


def save_site_list_obj(jsonObj):
    file = open('sileList.json', 'w')
    file.write(json.dumps(jsonObj))
