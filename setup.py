from setuptools import setup, find_packages

setup(
    name="auto-vuln-scanner",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["python-nmap"],
    entry_points={
        "console_scripts": [
            "auto-vuln-scanner=main:main",
        ]
    },
)