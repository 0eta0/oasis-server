import falcon
import json
from Message import MessageJson


class CORSMiddleware(object):

    def process_request(self, req, res):
        res.set_header('Access-Control-Allow-Origin', '*')
        res.set_header('Access-Control-Allow-Methods', 'GET,POST')

class JSONTranslator(object):

    def process_resource(self, req, resp, resource, params):
        if req.content_length in (None, 0):
            resp.context['result'] = MessageJson.REQUEST_FAILED.value
        body = req.stream.read()
        if not body:
            resp.context['result'] = MessageJson.REQUEST_FAILED.value
        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError) as error:
            resp.context['result'] = MessageJson.JSON_ERROR.value


    def process_response(self, req, resp, resource, req_succeeded):
        if 'result' not in resp.context:
            resp.body = MessageJson.REQUEST_FAILED.value
        else:
            if type(resp.context['result']) == dict:
                resp.body = json.dumps(resp.context['result'])
            else:
                resp.body = resp.context['result']
