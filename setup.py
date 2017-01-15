from setuptools import setup

setup(
    name="hue-client",
    version="0.1",
    packages=["app"],
    install_requires=[
        "click",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "hue-client = app.app:main"
        ]
    }
)
