from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "API de Jesús Romero - Proyecto de Ingeniería en Software"

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = {
        "id": user_id,
        "nombre": "Jesus Antonio Romero Duarte",
        "carrera": "Ingeniería en Desarrollo de Software",
        "estatus": "Activo"
    }
    
    query = request.args.get('query')
    if query:
        user["busqueda_extra"] = query
        
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json 
    
    data["mensaje_servidor"] = "Usuario procesado exitosamente"
    
    return jsonify(data), 201

if __name__ == '__main__':

    app.run(debug=True)
