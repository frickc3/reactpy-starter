from pathlib import Path
from reactpy import component, hooks, html, utils, web
from reactpy_router import link, route, simple
from reactpy.backend.fastapi import configure, Options
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from components import Product

META_SET = {'name': 'viewport',
           'content': 'width=device-width, initial-scale=1'
}

@component
def root():
    return simple.router(
        route("/", Product.Product()),
        route("*", html.h1("Missing Link 🔗‍💥")),
    )

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
configure(app,
          root,
          Options(
              html.head(
                  html.meta(META_SET),
                  html.link({'rel':'stylesheet', 'href':'/static/css/Base.css'}),
                  html.link({'rel':'stylesheet', 'href':'/static/css/App.css'}),
                  html.link({'rel':'stylesheet', 'href':'/static/css/Product.css'}),
                )
            )
         )

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
