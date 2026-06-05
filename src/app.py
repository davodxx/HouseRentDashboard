from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/echo", methods=["POST"])
def echo():
    user_text = request.form["user_input"]
    return render_template(
        "result.html",
        text=user_text
    )

if __name__ == "__main__":
    app.run(debug=True)