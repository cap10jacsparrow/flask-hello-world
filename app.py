# ---- Flask Hello World ----- #
# import the Flask class from the Flask pkg

from flask import Flask

# Create the application object
app = Flask(__name__)

# Use decorator pattern to link the view function of the url
@app.route("/")
@app.route("/hello")


# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()
