from flask import Flask, render_template, send_file, request, redirect, url_for
from forms import FormSelector, FormFactory
from document_generator import DocumentGeneratorFactory, OutputFormat
from config import FormType, Config
from datetime import datetime
import os
import zipfile
import io

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def select_form():
    form = FormSelector()
    if form.validate_on_submit():
        form_type = FormType[form.form_type.data]
        return redirect(url_for('fill_form', form_type=form_type.name))
    return render_template('select_form.html', form=form)

@app.route('/form/<form_type>', methods=['GET', 'POST'])
def fill_form(form_type):
    form_type_enum = FormType[form_type]
    form = FormFactory.create_form(form_type_enum)
    
    if form.validate_on_submit():
        # Create form data dictionary
        form_data = {field.name: field.data for field in form}
        
        # Generate HTML document
        generator = DocumentGeneratorFactory.create_generator(
            form_type_enum, 
            form_data, 
            OutputFormat.HTML.value
        )
        html_content = generator.generate()
        
        # Return HTML content directly to be displayed in browser
        return html_content
    
    return render_template('form.html', form=form, form_type=form_type_enum.value)

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        # Get file extension
        ext = filename.split('.')[-1].lower()
        mime_types = {
            'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'markdown': 'text/markdown',
            'md': 'text/markdown',
            'html': 'text/html'
        }
        
        return send_file(
            os.path.join(app.config['UPLOAD_FOLDER'], filename),
            as_attachment=True,
            download_name=filename,
            mimetype=mime_types.get(ext, 'application/octet-stream')
        )
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True) 