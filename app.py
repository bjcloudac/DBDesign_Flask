"""
This module designs and implement a simple static database with Flask application.
"""

import json
import uuid

from flask import Flask, jsonify, request

from db import stores, items

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    Handle requests to the home page.

    Returns:
        Response object: JSON response with a welcome message.
    """
    return jsonify(message="Welcome! The website is under construction."), 200


@app.route("/stores", methods=["GET"])
def get_stores() -> json:
    """
    Handle requests to the /stores page.

    Returns:
        Response object: JSON response with all store details.
    """
    return jsonify(list(stores.values()))


@app.route("/stores/<string:store_id>", methods=["GET"])
def get_store(store_id):
    """
    Handle requests to the /stores/store_id page.

    Returns:
        Response object: JSON response for single store.
    """

    try:
        return stores[store_id]
    except KeyError:
        return jsonify({"Error": "Store not found"}), 404


@app.route("/add_store", methods=["POST"])
def add_store():
    """
    Handle requests to the 127.0.0.1:5000/add_store page to add a store.
    Checks whether the store exists

    Returns:
        Response object: JSON response for single store added if successful; else Error Message.
    """
    store_data_received = request.get_json()

    store_id = uuid.uuid4().hex
    store = {**store_data_received, "Store_ID": store_id}
    stores[store_id] = store
    return jsonify(store, {"Success": " Store Added"}, 200)


@app.delete("/stores/<string:store_id>")
def delete_store(store_id):
    """
    Handle requests to the /stores/store_id delete page.

    Returns:
        Response object: JSON response for single item.
    """

    try:
        store = stores[store_id]
        del stores[store_id]
        return jsonify(store, {"Message": "Successfully deleted"})

    except KeyError:
        return jsonify({"Error": "Store not found"})


@app.put("/stores/<string:store_id>")
def update_store(store_id):
    """
    Handle requests to the /stores/store_id update page.

    Returns:
        Response object: JSON response for single item.
    """

    try:
        store_data_received = request.get_json()
        store = stores[store_id]
        store |= store_data_received
        return jsonify(store, {"Message": "Successfully updated"})

    except KeyError:
        return jsonify({"Error": "Store not found"})


@app.route("/add_item", methods=["POST"])
def add_item():
    """
    Handle requests to the 127.0.0.1:5000/add_item page to add an item.
    We expect the add_item request
    to hold the store_id along with request such that items gets added to the correct store.

    Returns:
        Response object: JSON response for single item added if successful; else Error Message.
    """
    item_data_received = request.get_json()
    item_id = uuid.uuid4().hex
    item = {**item_data_received, "Item_ID": item_id}
    items[item_id] = item
    return jsonify(item, {"Success": " Item Added"}, 200)


@app.route("/items", methods=["GET"])
def get_items() -> json:
    """
    Handle requests to the /items page.

    Returns:
        Response object: JSON response with all item details.
    """
    return jsonify(list(items.values()))


@app.route("/items/<string:item_id>", methods=["GET"])
def get_item(item_id):
    """
    Handle requests to the /items/item_id page.

    Returns:
        Response object: JSON response for single item.
    """

    try:
        return items[item_id]
    except KeyError:
        return jsonify({"Error": "Item not found"}, 404)


@app.delete("/items/<string:item_id>")
def delete_item(item_id):
    """
    Handle requests to the /items/item_id delete page.

    Returns:
        Response object: JSON response for single item.
    """

    try:
        item = items[item_id]
        del items[item_id]
        return jsonify(item, {"Message": "Successfully deleted"}, 200)

    except KeyError:
        return jsonify({"Error": "Item not found"}, 404)


@app.put("/items/<string:item_id>")
def update_item(item_id):
    """
    Handle requests to the /items/item_id update page.

    Returns:
        Response object: JSON response for single item.
    """

    try:
        item_data_received = request.get_json()
        item = items[item_id]
        item |= item_data_received
        return jsonify(item, {"Message": "Successfully updated"}, 200)

    except KeyError:
        return jsonify({"Error": "Item not found"}, 404)


if __name__ == "__main__":
    app.run(debug=True)  # Added debug mode for development
