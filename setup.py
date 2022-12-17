from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_dio",
    version="0.0.1",
    author="Marley Adriano",
    author_email="marleyasi@gmail.com",
    description="Project resulting from DIO 'Descomplicando a criação de pacotes de processamento de imagens em python' Lab.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marleyas/image-processing_dio.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)