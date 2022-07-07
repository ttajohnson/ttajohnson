from website import create_app # __init__.py file changes the website folder into a python package

app = create_app() 

if __name__ == '__main__': # only if we run this file will we run the webserver
    app.run(debug=True) # runs the Flask app webserver, starts a webserver, debug=True means if any py code is changed it will auto re-run the webserver
    