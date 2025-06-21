import serial
import flask
import flask_cors

serialPort: serial.Serial = serial.Serial("/dev/ttyACM0")

app: flask.Flask = flask.Flask("arduino-practice", template_folder="static")
flask_cors.CORS(app)

@app.route("/")
def rootHandler() -> flask.Response:
    return flask.render_template("index.html")

@app.route("/api/v1/getTemperature")
def temperatureHandler() -> flask.Response:
    return flask.jsonify({"LM75A": serialPort.readline().decode("utf-8")[:-2]})

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