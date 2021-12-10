from .front.main_page import app


def main():
    return app.run_server(debug=True)
