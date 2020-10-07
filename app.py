from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Post(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(255), nullable = False)
	content = db.Column(db.Text,nullable = False)
	created = db.Column(db.DateTime, default = datetime.utcnow)

	def __repr__(self):
		return '<Title "{}">'.format(self.title)



#Controleur
@app.route('/')
def home():
	return render_template('home.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/blog')
def blog():
	posts = Post.query.all()
	return render_template('blog.html',posts=posts)

@app.route('/blog/posts/<int:id>')
def posts_show(id):
	post = Post.query.get(id)
	return render_template('show.html',post=post)


@app.errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'),404


if __name__ == "__main__":
	db.create_all()
	app.run(debug = True)
