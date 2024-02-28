import requests
from flask import Flask, render_template

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)