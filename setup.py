from setuptools import setup, find_packages

setup(
    name='PygameEnhanced',
    version='1.3',
    packages=find_packages(),
    include_package_data=True,  # This will include templates and static files
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'run-remote-python-executor = remote_python_executor.app:run_app',  # Command to run the app
        ],
    },
)