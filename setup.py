import setuptools

setuptools.setup(
    include_package_data=True,
    name='chase',
    # Project Version
    version='1.0',
    # Description of your Package
    description='wolf and sheeps simulation',
    # Website for your Project or Github repo
    # Name of the Creator
    author='Piotr Zuchowski',
    # Projects you want to include in your Package
    packages=setuptools.find_packages(),

    # Classifiers allow your Package to be categorized based on functionality
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
