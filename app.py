from flask import Flask, send_file, jsonify, make_response
from flask_cors import CORS
import os
import glob
import subprocess
import sys

flask_app = Flask(__name__)
CORS(flask_app, resources={r"/*": {"origins": "*"}}, support_credentials=True)

image_dirs = ['./images', './opensourceimage/data/bike', './opensourceimage/data/cars', './opensourceimage/data/cats', './opensourceimage/data/dogs',  './opensourceimage/data/flowers',  './opensourceimage/data/horses',  './opensourceimage/data/human' ]
@flask_app.route('/image-ids')
def get_image_ids():
    image_ids = []
    for image_dir in image_dirs:
        if not os.path.exists(image_dir):
            continue
        files = glob.glob(os.path.join(image_dir, "*"))
        if not files:
            continue
        image_ids.extend([os.path.splitext(os.path.basename(file))[0] for file in files])
    if not image_ids:
        return "The directories are empty.", 404
    response = make_response(jsonify(image_ids))
    response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Origin', 'https://working-leather-suit.glitch.me')
    response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    return response

@flask_app.route('/image-ids', methods=['GET'], endpoint='test_route')
def your_route_handler():
    response = make_response("hi")
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    # response.headers.add('Access-Control-Allow-Origin', 'https://working-leather-suit.glitch.me')

    return response

@flask_app.route('/images/<image_id>')
def serve_image(image_id):
    for image_dir in image_dirs:
        matching_files = glob.glob(os.path.join(image_dir, f"{image_id}.*"))
        if matching_files:
            response = make_response(send_file(matching_files[0]))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    return f"Image {image_id} does not exist.", 404

# if __name__ == "__main__":
#     flask_app.run(port=5002, debug=True)

node_path = os.path.join("C:", os.sep, "Program Files", "nodejs")

if __name__ == '__main__':
    flask_process = subprocess.Popen([sys.executable, '-m', 'flask', 'run', '--port=5001'])
    npx_path = os.path.join(node_path, "npx.cmd")
    pylt_process = subprocess.Popen([npx_path, 'localtunnel', '--port', '5001',  '--subdomain',  'opensourcedsair' ])
            
    try:
        flask_process.wait()
        pylt_process.wait()
    except KeyboardInterrupt:
        flask_process.terminate()
        pylt_process.terminate()
