from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form.get('new_task')
    if new_task:
        tasks.append(new_task)
    return redirect(url_for('index'))


@app.route('/delete_task/<task_id>', methods=['POST'])
def delete_task(task_id):
    task_id = int(task_id)
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)