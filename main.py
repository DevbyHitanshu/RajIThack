
# import
from flask import Flask, render_template, request


# create server
server = Flask(__name__)

# configure
@server.get("/search")
def home():
    results = [1,2,3]
    query = request.form[]
    return render_template("home.html", context={"results": results})

# start
if __name__ == "__main__":
    server.run(debug=True, port=3000, host="127.0.0.1")