import falcon
from falcon_multipart.middleware import MultipartMiddleware
import json
from datetime import datetime

class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')

class Upload:
    def on_post(self, req, res):
        print(req)
        image = req.get_param('file')
        raw = image.file.read()
        filepath = './' + datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        with open(filepath, 'wb') as f:
            f.write(raw)

        resp = {
            'result': filepath + ' uploaded',
        }
        res.body = json.dumps(resp)

api = falcon.API(middleware=[CORSMiddleware(), MultipartMiddleware()])
api.add_route('/kitamura', Upload())
