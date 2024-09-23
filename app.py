from flask import Flask, request, render_template, redirect, url_for, jsonify
from src.document_upload import handle_document_upload
from src.document_query import handle_document_query
from src.logger import logging
from src.exception import CustomException
import sys


app = Flask(__name__)
app.secret_key = 'your_secret_key'




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_document():
    try:
        if 'file' not in request.files or 'chat_name' not in request.form:
            logging.info('Missing file or chat name', 'error')
            return redirect(url_for('index'))

        uploaded_file = request.files['file']
        chat_name = request.form['chat_name']
        
        if uploaded_file.filename == '':
            logging.error('No file selected', 'error')
            return redirect(url_for('index'))

        handle_document_upload(uploaded_file, chat_name)
        logging.info('Document indexed successfully', 'success')

    except Exception as e:
        logging.error(f"Error during document upload: {str(e)}")
        raise CustomException(e, sys)

    return redirect(url_for('index'))


@app.route('/query', methods=['POST'])
def query_document():
    try:
        chat_name = request.form.get('query_chat_name')
        question = request.form.get('question')

        if not chat_name or not question:
            logging.info('Missing chat name or question', 'error')
            return redirect(url_for('index'))


        answer = handle_document_query(chat_name, question)
        logging.info(f"Answer: {answer}", 'success')
        return render_template('index.html', answer=answer)

    except Exception as e:
        logging.error(f"Error during document query: {str(e)}")
        raise CustomException(e, sys)


if __name__ == '__main__':
    app.run(debug=True)
