from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME ="Sachin Borse"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS =['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email="shubham.ade122020@gcoeara.ac.in",
    description='A Simple Python Package To Make a simple Web App',
    long_description=long_description,
    long_description_content_type ='text/markdown',
    package=[SRC_REPO],
    python_requries =">=3.12",
    install_requries =LIST_OF_REQUIREMENTS,
)