def create_site_list():
    file = open("siteList.json", "w")
    file.write("{\n}")
    file.close()


def open_site_list():
    file = open("siteList.json", "r")
    return file
