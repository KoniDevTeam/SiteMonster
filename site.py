import files


def add(name, url, settings):
    sites = files.get_site_list()
    if name in sites.keys():
        return "site_name_exists_error"
    sites[name] = {"url": url, 'settings': settings}
    files.save_site_list_obj(sites)


def delete(name):
    sites = files.get_site_list()
    if name not in sites.keys():
        return "site_name_not_exists_error"
    del sites[name]
    files.save_site_list_obj(sites)


def rename(old_name, new_name):
    sites = files.get_site_list()
    if old_name not in sites.keys():
        return "site_name_not_exists_error"
    if new_name in sites.keys():
        return "site_name_exists_error"
    sites[new_name] = sites.pop(old_name)
    files.save_site_list_obj(sites)


def get_list():
    return files.get_site_list().keys()
