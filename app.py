from flask import Flask, jsonify, redirect, render_template, request, url_for
import database as dbase
from producto import producto


app = Flask(__name__)
db = dbase.dbConnection()
app.secret_key = 'clave_secreta_simple'  # Clave secreta más segura en producción


#Rutas del aplicativo
@app.route('/')
def pagproductos():
    productos = db['productos']
    productsReceived = productos.find()
    return render_template('productos.html', productos=productsReceived)



@app.route ('/products', methods=['POST'])
def AgregarProducto():
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']

    if nombre and precio and stock:
        producto = producto(nombre, precio, stock)
        productos.insert_one(producto.toDBCollection)
        response = jsonify({
            'nombre' : nombre,
            'precio' : precio,
            'stock' : stock    })
        
        return redirect(url_for('pagproducto'))
    else:
        return notFound()



@app.route('/delete/<string:producto_nombre>')
def eliminar(producto_nombre):
    productos = db['productos']
    productos.delete_one({'nombre': producto_nombre})
    return redirect(url_for('pagproducto')) 



@app.route('/editar/<string:producto_nombre', methods=['POST'])
def editar(producto_nombre):
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']

    if nombre and precio and stock:
        productos.update_one({'name' : producto_nombre}, {'$set' : {'nombre': nombre, 'precio': precio, 'stock': stock}})
        response = jsonify({'message': 'producto' + producto_nombre + 'actualizado correctamente'})
        return redirect(url_for('pagproducto'))
    else: 
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message':'No encontrado' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code =404
    return response

        

if __name__ == '__main__':
    app.run(debug=True, port=5500)