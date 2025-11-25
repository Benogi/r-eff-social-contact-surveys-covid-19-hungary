from dashboard.application.main_app import app
import dashboard.application.main_app_callbacks # szükséges import, akkor is ha szürke

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8050', debug=True)
