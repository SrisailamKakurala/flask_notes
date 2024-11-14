from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')


# templates and template inheritance

@app.route('/')
def hello():
    var = 'hello jinja 2'
    mylist = [1, 2, 3, 4, 5]
    return render_template('index.html', var=var, mylist=mylist)

@app.route('/other')
def other():
    return render_template('other.html')


# filters

# Custom filter to count occurrences of a character in a string
@app.template_filter('count_char')
def count_char(value, char):
    return value.count(char)

@app.route('/filter')
def filter():
    text = 'Hello wOrld'
    return render_template('filter.html', text=text)


@app.route('/redirect-endpoint')
def redirect_endpoint():
    return redirect(url_for('other')) 
    # redirects to the /other endpoint




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)