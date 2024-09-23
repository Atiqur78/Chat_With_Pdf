# Chat With PDF
================

A project that enables users to chat with PDF files.

## Description
---------------

This project aims to provide a innovative way of interacting with PDF files by allowing users to chat with them.

## Getting Started
-------------------

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/Atiqur78/Chat_With_Pdf.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create .env file and write the required API_KEY
4. Run the application: `python main.py`

Api Testing
------------

document_upload: curl -X POST -F "chat_name=example" -F "file=@path/to/document.pdf" http://localhost:5000/upload

query: curl -X POST -d "query_chat_name=example&question=What is the main topic?" http://localhost:5000/query



## Authors
-----------

* [Atiqur Rahman]