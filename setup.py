from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PersonalGPT",
    version="0.1",
    author="Alon Kiriati",
    author_email="akiriati@hotmail.com",
    description="Create a personal GPT by scanning documents from a folder / website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akiriati/PersonalGPT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)