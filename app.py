from flask import Flask, render_template, request

app = Flask(__name__)


def change_ssid(new_ssid):
    print(f"new ssid: {new_ssid}")


def change_password(new_password):
    print(f"new password: {new_password}")


def reboot():
    print("rebooting")


@app.route("/")
def index():
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
