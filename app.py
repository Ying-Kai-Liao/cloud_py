
from flask import Flask
from flask import render_template

# Data of Posts
all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1. BlaBlaBla......',
        'author' : 'Rebecca'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2. BlaBlaBla......'
    }
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template("posts.html", posts = all_posts)

@app.route('/test')
def hello():
    return 'Hello, World!'

@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

@app.route('/readme')
def readme():
    return "This is a read me page. Please read me first!!"

@app.route('/readme')
def readme2():
    return "hehe, broken"

@app.route('/home/posts/<int:id>')
def hello2(id):
    return 'Hello, ' + str(id)

@app.route('/home/<string:name>/posts/<int:id>')
def hello3(name, id):
    return 'Hello, ' + name + ', your post id: ' + str(id)

@app.route('/home/<string:name>/<int:id>')
def hello4(name, id):
    return 'Hello, ' + name + ', your post id: ' + str(id)

if __name__ == '__main__':
    app.run()