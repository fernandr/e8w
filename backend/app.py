from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Person import Base, Person
import os

app = Flask(__name__)
CORS(app)

engine = create_engine("sqlite:///persons.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def insert_test_data():
    session = Session()
    if session.query(Person).count() == 0:
        session.add_all(
            [
                Person(name="Alice", email="alice@example.com"),
                Person(name="Bob", email="bob@example.com"),
                Person(name="Charlie", email="charlie@example.com"),
            ]
        )
        session.commit()
    session.close()


insert_test_data()


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "message": "Welkom bij het Person Demo Portaal",
            "endpoints": ["/api/persons", "/api/person/<name>", "/api/person"],
        }
    )


@app.route("/api/persons", methods=["GET"])
def get_persons():
    session = Session()
    persons = session.query(Person).all()
    result = [{"id": p.id, "name": p.name, "email": p.email} for p in persons]
    session.close()
    return jsonify(result)


@app.route("/api/person/<name>", methods=["POST"])
def edit_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    if not person:
        session.close()
        return jsonify({"error": "Person not found"}), 404
    data = request.get_json()
    if "email" in data:
        person.email = data["email"]
    if "name" in data:
        person.name = data["name"]
    session.commit()
    updated = {"id": person.id, "name": person.name, "email": person.email}
    session.close()
    return jsonify(updated)


@app.route("/api/person", methods=["POST"])
def add_person():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Missing name or email"}), 400
    session = Session()
    person = Person(name=data["name"], email=data["email"])
    session.add(person)
    session.commit()
    result = {"id": person.id, "name": person.name, "email": person.email}
    session.close()
    return jsonify(result), 201


@app.route("/api/person/<name>", methods=["DELETE"])
def delete_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    if not person:
        session.close()
        return jsonify({"error": "Person not found"}), 404
    session.delete(person)
    session.commit()
    session.close()
    return jsonify({"message": f"Person {name} deleted"})


if __name__ == "__main__":
    app.run(debug=True)
