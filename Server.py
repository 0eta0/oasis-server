# Computer Network Lab, University of Aizu
# Author : Eita Yamaguchi(s1240219)
import falcon
import json
from Middle import CORSMiddleware, JSONTranslator
from Message import MessageJson
from Database import Data


class DataAPI(object):

    def on_post(self, req, res, operation):
        res.content_type = 'application/json'
        if 'doc' not in req.context:
            pass
        elif operation == 'get':
            res.context['result'] = Data().find(req.context['doc'])
        elif operation == 'insert':
            res.context['result'] = Data().insert(req.context['doc'])
        res.status = falcon.HTTP_200


# Create instance using middleware.
api = falcon.API(middleware=[CORSMiddleware(), JSONTranslator()])

# the request is used for operating data.
api.add_route('/data/{operation}', DataAPI())


if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, api)

    print('Start CNLAB WonderSense data server!')

    httpd.serve_forever()
