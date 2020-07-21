import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="repsci",
    version="1.1.8",
    author="Edward L. Platt",
    author_email="ed@elplatt.com",
    description="A tool for reproducible scientific computing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elplatt/repsci",
    packages=['repsci'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
