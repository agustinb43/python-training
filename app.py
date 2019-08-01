from db import startup
from router import app
import logging.config

#Start DB
startup()

#Start Logger
logging.config.fileConfig('logging.conf')

#Init flask app
print("Starting flask")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


