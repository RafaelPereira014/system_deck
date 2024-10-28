# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Define the desks with their names, URLs, and image URLs
desks = {
    'Helpdesk NIT': {
        'url': '/helpdesk',
        'image': 'static/images/helpdesk.png',  # Replace with actual image URL
    },
    'Gestão de Equipamentos': {
        'url': '/material_management',
        'image': 'static/images/gestao_material.png',  # Replace with actual image URL
    },
    'IT Support': {
        'url': '/it_support',
        'image': 'https://via.placeholder.com/150?text=IT+Support',  # Replace with actual image URL
    },
}

@app.route('/')
def index():
    return render_template('index.html', desks=desks)

# Define routes for each desk
@app.route('/helpdesk')
def helpdesk():
    return "Welcome to the Helpdesk NIT!"

@app.route('/material_management')
def material_management():
    return "Welcome to the Gestão de Equipamentos Desk!"

@app.route('/it_support')
def it_support():
    return "Welcome to the IT Support Desk!"

if __name__ == '__main__':
    app.run(debug=True)