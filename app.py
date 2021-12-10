from cryptovwap.front.main_page import app


if __name__ == "__main__":
    server = app.server
    app.run_server(debug=True)
