from flasgger import Swagger  # LazyJSONEncoder, LazyString,
from flask import Flask  # request


def initialize_flasgger(app: Flask):
    # app.json_encoder = LazyJSONEncoder

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
    }

    template = dict(
        info={
            "title": "360CRM Challenge - Swagger UI",
            "version": "0.1.0",
            "uiversion": 3,
            "description": "360CRM Challenge - API Documentation",
            "termsOfService": "/there_is_no_tos",
        },
        host="localhost:5000",
        schemes=["http", "https"],
    )

    return Swagger(app, config=swagger_config, template=template)
