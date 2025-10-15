import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)

import FlaskExercise.views