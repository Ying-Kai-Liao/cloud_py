
from flask import Flask

print(__name__)
app = Flask(__name__)


@app.route('/')
@app.route('/test')
def hello():
    return 'Hello, World!'

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

@app.route('/')

if __name__ == '__main__':
    app.run()