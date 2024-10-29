import time


def response_data(data=None, code=200, message=""):
    return {
        "meta": {
            "code": code,
            "message": message,
            "time_stamp": int(time.time())
        },
        "data": data
    }