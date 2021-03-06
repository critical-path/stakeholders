import setuptools


setuptools.setup(
    name="stakeholders",
    version="0.1.6",
    author="critical-path",
    url="https://github.com/critical-path/stakeholders",
    description="Manage stakeholders like a pro!",
    license="MIT",
    keywords="python pmbok project-management stakeholder-management stakeholders",
    packages=setuptools.find_packages(),
    package_data={
        "stakeholders": [
            "static/css/*",
            "static/js/*",
            "static/svg/*",
            "templates/*"
        ]
    },
    install_requires=[
        "flask",
        "gunicorn==19.9.0",
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
