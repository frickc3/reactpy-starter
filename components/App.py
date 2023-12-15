from reactpy import component, hooks, html, utils, web

@component
def App():
    return html.div(
        html.h1('Got to App.py'),
    )
