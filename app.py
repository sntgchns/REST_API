from flask import Flask, jsonify, request
from products import products
import requests, json

app = Flask(__name__)

@app.route('/products')
def getproducts():
    return jsonify({
        "Products": products,
        "message": "Products retrieved successfully"
        })

@app.route('/tester')
def test():
    url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    r = requests.get(url)
    j = json.loads(r.text)
    city = j['city']
    print(city)

@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        return jsonify({
            "Products": productsFound[0],
            "message": "Products list"
            })
    return jsonify({
        "message": "Product not found"
        })

@app.route('/products', methods=['POST'])
def addproduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({
        "message": "Product added succesfully",
        "products": products
        })

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product deleted",
            "products": products
            })
    return jsonify({"message": "Product not found"})

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == "__main__":
    app.run(debug=True, port=4000)