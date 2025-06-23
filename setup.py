import setuptools

requirements = [
    "fastapi==0.111.0",
    "uvicorn",
    "sqlalchemy",
    "psycopg2-binary",
    "pydantic-settings",
    "python-dotenv"
]

setuptools.setup(
    name="railway-service",
    version="0.1.0",
    setup_requires=["pip"],
    install_requires=requirements,
    packages=setuptools.find_packages(),
)

