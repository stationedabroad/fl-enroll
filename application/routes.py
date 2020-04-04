from application import app

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Server test one ...</h1>"