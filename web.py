
import base64
import cv2
import numpy as np
import time,json
from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

def base64_cv2(base64_str):
    imgString = base64.b64decode(base64_str)
    nparr = np.frombuffer(imgString,np.uint8)  
    image = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    return image


@app.route("/show/<filename>", methods=['GET'])
def show(filename):
    retval, buffer = cv2.imencode('.jpg', cv2.imread('static/'+filename))
    base64str = base64.b64encode(buffer).decode().replace('/','#')
    objs={'base64':base64str}
    response = json.dumps(objs)
    return response

@app.route("/upload", methods=['POST'])
def upload():
    bstring = request.form['base64']
    bstring1=bstring.replace("data:image/jpeg;base64,", "")
    img = base64_cv2(bstring1)
    filename = str(time.time()) + '.jpg'
    cv2.imwrite('static/' +filename , img)
    # print(response)
    return json.dumps({'base64':bstring1})


if __name__ == "__main__":


    app.run(host='0.0.0.0', port=8085, debug=True)