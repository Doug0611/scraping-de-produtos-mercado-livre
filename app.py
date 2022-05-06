from flask import Flask, render_template, redirect
from controller import soup


scrapy = Flask(__name__, template_folder='templates', static_folder='static')
scrapy.debug = True
scrapy.env = 'development'

@scrapy.route('/')
@scrapy.route('/Day Promotion')
def index():
     
    return render_template('index.html', soup=soup())

if __name__ == '__main__':
    scrapy.run()