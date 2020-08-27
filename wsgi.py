from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "I like you!"

if __name__ == "__main__":
    application.run()
