from flask import Flask, make_response, jsonify, request
from productos import productos

app = Flask(__name__)


# METODOS GET   ##################################################################

@app.route('/', methods=['GET'])
def home():
    res =   make_response(
            jsonify({"consultarProductos":"http://localhost:4000/productos",
                     "agregarProductos":"http://localhost:4000/productos/agregar-producto - Se tiene en cuenta el uso de un cliente de REST API",
                     "actualizarProductos":"http://localhost:4000/productos/actualizar-producto/<nombre_producto> - Se tiene en cuenta el uso de un cliente de REST API",
                     "eliminarProducto":"http://localhost:4000/productos/eliminar-producto/<nombre_producto> - Se tiene en cuenta el uso de un cliente de REST API"}),200)
    return res

@app.route('/productos', methods=['GET'])
def consultarProductos():
    """
    Funcion para consultar todos los productos registrados
    Args: N/A
    return: Todos los productos en formato JSON
    """
    res = make_response(jsonify({"productos":productos}),200)
    return res


@app.route('/productos/<string:nombre_producto>', methods=['GET'])
def consultarProductoXNombre(nombre_producto):
    """
    Funcion para consultar productos por el nombre
    Args: (string) nombre del producto
    return: El producto consultado en formato JSON
    """
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            producto_consultado = producto
            res = make_response(jsonify({"produtoConsultado":producto_consultado}),200)
            return res
    res = make_response(jsonify({"error":"producto no encontrado!"}),404)
    return res


# METODOS POST  ##################################################################

@app.route('/productos/agregar-producto', methods=['POST'])
def agregarProducto():
    """
    Funcion para agregar productos a la lista de productos
    Args: (json) recibe un JSON mediante un cliente de REST API en mi caso Insomnia.
    return: - En caso de que el producto ya exista lo notifica
            - En caso de que el producto no exista lo agrega y muestra el mensaje correspondiente
    """
    nuevo_producto = {
        "nombre" : request.json['nombre'],
        "precio" : request.json['precio'],
        "cantidad" : request.json['cantidad']
    }

    if nuevo_producto in productos:
        res = make_response(jsonify({"error":"producto ya existe!"}),404)
        return res
    else:
        productos.append(nuevo_producto)
        res = make_response(jsonify({"mensaje":"Producto agregado exitosamente!", "productos":productos}),200)
        return res


# METODO PUT    ##################################################################

@app.route('/productos/actualizar-producto/<string:nombre_producto>', methods=['PUT'])
def actualizarProducto(nombre_producto):
    """
    Funcion para actualizar productos de la lista de productos
    Args: (json) recibe un JSON mediante un cliente de REST API en mi caso Insomnia.
    return: - En caso de que el producto no exista lo notifica
            - En caso de que el producto exista lo actualiza y muestra el mensaje correspondiente
    """
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            producto_actualizar = producto
            producto_actualizar['nombre'] = request.json['nombre']
            producto_actualizar['precio'] = request.json['precio']
            producto_actualizar['cantidad'] = request.json['cantidad']
            
            res = make_response(jsonify({
                                        "mensaje":"Producto actualizado exitosamente!", 
                                        "producto":producto_actualizar
                                        }),200)
            return res
    
    res = make_response(jsonify({"error":"producto no encontrado"}),404)
    return res
    

# METODO DELETE ##################################################################

@app.route('/productos/eliminar-producto/<string:nombre_producto>', methods=['DELETE'])
def eliminarProducto(nombre_producto):
    """
    Funcion para eliminar productos de la lista de productos
    Args: (json) recibe un JSON mediante un cliente de REST API en mi caso Insomnia.
    return: - En caso de que el producto no exista lo notifica
            - En caso de que el producto exista lo elimina y muestra el mensaje correspondiente
    """
    for producto in productos:
        if producto['nombre'] == nombre_producto:
            producto_eliminar = producto
            productos.remove(producto_eliminar)
            res = make_response(jsonify({
                                        "mensaje":"Producto eliminado exitosamente!", 
                                        "producto eliminado": producto_eliminar,
                                        "productos": productos
                                        }),200)
            return res
    
    res = make_response(jsonify({"error":"producto no encontrado"}),404)
    return res

if __name__ == '__main__':
    app.run(debug=True, port=4000)