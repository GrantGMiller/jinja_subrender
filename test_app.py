from flask import Flask, render_template
import jinja_subrender

app = Flask('test app')
app.register_blueprint(jinja_subrender.bp)


@app.route('/')
def Index():
    return render_template(
        'all_items.jinja',
        items=[
            {'name': f'name {i}', 'src': f'src {i}'} for i in range(5)
        ])


@app.route('/multiple_arguments')
def MultipleArguments():
    return render_template(
        'multiple_arguments.jinja',
        items=[
            {'name': f'name {i}', 'src': f'src {i}'} for i in range(5)
        ])


if __name__ == '__main__':
    app.run(debug=True)
