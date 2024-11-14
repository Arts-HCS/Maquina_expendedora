from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

display = "" 
products = []
unidades = 1

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html', display=display, products=products, unidades=unidades)


@app.route('/upload', methods=["POST", "GET"])
def upload():
    global display, products, unidades
    if request.method == "POST":
        value = request.form["button"]
        if value == "Sel":
            if request.method == "POST":
                if display == "0" or display=="" or int(display)>40:
                    error2 = "Número fuera de rango"
                    display = ""
                    return render_template('index.html', error2=error2, products=products, unidades=unidades)
                name = "drink"+display
                if products.count(name) >=unidades: 
                    error = "No hay más unidades"
                    display = ""
                    return render_template('index.html', error=error, products=products, unidades=unidades)
                products.append(name)
                drink_value = request.form[name]
                display = ""
                return render_template('index.html', drink_value=drink_value, products=products, unidades=unidades)
        elif value == "fproduct":
            display = ""
            mensaje = "Tomaste un producto"    
            return render_template('index.html', products=products, unidades=unidades, mensaje=mensaje)    
        elif value == "C":
            display = ""
        elif value == "R":
            display = display[:-1]
        else:
            display += value
        
        return render_template('index.html', display=display, products=products, unidades=unidades)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
