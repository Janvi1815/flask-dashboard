from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1, 10)
    now = datetime.now()
    copyright_text = f"© {now.year} Janvi Bhatt. All rights reserved."
    return render_template(
        'jinjademo.html',
        num=random_num,
        current_time=now,
        copyright=copyright_text
    )

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blogs = response.json()

    # ✅ Pass all blogs, filter ID=2 in blog.html using for loop
    return render_template("blog.html", blogs=blogs)

@app.route('/guess/<name>')
def guess(name):
    guess_url = f"https://api.genderize.io?name={name}"
    guess_response = requests.get(guess_url)
    guess_data = guess_response.json()
    gender = guess_data['gender']

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']

    return render_template('guess.html', p_name=name, p_gender=gender, p1_age=age)

if __name__ == '__main__':
    app.run(debug=True)
