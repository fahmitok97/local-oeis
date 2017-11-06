from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/ieos')
def home():
	return render_template('index.html')

@app.route('/ieos/find',methods = ['POST'])
def find():
	query = request.form['q']
	data = __get_matching_sequence(query)
	return render_template('display.html', data = data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def __clean_ctx(ctx):
	cleaned = []
	word = ""

	for elem in ctx:
		if (elem == " " or elem == ",") :
			if word != "" :
				cleaned.append(int(word))
				word = ""

		elif ( ord(elem) >= ord('0') and ord(elem) <= ord('9') ) :
			word += elem

	if word != "" :
		cleaned.append(int(word))
		word = ""

	return cleaned

def __is_match(query, document):
	doc_idx = 0
	for elem in query :
		if doc_idx >= len(document) :
			return False

		while document[doc_idx] != elem :
			doc_idx += 1
			if doc_idx >= len(document) :
				return False

		doc_idx += 1

	return True

def __get_matching_sequence(query):
	result = []
	cleaned_query = __clean_ctx(query)

	with open('result.json') as data_file:
		data = json.load(data_file)
		can = True

		for elem in data:
			cleaned_element = __clean_ctx(elem['sequence'])
			if(can):
				can = False

			if(__is_match(cleaned_query, cleaned_element)):
				result.append(elem)

	return result[:10]

if __name__ == '__main__':
	app.run()
