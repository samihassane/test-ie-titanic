from flask import Flask, request

app = Flask(__name__)  # flask needs a parameter


@app.route(
    "/"
)  # when the user reaches the home page, execute hello, world. It links the python function with WebApp
def hello():
    # request.args["name"] #Too strict, fails if name is not passed#object that will hold properties for us. Every connection coming from a client. Server give back a "response"
    # if "name" in request.args
    name = request.args.get("name")
    greeting = request.args.get("greeting", "Hello")
    if name is not None:
        return f"{greeting}, {name}!"
    else:
        return "Hello, stranger"
