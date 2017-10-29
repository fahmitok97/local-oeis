from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/find',methods = ['GET'])
def find():
	query = request.args.get('q')
	data = __get_matching_sequence(query)
	return render_template('display.html', data = data)

def __clean_ctx(ctx):
	cleaned = ""
	for elem in ctx:
		if not(elem == " " or elem == ",") :
			cleaned += elem
	return cleaned

def __get_matching_sequence(query):
	result = []
	cleaned_query = __clean_ctx(query)

	with open('result.json') as data_file:
		data = json.load(data_file)

		for elem in data:
			cleaned_element = __clean_ctx(elem['sequence'])
			if(cleaned_query in cleaned_element):
				result.append(elem)

	return result

if __name__ == '__main__':
	app.run()
