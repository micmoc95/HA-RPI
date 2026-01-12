import os, requests, logging, subprocess
from flask import Flask, request

SUPERVISOR = "http://supervisor"
TOKEN = os.environ["SUPERVISOR_TOKEN"]

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("hadialer")
log.info("Starting ...")

def ha(url, data=None):
    return requests.post(
        SUPERVISOR + url,
        headers={"Authorization": f"Bearer {TOKEN}"},
        json=data
    )

ha("/core/api/services/hadialer/dial", {
    "description": "Composition d'un numéro de téléphone",
    "fields": {
        "num": {"description":"Numéro à composer"}
    }
})

@app.route("/dial", methods=["POST"])
def dial():
    data = request.json or {}
    num = data.get("num")
    log.info("Numéro à composer: %s", num)
    try:
        cmd = "adb shell am start -a android.intent.action.CALL -d tel:" + f"num"
        result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True)
        log.info("Résultat : %s", result.stdout.strip())
        return result.stdout
    except subprocess.CalledProcessError as e:
        log.error("Erreur lors de l'exécution : %s", e.stderr)
        return e.stderr, 500

app.run(host="0.0.0.0", port=8124)
