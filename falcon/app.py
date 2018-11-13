import json

import falcon

api = application = falcon.API()


class Resource(object):

    def on_get(self, req, resp):
        resp.body = json.dumps({"msg": "falcon!"})
        resp.status = falcon.HTTP_200


resource = Resource()
api.add_route('/', resource)
