
def configure_app(app):
    app.config['MYSQL_HOST'] = ''
    app.config['MYSQL_USER'] = ''
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = ''
    app.config['MYSQL_CURSORCLASS'] = "DictCursor"

