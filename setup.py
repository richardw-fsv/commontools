from setuptools import setup, find_packages

# Function to read requirements from requirements.txt
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()
setup(
    name="rwcommontools",
    version="0.1.3",
    packages=find_packages(),
    install_requires=read_requirements(),
    author="RWest",
    description="A collection of common tools",
    python_requires=">=3.8",
)