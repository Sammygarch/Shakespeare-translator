import shakespeare_translate
from setuptools import setup


with open("README.rst", "r") as fp:
    long_description = fp.read()


setup(name="shakespeare_translate",
      version=shakespeare_translate.__version__,
      author="Sammy Garcia",
      author_email="s@mmygarcia.com",
      url="https://github.com/Sammygarch/Shakespeare-translator",
      py_modules=["shakespeare_translate"],
      description="Translate modern English into Shakespearean English",
      long_description=long_description,
      license="MIT",
      classifiers= [
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3"
                ],
      python_requires=">=3"
)
