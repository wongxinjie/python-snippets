from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.blogger


def mock_slow_query():
    db.blogger.find({"$where": "sleep(1000) || true"})
    return True


print(mock_slow_query())
