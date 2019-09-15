import setuptools


setuptools.setup(
    name="stakeholders",
    version="0.1.1",
    author="critical-path",
    url="https://github.com/critical-path/stakeholders",
    description="Manage stakeholders like a pro!",
    license="MIT",
    keywords="pmbok project-management stakeholder-management stakeholders",
    packages=setuptools.find_packages(),
    package_data={
        "stakeholders": [
            "static/css/*",
            "static/js/*",
            "static/svg/*",
            "templates/*"
        ]
    },
    python=">=3.6",
    install_requires=[
        "flask",
        "gunicorn",
        "requests"
    ],
    extras_require={
        "test": [
            "coveralls",
            "pytest",
            "pytest-cov",
            "selenium"
        ]
    }
)
