import os, requests, subprocess
from flask import Flask, request

app = Flask(__name__)

def ha(url, data=None):
    return requests.post("http://supervisor" + url, headers={"Authorization": f"Bearer {os.environ["SUPERVISOR_TOKEN"]}"}, json=data)

ha("/core/api/services/hadialer/dial", {
    "description": "Composition d'un numéro de téléphone",
    "fields": {
        "num": {"description":"Numéro à composer"},
        "tmout": {"description":"Durée de l'appel"}
    }
})

@app.route("/dial", methods=["POST"])
def dial():
    data = request.json or {}
    num = data.get("num")
    tmout = data.get("tmout")
    try:
        cmd = f"adb shell am start -a android.intent.action.CALL -d tel:{num}"
        result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True, timeout=30)
        return result.stdout
    except subprocess.CalledProcessError as e:
        log.error("Erreur lors de l'exécution : %s", e.stderr)
        return e.stderr, 500

app.run(host="0.0.0.0", port=8124)
