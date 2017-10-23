"""This is a setup file."""


from setuptools import setup
setup(
    name="linked_list",
    description="Command-line script used to track donations and \
    write thank you notes.",
    py_modules=['linked_list'],
    install_requires=[
    ],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
