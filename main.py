from flask import Flask, render_template, request
import requests
import smtplib

blog_response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
posts = blog_response.json()

app = Flask(__name__)

@app.route('/')
# @app.route('/index.html')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:num>')
def get_post(num):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_mail(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="shotokillua55@gmail.com", password="***")
        connection.sendmail(from_addr="shotokillua55@gmail.com", to_addrs="shotokillua55@gmail.com", msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)

