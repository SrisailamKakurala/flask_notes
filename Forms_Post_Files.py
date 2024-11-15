from flask import Flask, render_template, request, Response, jsonify
import pandas as pd

app = Flask(__name__, template_folder='templates')


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
        if name == 'ssl' and password == 'ssl':
            return "success"
        else:
            return "failed"
        


# In Flask, url_for() in html requires an endpoint name to generate URLs. 
# By default, this endpoint is the name of the view function, but 
# you can specify a different endpoint name using the `endpoint` parameter 
# in @app.route. This allows url_for() to search for a route with a matching endpoint.
# In short: The route is the URL path, while the endpoint is the identifier used to refer to that route in Flask's code.
@app.route('/file_uploads', methods=['POST'], endpoint='file_uploads')
def upload():
    file = request.files['filename']
    
    if file.content_type == 'application/text/plain':
        return file.read().decode('utf-8')
    if file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    if file.content_type == 'text/csv':
        df = pd.read_csv(file)
        return df.to_html()
    
    
@app.route('/convert_excel', methods=['POST'])
def convert_excel():
    file = request.files['filename']
    
    if file.content_type == 'text/csv' or file.content_type == '.csv':
        df = pd.read_csv(file)
        xl = df.to_excel(excel_writer='converted_file.xlsx')
        res = Response(
            xl, 
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition':'attachment;filename=converted_file.xlsx'}
        )
        
        return res
 
 


@app.route('/json_request', methods=['POST'])
def json_request():
    name = request.json['name']
    greeting = request.json['greeting']
    
    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')
    
    return jsonify({ 'message': 'file written successfully'})

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)