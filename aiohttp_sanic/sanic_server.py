from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)


@app.route('/')
async def index(request):
    return text("sanic server")


app.run(host="0.0.0.0", port=8000, debug=True)
