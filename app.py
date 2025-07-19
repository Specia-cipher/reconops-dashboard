from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🔍 ReconOps Dashboard is live! Start building your recon modules here."

if __name__ == '__main__':
    app.run(debug=True)
