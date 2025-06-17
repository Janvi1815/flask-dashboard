from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ✅ New: Temporary storage for blog posts
blog_posts = []

@app.route('/')
def home():
    return render_template('regist.html', posts=blog_posts)  # 👈 Pass posts to template

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return redirect(url_for('success', name=name, email=email, password=password))

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    return render_template('success.html', name=name, email=email, password=password)

@app.route('/home')
def home_page():
    return render_template('home.html')  # Your home.html page

# ✅ New: Add blog post route
@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    blog_posts.append({'title': title, 'content': content})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
