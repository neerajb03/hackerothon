from flask import Flask
import os

app = Flask(__name__)

logfile = "logs.txt"

@app.route("/trigger", methods=["POST", "GET"])
def trigger():
    if os.path.exists(logfile):
            os.remove(logfile)
            return "logs cleared",200
        
    else:
        return "logs not found",404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
