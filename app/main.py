from flask import Flask, jsonify

from app.domain.service.dish_service import DishService

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'index'


@app.route('/dishes')
def dishes():
    dishes = DishService.find_with_dishes()
    return jsonify(
        dict(
            dishes=[dish.to_dict() for dish in dishes]
        )
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
