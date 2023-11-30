from fastapi import FastAPI
import datetime
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    html = """
    <html>
    <head>
        <title>Rozwiązanie zadania PZC 2.1</title>
    </head>
    <body>
    """
    html += datetime.datetime.now()
    html +=  """
    </body>
    """

    return html
