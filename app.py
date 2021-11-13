from bilibili_api import video, sync
from flask import Flask
from flask_restful import Resource, Api, reqparse

class Danmus(Resource):
    def get(self, video_id):
        v = video.Video(bvid=video_id)
        dms = sync(v.get_danmakus(0))
        dict_dms = map(lambda x: {'text': x.text, 'time': x.dm_time, 'send_time': x.send_time, 'crc32_id': x.crc32_id}, dms)
        dict_dms = list(dict_dms)
        return {'data': dict_dms}, 200

app = Flask(__name__)
api = Api(app)

api.add_resource(Danmus, '/danmus/', '/danmus/<video_id>')
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=6677)
