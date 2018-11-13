import time

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY=('\xb73?\xb5\x83j\xf7W\xc1?\x8f\xe7'
                '\xbb\xa3\xaf0\x9d\x90\x00l\xc5\xe1CM')
))


@app.route("/callback", methods=['POST'])
def receiver():
    context = request.get_json()
    print(context)
    return jsonify({"response": "OK!"})


@app.route('/block')
def block_view():
    time.sleep(10)
    print('block view processing finish')
    return jsonify({"content": "block view ok"})


@app.route('/normal')
def normal_view():
    print('normal view processing finish')
    return jsonify({"content": "normal view ok"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=19939, debug=True)
