from flask import Flask
import os
import sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"+str(sys.argv[1])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

#subnet-0582ba2543a088175