from flask import Flask, render_template
func_name = __name__
app = Flask(func_name)

@app.route("/")
def site():
    return render_template("index.html")

if func_name == "__main__":
    app.run(debug=True)