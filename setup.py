from setuptools import setup, find_packages

setup(
    name = "pylama_print",
    version ='0.9.1',
    author = "Geotob",
    packages = find_packages(),
    zip_safe = False,
    install_requires=[],
    setup_requires=['pytest-runner', 'pylama'],
    tests_require=['pytest', 'pylama'],
    entry_points={
        'pylama.linter': ['print = pylama_print.linter_print:Linter'],
    }
)
