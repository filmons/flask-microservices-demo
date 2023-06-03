from flask import Flask, jsonify, request
import logging
import requests


app = Flask(__name__)


@app.route('/detail/<int:order_id>', methods=['GET'])
def detail(order_id):
    print(order_id)
    order = requests.get('http://localhost:5000/order/{}'.format(order_id)).json()
    items = [_fetch_item(item_id) for item_id in order.get('items', [])]
    del order['items']
    order['items'] = items
    return jsonify(order), 200


def _fetch_item(item_id):
    return requests.get('http://localhost:5001/item/{}'.format(item_id)).json()


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(port=5002,debug=True, host='0.0.0.0')