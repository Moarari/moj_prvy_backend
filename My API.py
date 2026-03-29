from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Adam Novak", "age": 17, "image": "https://picsum.photos/200?1"},
    {"id": 2, "name": "Beata Kralova", "age": 18, "image": "https://picsum.photos/200?2"},
    {"id": 3, "name": "Cyril Urban", "age": 16, "image": "https://picsum.photos/200?3"},
    {"id": 4, "name": "Diana Mrazova", "age": 17, "image": "https://picsum.photos/200?4"},
    {"id": 5, "name": "Erik Svec", "age": 18, "image": "https://picsum.photos/200?5"},
    {"id": 6, "name": "Filip Hric", "age": 17, "image": "https://picsum.photos/200?6"},
    {"id": 7, "name": "Gabriela Tothova", "age": 16, "image": "https://picsum.photos/200?7"},
    {"id": 8, "name": "Hana Bielikova", "age": 17, "image": "https://picsum.photos/200?8"},
    {"id": 9, "name": "Ivan Kollar", "age": 18, "image": "https://picsum.photos/200?9"},
    {"id": 10, "name": "Jana Sramkova", "age": 17, "image": "https://picsum.photos/200?10"}
]

@app.route("/")
def home():
    return "Vitaj v mojom prvom backende!"

@app.route("/api")
def get_all_students():
    return jsonify(students)

@app.route("/api/student/<int:student_id>")
def get_student(student_id):
    for s in students:
        if s["id"] == student_id:
            return jsonify(s)
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
