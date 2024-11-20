from setuptools import setup

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

setup(
    install_requires=parse_requirements("requirements.txt"),
)
