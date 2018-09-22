from flask import Flask, jsonify, redirect

# Create flask app
app = Flask(__name__)

# Create who am i endpoint
@app.route('/who-am-i')
def who_am_i():
	data = {"message": "I am 'umbriel' microservice"}
	response = jsonify(data)
	return response

# Run the app
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=7081)
