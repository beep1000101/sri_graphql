from app_factory import create_app
from config import get_flask_config, DevelopmentConfig

# flask_config = get_flask_config()
# app = create_app(flask_config)
app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run()
