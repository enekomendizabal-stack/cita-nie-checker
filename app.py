from flask import Flask
import urllib.request
import time

app = Flask(__name__)

URL = "https://sede.administracionespublicas.gob.es/icpplus/index"

def comprobar():
    try:
        r = urllib.request.urlopen(URL, timeout=20).read().decode("utf-8", "ignore").lower()
        if "no hay citas" in r or "no hay citas disponibles" in r:
            return "❌ No hay citas disponibles."
        else:
            return "✅ Posible disponibilidad: revisa la web manualmente."
    except Exception as e:
        return f"⚠️ Error al conectar: {e}"

@app.route("/")
def index():
    resultado = comprobar()
    hora = time.strftime("%H:%M:%S")
    html = f"""
    <html>
      <head><title>Comprobador de Citas NIE</title></head>
      <body style="font-family:Arial; text-align:center; margin-top:50px;">
        <h1>Comprobador de Citas NIE</h1>
        <h2>{resultado}</h2>
        <p>Última comprobación: {hora}</p>
        <p><a href="/">🔄 Actualizar</a></p>
      </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
