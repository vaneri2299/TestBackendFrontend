from flask import (
    Blueprint, render_template
)

inicio_blueprint = Blueprint('inicio_blueprint', __name__, template_folder='templates')

@inicio_blueprint.route("/", methods=['GET', 'POST'])
def inicio():
    """
    Vista de inicio
    """

    return render_template("inicio/inicio.html")