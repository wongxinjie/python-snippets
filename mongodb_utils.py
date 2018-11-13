from pymongo import MongoClient

mdb = MongoClient('mongodb://bidong:wifi_BD*@14.23.62.180:27517/ap').ap


def find_max_size_collection():
    collections = mdb.collection_names(include_system_collections=False)

    name_size_dict = {}
    for c in collections:
        size = mdb.command("collstats", c)["storageSize"]
        name_size_dict[c] = size

    rvs = sorted(name_size_dict.items(), key=lambda x: x[1], reverse=True)
    limit = 10
    rvs = rvs[:limit]
    print('top %s size collection ' % (limit, ))
    for r in rvs:
        print("%s => %s G" % (r[0], r[1] / 1024.0 / 1024.0 / 1024.0))


if __name__ == "__main__":
    find_max_size_collection()
