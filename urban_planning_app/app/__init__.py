from flask import Flask

# The 'app' directory is the app.root_path.
# templates are one level up from app.root_path.
app = Flask(__name__, template_folder='../templates')

from . import routes
app.register_blueprint(routes.main_bp)
