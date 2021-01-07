import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-hectormao1025",
    version="0.0.1",
    author="Hector Mao",
    author_email="hectormao1025@gmail.com",
    description="A sample python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HectorNet/python-package-sample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
