from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        
        # Valor tarro
        valor_tarro = 9000
        total_normal = cantidad * valor_tarro
        
        # Descuentos
        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0
            
        descuento = total_normal * porcentaje_descuento
        total_descuento = total_normal - descuento
        
        resultado = {
            'nombre': nombre,
            'total_normal': int(total_normal),
            'descuento': float(descuento),
            'total_descuento': float(total_descuento)
        }
        return render_template('ejercicio1.html', resultado=resultado, nombre=nombre, edad=edad, cantidad=cantidad)
        
    return render_template('ejercicio1.html', resultado=None)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']
        
        # Verificación de usuarios estáticos
        if usuario == "juan" and clave == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and clave == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
            
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
