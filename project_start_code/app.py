from flask import Flask, render_template

from controllers.bucket_list_controller import destinations_blueprint
from controllers.destination_controller import city_destinations_blueprint


app = Flask(__name__)

app.register_blueprint(country_blueprint)
app.register_blueprint(destinations_blueprint)
app.register_blueprint(city_destinations_blueprint)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()