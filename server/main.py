from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import base64
import face_recognition
import io
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()

################################################################################

@cross_origin()
@app.route('/health', methods=['GET'])
def health():
    return jsonify({ 'message': 'Alive!' }), 200

@cross_origin()
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []

    for user in users:
        result.append({ 
            'id': user.id, 
            'username': user.username, 
            'image_path': user.image_path 
        })

    return jsonify(result), 200

@cross_origin()
@app.route('/user/<string:username>', methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    result = {}

    if user:
        result['id'] = user.id
        result['username'] = user.username
        result['image_path'] = user.image_path

    return jsonify(result), 200

@cross_origin()
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({ 'message': 'This username does not exist' }), 401
    
    input_picture = request.form['picture']
    input_picture = input_picture.split(',')[1]
    input_picture = base64.b64decode(input_picture)
    
    picture_of_user = face_recognition.load_image_file(user.image_path)
    user_face_encoding = face_recognition.face_encodings(picture_of_user)[0]

    input_picture = face_recognition.load_image_file(io.BytesIO(input_picture))
    input_face_encoding = face_recognition.face_encodings(input_picture)[0]
    results = face_recognition.compare_faces([user_face_encoding], input_face_encoding, 0.4)

    # See the distances between two faces
    # face_distances = face_recognition.face_distance([user_face_encoding], input_face_encoding)
    # print(face_distances)
    
    if results[0] == False:
        return jsonify({ 'message': 'Unauthorized' }), 401
    
    return jsonify({ 'message': 'Signed in successfully' }), 200

@cross_origin()
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    confirm_username = request.form['confirmUsername']
    if username != confirm_username:
        return jsonify({ 'message': 'The Username and confirm username does not match' }), 400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({ 'message': 'This username already exists' }), 401

    user = User(username=username, image_path=f'./dataset/{username}.jpg')
    db.session.add(user)
    db.session.commit()

    input_picture = request.form['picture']
    input_picture = input_picture.split(',')[1]
    input_picture = base64.b64decode(input_picture)

    # Create the ./dataset/ directory if it does not exist
    dataset_dir = os.path.join(os.getcwd(), 'dataset')
    if not os.path.exists(dataset_dir):
        os.mkdir(dataset_dir)

    # Save the image to the ./dataset/ directory
    filename = f'{username}.jpg'
    filepath = os.path.join(dataset_dir, filename)
    with open(filepath, 'wb') as f:
        f.write(input_picture)

    return jsonify({ 'message': 'Signed up successfully' }), 201





