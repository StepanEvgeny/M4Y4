#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_html=button_html,button_db=button_db)

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/submit',methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
    with open('forms.txt', 'a',) as f:
            f.write(name+'\n')
            f.write(email+'\n')
            f.write(address+'\n')
            f.write(date+'\n')
    return render_template('forms.text',
                           name=name,
                           email=email,
                           address=address,
                           date=date
                           )
app.run(debug=True)