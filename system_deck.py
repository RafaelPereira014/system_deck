# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Define the desks with their names, URLs, and image URLs
desks = {
    'Helpdesk NIT': {
        'url': 'https://helpdesk.edu.azores.gov.pt',
        'image': 'static/images/helpdesk.png',  # Replace with actual image URL
    },
    'Gestão de Equipamentos': {
        'url': 'http://172.22.130.12:8081',
        'image': 'static/images/gestao_material.png',  # Replace with actual image URL
    },
    'Gestão de Bolsas de Ilha': {
        'url': 'https://bolsas-ilha.azores.gov.pt/',
        'image': 'static/images/bolsas.png',  # Replace with actual image URL
    },
    'WIKI': {
        'url': 'https://nit.edu.azores.gov.pt/',
        'image': 'static/images/image.png',  # Replace with actual image URL
    },

}

@app.route('/')
def index():
    return render_template('index.html', desks=desks)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)