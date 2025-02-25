from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return 'Это главная venom.'

# @app.route('/about')
# def about():
# 	return 'Здесь будет venom об venom сайта.'

# @app.route('/blog')
# def blog():
# 	return 'Это venom с заметками о venom и venom.'


app.run(debug=True)
