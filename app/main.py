from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'index'


@app.route('/hello')
def hello():
    # message = 11
    co: int = typing('Hello, world')
    return jsonify(
        {
            'stringCount': co,
            'message': 'Hello, world'
        }
    )


def typing(message: str) -> int:
    return len(message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
