from flask import Flask
from flask import render_template, request
from database import get_all_cats, get_cat_by_id, create_cat


app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
@app.route('/cats/<int:id>')
def view_details(id):
	cats= get_cat_by_id(id)
	return render_template("cat.html", cat=cats)
@app.route('/create_cat',methods=['GET','POST'])
def addpage():
	if request.method=='GET':
		return render_template("add.html")
	else:
		name= request.form['firstname']
		create_cat(name)
		cats= get_all_cats()
		return render_template('home.html',cats=cats)

if __name__ == '__main__':
	app.run(debug = True)
