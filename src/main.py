import logging
import os
from uuid import uuid4

import boto3
from flask import Flask, request

from config import FlaskConfig
from library.exceptions import exception_handler
from routes import blueprints as bp
from swagger import initialize_flasgger


def create_app():
    try:
        app = Flask(__name__)

        # logging into dynamodb
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="us-east-1",
            endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
        )
        table = dynamodb.Table(os.getenv("DYNAMODB_LOG_TABLE_NAME"))

        @app.before_request
        def log_request_info():
            request_id = str(uuid4())
            log_entry = {
                "logID": request_id,
                "Method": request.method,
                "URL": request.url,
                "Headers": dict(request.headers),
            }

            try:
                table.put_item(Item=log_entry)
                logging.info(f"Logged request {request_id}")
            except Exception as e:
                logging.error(
                    f"Unable to write log to DynamoDB table. logID: {request_id}"
                )
                raise e

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
