from setuptools import find_packages, setup

setup(
    name="mcq-generator",
    version='0.0.1',
    author='shankar wagh',
    author_email='shankarwagh297@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)