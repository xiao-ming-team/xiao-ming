from flask import Flask

app = Flask("xiao-ming")

@app.route("/")
def index():
    return "hello world"


if __name__ == "__main__":
    app.run()