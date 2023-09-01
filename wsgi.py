import os
from service import create_app

# Create the Flask app
app = create_app()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "8080")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
