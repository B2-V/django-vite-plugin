from setuptools import setup, find_packages

setup(
    name="django_vite_plugin",
    version="4.1.1_dev",
    description="Custom django-vite-plugin",
    long_description=open("django/README.md").read(),
    long_description_content_type="text/markdown",
    author="Stepan Stanchev",
    url="https://github.com/B2-V/django-vite-plugin",
    package_dir={"": "django/src"},
    packages=find_packages(where="django/src"),
    include_package_data=True,
    install_requires=[
        "Django>=3.10",
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
)
