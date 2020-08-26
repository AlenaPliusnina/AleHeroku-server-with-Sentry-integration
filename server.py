import os
import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

from dotenv import load_dotenv
load_dotenv()

# Интеграция с Sentry. Переменная DSN_ENV в файле .env
sentry_sdk.init(
    dsn=os.environ['DSN_ENV'],
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route("/")
def general_func():
    return "/"


@app.route("/success")
def success_func():
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <title>Heroku server</title>
      </head>
      <body>
        <div class="container">
          <h1>Ошибок не обноружено!</h1>
          <h3>success HTTP -  200 OK</h3>
        </div>
      </body>
    </html>
    """
    return html


@app.route("/fail")
def fail_func():
    raise RuntimeError("There is an error!")
    return


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
