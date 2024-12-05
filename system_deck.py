# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Define the desks with their names, URLs, and image URLs
desks = {
    'Helpdesk NIT': {
        'url': 'https://helpdesk.edu.azores.gov.pt',
        'image': 'static/images/helpdesk.png', 
    },
    'Gestão de Equipamentos': {
        'url': 'https://itcontrol.edu.azores.gov.pt',
        'image': 'static/images/gestao_material.png',  
    },
    'WIKI': {
        'url': 'https://wiki.edu.azores.gov.pt/',
        'image': 'static/images/image.png',  
    },
    'PassBolt': {
        'url': 'https://nitpass.edu.azores.gov.pt',
        'image': 'static/images/passbolt.png',  
    },
    'NMS': {
        'url': 'https://nms.edu.azores.gov.pt',
        'image': 'static/images/grafana.png',  
    },

}

@app.route('/')
def index():
    return render_template('index.html', desks=desks)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)