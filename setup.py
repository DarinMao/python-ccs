from setuptools import setup

setup(name="ccs",
      version="0.8",
      description="Python wrapper for online CyberPatriot scoreboard",
      url="https://github.com/DarinMao/python-ccs/",
      author="Darin Mao",
      author_email="maodarin@gmail.com",
      license="MIT",
      packages=["ccs"],
      install_requires=[
         "requests",
         "bs4",
         "datetime"
      ],
      zip_safe=False)