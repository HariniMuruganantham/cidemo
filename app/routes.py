from flask import Flask, jsonify
import os
import psycopg2

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        db_url = os.getenv("DATABASE_URL", "sqlite:///:memory:")
        try:
            # Only try to connect if using Postgres
            if db_url.startswith("postgres"):
                conn = psycopg2.connect(db_url)
                cursor = conn.cursor()
                cursor.execute("SELECT version();")
                version = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                return jsonify({"message": "Connected to PostgreSQL!", "version": version})
            else:
                return jsonify({"message": "Using default SQLite memory DB."})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app
