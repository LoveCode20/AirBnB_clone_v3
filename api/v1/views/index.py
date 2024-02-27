from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

app = Flask(__name__)

@app.route('/api/v1/stats', methods=['GET'])
def get_stats():
    counts = {}
    counts['objects'] = {}
    counts['object']['Object1'] = storage.count('Object1')
    counts['object']['Object2'] = storage.count('Object2')
    counts['object']['Object3'] = storage.count('Object3')
    return jsonify(counts)

if __name__ == '__main__':
    app.run(debug=True)
