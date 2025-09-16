from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from somador3000.functions import soma_3_mil

app = FastAPI()


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/soma-3-mil")
def soma_3_mil_endpoint(x: int = 0):
    """Endpoint que retorna x somado a 3000."""
    return {"resultado": soma_3_mil(x)}
