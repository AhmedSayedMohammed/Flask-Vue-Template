from flask import Flask, render_template
from flask_cors import CORS
from User import user

app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.register_blueprint(user, url_prefix='/users')


@app.route('/', methods=['GET'])
def index():
    return "Index"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
