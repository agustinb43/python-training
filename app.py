from router import app
from python_app import repository

#Start DB
repository.startup()

#Init flask app
print("Starting flask")
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000)


