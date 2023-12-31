from setuptools import setup

setup(
    name='termoto',
    version='0.1.1',
    description='A terminal and system argument based pomodoro',
    author='Darshan Patil',
    author_email='drshnp@outlook.com',
    url='https://github.com/1darshanpatil/termoto.git',
    py_modules=['termoto'],
    install_requires=['win10toast'],
    entry_points={
        'console_scripts': [
            'pomodoro=main:run_pomo',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
