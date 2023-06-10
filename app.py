from flask import Flask, render_template, request
from sorting import perform_sorting

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # retrieve the uploaded file
        file = request.files['file']

        # save the uploaded file
        file.save('uploaded_data.csv')

        # perform sorting and categorization
        data = perform_sorting('uploaded_data.csv')

        # render the template with the sorted data
        return render_template('result.html', data=data)

    # render the upload form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
