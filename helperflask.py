from flask import Flask, render_template
import CMBX_FUNC_LIVE
import os

app = Flask(__name__)
#@app.route('/')
#def sum_table():
#    return CMBX_FUNC_LIVE.web_tool_cmbx()

@app.route('/',methods=["GET", "POST"])
def temp():
    return render_template('index.html',tables=[CMBX_FUNC_LIVE.web_tool_cmbx().to_html(classes='data', header="true")])


#app.run()
#app.run(host=socket.gethostbyname(socket.gethostname()))
#app.run(host='0.0.0.0', debug=True, port=3134,use_reloader=False)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
