import config
from models import Subscription

app = config.connex_app
app.add_api(config.basedir / "swagger.yaml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)