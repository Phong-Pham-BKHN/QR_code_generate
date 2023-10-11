from flask import Flask, render_template, request, send_file
import qrcode
import os
#from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form.get('data')
    #filename = f'{data}.png'
    filename = f'qrcode.png'
    filepath = os.path.join('static', filename)
    
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    # logo = Image.open('image/lamhai01.png')
    # basewidth = 100
    # wpercent = (basewidth/float(logo.size[0]))
    # hsize = int((float(logo.size[1])*float(wpercent)))
    # logo = logo.resize((basewidth, hsize))
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    # img.paste(logo, pos)
    img.save(filepath)
    
    return filename

@app.route('/download_qr/<filename>', methods=['GET'])
def download_qr(filename):
    filepath = os.path.join('static', filename)
    return send_file(filepath, as_attachment=True, download_name=f'{filename}')

if __name__ == '__main__':
    app.run(port=5001, host="0.0.0.0", debug=True)
