from json import load
from datetime import datetime as dt

def getReviews():
    with open("modules/reviews.json") as f:
        return load(f)

def getProducts():
    with open("modules/products.json") as f:
        return load(f)

def getSocialMedias():
    with open("modules/socialMedias.json") as f:
        return load(f)

def getOpeningTimes():
    with open("modules/openingTimes.json") as f:
        return load(f)

def isOpen():
    now = dt.now()

    hour = now.hour
    day = now.weekday()

    data = getOpeningTimes()

    today = list(data.values())[day]
    if today.get("opening") and today.get("closing"):
        return hour >= today["opening"] and hour < today["closing"]
    return False

class Enquiries:
    def __init__(self):
        ...

    def add(self, name: str, email: str, message: str, number: str=None):
        data = self.read()
        data.append({
            "name": name,
            "email": email,
            "message": message,
            "number": number
        })

    def read(self):
        with open("modules/enquiries.json", "r") as f:
            return load(f)