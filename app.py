import main
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class DownloadPlaylist(Resource):
    def get(self, playlistid):
        return {'data': main.downloadplaylist(playlistid)}


api.add_resource(DownloadPlaylist, '/download/<playlistid>')

if __name__ == '__main__':
    app.run()
