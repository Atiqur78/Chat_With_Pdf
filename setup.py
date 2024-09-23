from setuptools import setup, find_packages

def get_requiremnts():
   
    requirements_list =[]
    try:
        with open("requirements.txt") as f:
            list = f.read()
            requirements_list = list.splitlines()
            requirements_list.remove("-e .")
    except FileNotFoundError as e:
        raise e
    return requirements_list

PROJECT_NAME = "Chat_With_Pdf"
AUTHOR_NAME = "Atiqur Rahman"
AUTHOR_EMAIL = "atikurrahman209@gmail.com"
VERSION = "0.1.0"

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requiremnts(),
)
