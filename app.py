from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Brady Hammann! This is my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():  # put application's code here
    return render_template('about-css.html')

@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')

    return render_template('favorite-course.html', subject=subject, course_number=course_number)

if __name__ == '__main__':
    app.run()
