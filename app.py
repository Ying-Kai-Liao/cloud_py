import os
import logging
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
db_url = os.getenv('POSTGRES_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace('postgres://', 'postgresql://', 1)

db = SQLAlchemy(app)

# DataBase Config
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text,nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return 'Blog post ' + str(self.id)
    
def init_db():
    print ('initiated')
    with app.app_context():
        db.create_all()
        
@app.route('/test_connection')
def test_connection():
    try:
        # Query the database, this will throw an exception if the database is not accessible
        result = db.session.execute(text("SELECT 1"))
        return 'Database connection successful', 200
    except Exception as e:
        # Log the exception to your logs (consider using app.logger.error)
        return str(e), 500

# Default Route
@app.route('/')
def index():
    return render_template('index.html')

# POSTS
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    
    if request.method == 'POST':
        print ('hi_there')
        post_title = request.form['title']
        post_author = request.form['author']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("posts.html", posts = all_posts)
    
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    post = BlogPost.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)

# OTHERS
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/readme')
def readme():
    return "This is a read me page. Please read me first!!"

# TESTS
@app.route('/test')
def hello():
    return 'Hello, World!'

@app.route('/home/posts/<int:id>')
def hello2(id):
    return 'Hello, ' + str(id)

@app.route('/home/<string:name>/posts/<int:id>')
def hello3(name, id):
    return 'Hello, ' + name + ', your post id: ' + str(id)

@app.route('/home/<string:name>/<int:id>')
def hello4(name, id):
    return 'Hello, ' + name + ', your post id: ' + str(id)

init_db()
    
if __name__ == '__main__':
    app.run()