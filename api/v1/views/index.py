from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

@app.route('/api/v1/stats', methods=['GET'])
def get_stats():
    stats = {
        'amenities': storage.count('amenities'),
        'cities': storage.count('cities'),
        'places': storage.count('places'),
        'reiews': storage.count('reiews'),
        'states': storage.count('states'),
        'users': storage.count('users'),
    }
    return jsonify(counts)

if __name__ == '__main__':
    app.run(debug=True)
