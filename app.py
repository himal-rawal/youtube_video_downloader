import main
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class DownloadPlaylist(Resource):
    def get(self, youtubeurl):
        return {'data': main.downloadplaylist(youtubeurl)}


api.add_resource(DownloadPlaylist, '/download/<youtubeurl>')

if __name__ == '__main__':
    app.run()