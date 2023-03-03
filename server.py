from flask_app.controllers import clubs_controller, users_controller, movies_controller
from flask_app import app
import requests, json
import tmdbsimple as tmdb
tmdb.API_KEY = 'df37e82fe4df884b36076a43303b68ae'

if __name__ == "__main__":
    app.run(debug=True)