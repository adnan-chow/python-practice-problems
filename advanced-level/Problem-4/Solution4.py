from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for tasks (reset on server restart)
tasks = []
current_id = 1  # Auto-incrementing ID counter

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Return all tasks as JSON"""
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    """Add a new task from JSON input"""
    global current_id
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing "content" field'}), 400
    
    new_task = {
        'id': current_id,
        'content': data['content']
    }
    tasks.append(new_task)
    current_id += 1
    return jsonify(new_task), 201  # 201 = Created

@app.route('/tasks', methods=['DELETE'])
def delete_task():
    """Delete a task by ID (passed as query parameter)"""
    task_id = request.args.get('id')
    
    if not task_id:
        return jsonify({'error': 'Missing "id" parameter'}), 400
    
    try:
        task_id = int(task_id)
    except ValueError:
        return jsonify({'error': 'Invalid "id" format'}), 400
    
    for index, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted_task = tasks.pop(index)
            return jsonify({'message': 'Task deleted', 'task': deleted_task}), 200
    
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)