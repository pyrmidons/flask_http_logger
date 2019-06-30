""" Flask Http Logger class. """

import os
from flask import current_app, request

from functools import wraps


class HttpLogger:
    """  """ #todo

    def __init__(self, app, config=None):
        """ """     #todo
        self.app = app
        self.config = config

        if app is not None:
            self.init_app(app, config)

    def init_app(self, app, config=None):
        """ """ #todo
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')


    def log_request_info(self, decorated_function):

        @wraps(decorated_function)
        def wrapper(*args, **kwargs):
            print('trulllail')
            print('Headers: %s', request.headers)
            print('Body: %s', request.get_data())

            return decorated_function(*args, **kwargs)

        return wrapper


    @staticmethod
    def log_everything(configs=None):
        print('Headers: %s', request.headers)
        print('Body: %s', request.get_data())