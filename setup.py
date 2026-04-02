from setuptools import setup, find_namespace_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    this function will return list of requirements    
    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read all lines
            lines = file.readlines()

            # process each line
            for line in lines:
                requirement = line.strip()

                # ignore empty line and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")  

    return requirement_lst      

setup(
    name="Network security",
    version="0.0.1",
    author="Jeet kumar gupta",
    author_email="jeetkumargupta828404@gmail.com",
    packages=find_namespace_packages(),
    install_requires= get_requirements()
)