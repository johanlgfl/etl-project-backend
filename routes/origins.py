from flask import Blueprint

origins = Blueprint("origins", __name__, url_prefix="/origins")


@origins.route("/")
def home():
    return "Origins list!"


@origins.route("/<int:origin_id>", methods=["POST"])
def origin(origin_id):
    return f"Origin {origin_id}"