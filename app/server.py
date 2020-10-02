import logging
import connexion
import traceback
from flask import jsonify, send_from_directory
from werkzeug.exceptions import HTTPException

from app.config import STATIC_ROOT
from app.views import design_tools_api

log = logging.getLogger(__name__)


EXTRA_FILES = ['app/swagger.yaml']


def create_app():
    connexion_app = connexion.App('designer-tools', specification_dir='app')
    connexion_app.add_api('swagger.yaml')

    flask_app = connexion_app.app
    flask_app.config.from_object('app.config')
    flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    flask_app.register_blueprint(design_tools_api, url_prefix='/api/')

    @flask_app.route('/<js>.js')
    def serve_js(js):
        return send_from_directory(STATIC_ROOT, f'{js}.js')

    @flask_app.route('/assets/<svg>.svg')
    def serve_assets(svg):
        return send_from_directory(STATIC_ROOT, f'assets/{svg}.svg')

    @flask_app.route('/favicon.ico')
    def serve_favicon():
        return send_from_directory(STATIC_ROOT, 'assets/favicon.ico')

    @flask_app.route('/')
    def serve_index():
        return send_from_directory(STATIC_ROOT, 'index.html')

    flask_app.register_error_handler(Exception, handle_exception)
    return connexion_app


def handle_exception(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    trace = ''.join(traceback.format_tb(e.__traceback__))
    response = jsonify(error=str(e), traceback=trace)
    log.error(response)
    return response, code


if __name__ == '__main__':
    the_app = create_app()
    flask_app = the_app.app
    the_app.run(
        port=flask_app.config['PORT'], host=flask_app.config['HOST'], debug=flask_app.config['DEBUG'],
        extra_files=EXTRA_FILES
    )
