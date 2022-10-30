from setuptools import setup

setup(
    name="burner",
    version="0.1.0",
    py_modules=["app"],
    install_requires=["Click", "requests", "beautifulsoup4"],
    entry_points={"console_scripts": ["burner = app:cli"]},
    package_data={"burner": ["sms.db"]},
    zip_safe=False,
)
