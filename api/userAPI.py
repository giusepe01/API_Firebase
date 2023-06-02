import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('BeJpaD0QzVO7gdx86gP0w88rQ2D3')
doc_Ref = db.collection('BeJpaD0QzVO7gdx86gP0w88rQ2D3').document('yJjPQ6ZXt6pNzkZ612v3')

userAPI = Blueprint('userAPI', __name__)

@userAPI.route('/add', methods=['POST'])
def create():
        try:
            id = uuid.uuid4()
            user_Ref.document(id.hex).set(request.json)
            return jsonify({"success": True}), 200
        except Exception as e:
            return f"An Error Occured: {e}"

@userAPI.route('list', methods=['GET'])
def read():
     try:
          all_devices = [doc.to_dict() for doc in user_Ref.stream()]
          return jsonify(all_devices), 200
     except Exception as e:
          return f"An Error Occured: {e}"

@userAPI.route('/att', methods=['PUT'])
def update():
        try:
            doc_Ref.update(request.json)
            return jsonify({"success": True}), 200
        except Exception as e:
            return f"An Error Occured: {e}"
        
@userAPI.route('single', methods=['GET'])
def single():
     try:
          doc = doc_Ref.get()
          return jsonify(doc.to_dict()), 200
     except Exception as e:
          return f"An Error Occured: {e}"