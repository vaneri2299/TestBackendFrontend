from flask import (
    Blueprint, render_template
)

detalles_blueprint = Blueprint('detalles_blueprint', __name__, template_folder='templates')

@detalles_blueprint.route("/", methods=['GET', 'POST'])
def detalles():
    """
    Vista de detalles
    """

    return render_template("detalles/detalles.html")