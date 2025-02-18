from flask import Flask, request, jsonify, render_template, redirect, url_for, abort, flash # type: ignore

app = Flask(__name__)

# Configuración flash
app.secret_key = 'supersecretkey'

# Lista de tareas simulada
tareas = [
    {'id': 1, 'titulo': 'Aprender Python', 'hecho': True},
    {'id': 2, 'titulo': 'Configurar GitHub Actions', 'hecho': True},
    {'id': 3, 'titulo': 'Sacar 10 en esta práctica', 'hecho': False}
]

# Ruta para la página principal que muestra las tareas
@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

# Ruta GET: Obtener todas las tareas (API)
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify({'tareas': tareas})

# Ruta POST: Crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    titulo = request.form.get('titulo')
    if not titulo:
        return redirect(url_for('index'))
    tarea = {
        'id': tareas[-1]['id'] + 1 if tareas else 1,
        'titulo': titulo,
        'hecho': False
    }
    tareas.append(tarea)
    flash('Tarea agregada exitosamente.')  # Mensaje de éxito
    return redirect(url_for('index'))

# Ruta DELETE: Eliminar una tarea
@app.route('/tareas/<int:tarea_id>', methods=['POST'])
def eliminar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea is None:
        abort(404)
    tareas.remove(tarea)
    flash('Tarea eliminada exitosamente.')  # Mensaje de éxito
    return redirect(url_for('index'))

# Ruta PUT: Actualizar una tarea
@app.route('/tareas/<int:tarea_id>', methods=['POST'])
def actualizar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea is None:
        abort(404)

    tarea['hecho'] = True
    flash('Tarea marcada como hecha.')  # Mensaje de éxito
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
