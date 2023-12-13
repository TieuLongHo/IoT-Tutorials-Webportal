from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


def change_ssid(new_ssid):
    print(f"new ssid: {new_ssid}")


def change_password(new_password):
    print(f"new password: {new_password}")


def reboot():
    print("rebooting")
    subprocess.Popen(["sudo", "reboot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def get_current_ssid():
    try:
        result = subprocess.run(
            ["nmcli", "dev", "wifi", "list"], capture_output=True, text=True
        )

        output_lines = result.stdout.split("\n")
        for line in output_lines:
            if "*" in line:  # '*' indicates the connected network
                ssid = line.split()[0]
                return ssid
    except Exception as e:
        print(f"Error: {e}")
        return None


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/")
def index():
    print(get_current_ssid())
    return render_template("index.html")


@app.route("/change", methods=["POST"])
def change():
    if request.method == "POST":
        new_ssid = request.form["ssid"]
        new_password = request.form["password"]
        change_ssid(new_ssid)
        change_password(new_password)
        reboot()
        return "Changes applied successfully!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
