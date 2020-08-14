setup(
    name="barcode-generator",
    version="1.0.0",
    description="Automatic generation of Code128 test barcodes",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Henk van Asselt",
    author_email="Henk.van.Asselt@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=[],
    # packages=["reader"],
    include_package_data=True,
    install_requires=[
        #"feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["barcode-generator.__main__:main"]},
)