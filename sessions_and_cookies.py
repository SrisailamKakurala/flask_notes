from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'SOME SECRET KEY'

@app.route('/')
def index():
    return render_template('session.html')


@app.route('/set_session')
def set_session():
    session['name'] = 'ssl'
    return render_template('session.html', message='session set successfully')


@app.route('/get_session')
def get_session():
    if 'name' in session.keys():
        name = session['name']
        return render_template('session.html', message=f'session value is {name}')
    else:
        return render_template('session.html', message='session value is not set')
        
@app.route('/clear_session')
def clear_session():
    session.clear()
    # session.pop('particular session name')
    return render_template('session.html', message='session cleared successfully')



@app.route('/set_cookie')
def set_cookie():
    res = make_response(render_template('session.html', message='cookie set successfully'))
    res.set_cookie('cookie_name', 'cookie_value', expires=60)
    return res


@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('cookie_name')
    return render_template('session.html', message=f'cookie value is {cookie}')


@app.route('/clear_cookie')    
def clear_cookie():
    res = make_response(render_template('session.html', message='cookie cleared successfully'))
    res.delete_cookie('cookie_name')
    return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        password = request.form['pass']
        if name == 'ssl' and password == 'ssl':
            flash('login successful')
            return render_template('login.html', message='login successful')
        else:
            flash('login failed')
            return render_template('login.html', message='login failed')
        
        
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)