class DB:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:abc123@localhost/budget_app'
    SECRET_KEY = 'DirtySecret'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'


