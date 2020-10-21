class BaseConfig:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///notefy.db'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx', 'pptx'}
    UPLOAD_FOLDER = 'notefy/uploads'
    DEBUG = False


class DevelopmentConfig(BaseConfig):

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig(BaseConfig):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


config = DevelopmentConfig
