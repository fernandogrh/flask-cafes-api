from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

def str_to_bool(value):
    return str(value).lower() in ["true", "t", "yes", "1", "on"]

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if not all_cafes:
        return jsonify(error={"Not found": "Sorry, no cafes available in the database."}), 404
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search():
    location = request.args.get('loc', '').strip()
    matches = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    if matches:
        return jsonify(cafes=[cafe.to_dict() for cafe in matches])
    else:
        return jsonify(error={"Not found": "Sorry, we do not have a cafe at that location"}), 404

@app.route("/add", methods=["POST"])
def add_cafe():
    existing_cafe = db.session.execute(db.select(Cafe).where(Cafe.name == request.form.get('name'))).scalar()
    if existing_cafe:
        return jsonify(error={"Conflict": "A cafe with that name already exists in the database."}), 409
    cafe_to_add = Cafe(
        name=request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_sockets=str_to_bool(request.form.get("sockets")),
        has_toilet=str_to_bool(request.form.get("toilet")),
        has_wifi=str_to_bool(request.form.get("wifi")),
        can_take_calls=str_to_bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(cafe_to_add)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    new_price = request.form.get('new_price')
    cafe_to_update = db.get(Cafe, cafe_id)
    if cafe_to_update is None:
        return jsonify(error={"Not found": "Sorry, a cafe with that id was not found in the database."}), 404
    cafe_to_update.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == API_KEY:
        cafe_to_delete = db.get(Cafe, cafe_id)
        if cafe_to_delete is None:
            return jsonify(error={"Not found": "Sorry, a cafe with that id was not found in the database."}), 404
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
