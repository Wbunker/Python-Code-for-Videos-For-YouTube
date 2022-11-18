from flask import request, Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    print("request.args",
            request.args)
    print("request.form",
        request.form)
    print("request.values",
        request.values)
    # this does not work
    # unless MIME not
    # recognized
    print("request.data", 
        request.data)
    return "We have you covered"

app.run(host='0.0.0.0', port=81)