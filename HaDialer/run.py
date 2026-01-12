import os, requests, subprocess, time
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
        result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True)
        time.sleep(tmout)
        cmd = "adb shell input keyevent KEYCODE_ENDCALL"
        result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr, 500

app.run(host="0.0.0.0", port=8124)
