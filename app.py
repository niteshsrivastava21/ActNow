from flask import Flask, render_template, request, jsonify, make_response
from model import bot_utils

app = Flask(__name__, template_folder="template")


@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("login.html")


@app.route('/botrequest', methods=['GET', 'POST'])
def bot_requests():
    req = request.get_json(silent=True, force=True)
    return make_response(jsonify(bot_utils.parse_results(req)))


if __name__ == '__main__':
    app.run()
