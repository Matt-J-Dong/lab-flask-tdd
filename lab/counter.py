from flask import Flask

app = Flask(__name__) #le wut now

@app.route("/counters/<name>",methods="POST")
def create_counters(name):
    #creates a counter from the name
    