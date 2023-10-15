from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import uvicorn

app = FastAPI()
app.mount("/", StaticFiles(directory="html", html=True), name="static")

# Adicionando middleware para habilitar o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_index():
    return HTMLResponse(
        open("index.html", "r", encoding="utf-8").read(), status_code=200
    )


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
