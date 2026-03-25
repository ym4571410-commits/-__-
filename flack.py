from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="font-size: 40px; color: #007bff;">𝑨𝑫𝑨𝑴𝑽𝑰𝑷 𝑺𝑻𝑶𝑹𝑬</h1>
        <p style="font-size: 20px;">المتجر جاهز واشتغل أونلاين بنجاح!</p>
    </div>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

            
