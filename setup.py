import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="cem",
    version="1.2.0",
    author=("Mateo Espinosa Zarlenga, Pietro Barbiero, Gabriele Ciravegna, Giuseppe Marra, "
            "Francesco Giannini, Michelangelo Diligenti, Zohreh Shams, Frederic Precioso, Stefano Melacci, "
            "Adrian Weller, Pietro Lio, Mateja Jamnik"),
    author_email="me466@cam.ac.uk",
    description="Concept Embedding Model",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/mateoespinosa/cem",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    python_requires='>=3.7',
    install_requires=[
        "joblib",
        "jupyter",
        "matplotlib",
        "lightning",
        "scikit-learn-extra",
        "scikit-learn",
        "seaborn",
        "torch",
        "torchmetrics",
        "torchvision",
        "tensorflow",
        "prettytable"
    ],
)
