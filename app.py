import os
import sys


from flask import Flask, request, make_response
from werkzeug.routing import Rule

from loggers import logger

app = Flask(__name__)
app.url_map.add(Rule('/<path:path>', endpoint='query'))
app.url_map.add(Rule('/', endpoint='query', defaults={'path': ''}))

PORT = 5000

if len(sys.argv) == 2 and '=' in sys.argv[1]:
    var_name, var_value = sys.argv[1].split('=')
    if var_name == 'PORT' and var_value.isdigit():
        PORT = os.environ[var_name] = var_value


@app.endpoint('query')
def query(path):
    try:
        # we want to log a timestamp when request was received. Using logger auto timestamp for that
        logger.info(f'{request.method} - /{path} - {dict(request.args)}')

        if request.method != 'GET':
            logger.error(f'{request.method} method not allowed\n')
            return

        if request.args.get('invalid') == '1':
            logger.error('Got "invalid = 1" parameter\n')
            return

        if path not in ['api/', 'api']:
            logger.error('Invalid path\n')
            return

        process1()

        is_success = process2()
        if not is_success: return

        process3()
    finally:
        return make_response()


def process1():
    logger.info('Starting process1')
    logger.info('Doing complicated calculations for process1')
    logger.info('Completed process1')


def process2():
    logger.info('Starting process2')

    if request.args.get('notawaiting') == '1':
        logger.error('Got "notawaiting=1" parameter')
        logger.info('Closing process2\n')
        return False

    logger.info('Doing complicated calculations for process2')
    logger.info('Completed process2')
    return True


def process3():
    logger.info('Starting process3')
    logger.info('Doing complicated calculations for process3')
    logger.info('Completed process3\n')


if __name__ == '__main__':
    app.run(port=PORT)
