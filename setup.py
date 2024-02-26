from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    url="http://github.com/yourusername/myproject",
    author="Author Name",
    author_email="author@gmail.com",
    description="Description of my package",
    packages=find_packages(),    
    install_requires=[
        "inspect"
    ],
)