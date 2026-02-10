from setuptools import setup, find_packages

setup(
    name="termitactoe",            # Package name
    version="0.1.0",               
    packages=find_packages(),      
    install_requires=[             
        "pytest>=7.0.0",
        "colorama>=0.4.6"
    ],
    entry_points={
        "console_scripts": [       
            "termitactoe=main:main"
        ]
    },
    python_requires=">=3.11",     
    description="Terminal-based multiplayer Tic-Tac-Toe game",
    author="Prasad Firame",
    license="MIT",
)
