import requests


def hello():
    c = requests.get("https://api.github.com/repos/insper/dev-aberto/commits")
    info = c.json()
    if isinstance(info, list):
        commit_info = info[0]["commit"]["author"]
        return commit_info["date"], commit_info["name"]
    return None, None
