from flask import Flask, request, jsonify
import os

count = 0

app = Flask(__name__) 

@app.route("/")
def hello():
    return "Hello, frontpage!!"

@app.route("/query-example") # here we want to get the value of name (i.e. ?name=some-value)
def query_example():
    name = request.args.get('name', 'World!')
    return "Hello, {}".format(name)

@app.route("/count")
def display_count():
    global count
    count += 1
    return "The count is {} from pod {}".format(count, os.environ['MY_POD_NAME'])

@app.route("/env-var")
def env_var():
    return "This variable is from a ConfigMap - {}<br>This variable is from a Secret - {}".format(os.environ['ENV_VAR'], os.environ['ENV_SECRET'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True) #run app in debug mode on port 5000

