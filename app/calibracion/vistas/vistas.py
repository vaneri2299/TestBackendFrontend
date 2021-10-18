from flask import (
    Blueprint, render_template
)

calibracion_blueprint = Blueprint('calibracion_blueprint', __name__, template_folder='templates')

@calibracion_blueprint.route("/", methods=['GET', 'POST'])
def calibracion():
    """
    Vista de calibracion
    """

    return render_template("calibracion/calibracion.html")