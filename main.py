import serial
import flask
import flask_cors
import random

serialPort: serial.Serial = serial.Serial("/dev/ttyACM0")

app: flask.Flask = flask.Flask("arduino-practice", template_folder="static")
flask_cors.CORS(app)

@app.route("/")
def rootHandler() -> flask.Response:
    return flask.render_template("index.html", info=serialPort.readline().decode("utf-8")[:-2])

@app.route("/api/v1/getTemperature")
def temperatureHandler() -> flask.Response:
    return flask.jsonify({"LM75A": str(random.randint(0, 30))})

def main() -> None:
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        if serialPort.is_open():
            serialPort.close()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()