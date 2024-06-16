from flask import Flask

from config import FlaskConfig
from library.exceptions import exception_handler
from routes import blueprints as bp
from swagger import initialize_flasgger


def create_app():
    try:
        app = Flask(__name__)

        initialize_flasgger(app)

        app.config.from_object(FlaskConfig())
        app.register_error_handler(Exception, exception_handler)

        # Blueprints
        app.register_blueprint(bp.users_bp, url_prefix="/api/v1/user")
        app.register_blueprint(bp.roles_bp, url_prefix="/api/v1/role")
        app.register_blueprint(bp.claims_bp, url_prefix="/api/v1/claim")
        app.register_blueprint(bp.user_claims_bp, url_prefix="/api/v1/user-claim")

        return app
    except Exception as e:
        raise Exception(f"Error while creating app: {e}")


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
