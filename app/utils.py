from flask import Flask

def register_blueprints(app: Flask) -> None:

    # Importar blueprints
    from app.inicio.vistas.vistas import inicio_blueprint
    from app.detalles.vistas.vistas import detalles_blueprint
    from app.calibracion.vistas.vistas import calibracion_blueprint

    # Registrar blueprints con la app de Flask
    app.register_blueprint(inicio_blueprint, url_prefix="/")
    app.register_blueprint(detalles_blueprint, url_prefix="/detalles")
    app.register_blueprint(calibracion_blueprint, url_prefix="/calibracion")