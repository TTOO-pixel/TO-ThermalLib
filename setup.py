from setuptools import setup, find_packages

setup(
    name='thermalib',
    version='1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "qiskit",
        "scipy",
        "matplotlib"
    ],
    author="Investigador/a Anónimo/a",
    description="Implementación computacional del modelo TO para teleportación cuántica",
    license="MIT"
)