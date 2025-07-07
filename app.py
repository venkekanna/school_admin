from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # School admin page with personal details
    student = {
        'name': 'Venkatesh',
        'age': 14,
        'class': '8th Grade',
        'school': 'Sunshine Public School'
    }
    return render_template('index.html', student=student)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
