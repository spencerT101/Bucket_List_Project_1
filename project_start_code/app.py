from flask import Flask, render_template

from controllers.bucket_list_controller import bucket_list_blueprint


app = Flask(__name__)

app.register_blueprint(bucket_list_blueprint)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()