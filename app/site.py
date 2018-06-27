from api import files


def get_site_list():
    return files.read('siteList.json')


def save_site_list_obj(sites_obj):
    files.save(sites_obj, 'siteList.json')


def add(name, url, settings):
    sites = get_site_list()
    if name in sites.keys():
        return "site_name_exists_error"
    sites[name] = {"url": url, "settings": settings}
    save_site_list_obj(sites)


def delete(name):
    sites = get_site_list()
    if name not in sites.keys():
        return "site_name_not_exists_error"
    del sites[name]
    save_site_list_obj(sites)


def rename(old_name, new_name):
    sites = get_site_list()
    if old_name not in sites.keys():
        return "site_name_not_exists_error"
    if new_name in sites.keys():
        return "site_name_exists_error"
    sites[new_name] = sites.pop(old_name)
    save_site_list_obj(sites)


def get_list():
    return get_site_list().keys()


def build_settings(method, headers, body, proxy, expected_code, expected_answer, sitemap_search):
    return {"method": method, "headers": headers, "body": body, "proxy": proxy, "expected_code": expected_code,
            "expected_answer": expected_answer, "sitemap_search": sitemap_search}
