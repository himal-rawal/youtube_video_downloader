import main
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class DownloadPlaylist(Resource):
    def get(self, youtubeurl):
        return {'data': main.downloadplaylist(youtubeurl)}


api.add_resource(DownloadPlaylist, '/download/<youtubeurl>') #I think giving url as a parameter in url is not acceptable so how can we use post request instead of get in this programs context

if __name__ == '__main__':
    app.run()
