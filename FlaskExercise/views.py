from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == "info":
        app.logger.info("Button pressed")
    elif log == "warning":
        app.logger.warning("Button pressed")
    elif log == "error":
        app.logger.error("Button pressed")
    elif log == "critical":
        app.logger.critical("Button pressed")
    return render_template(
        'index.html',
        log=log
    )
