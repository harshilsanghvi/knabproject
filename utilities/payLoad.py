
def addCardPayload(name, due, desc="", pos=""):
    body = {

        "name": name,
        "desc": desc,
        "pos": pos,
        "due": due
    }
    return body

def updateCardPayload(desc):
    body = {
        "desc": desc,
    }
    return body