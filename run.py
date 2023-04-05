from app import get_app

if __name__ == "__main__":
    app = get_app()
    app.run(port=5010, debug=True)