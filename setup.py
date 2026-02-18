from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    this function will return list of requirements
    
    """
    requiement_lst: List[str] = []

    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()

            for line in lines:
                requiement=line.strip()
                if requiement and requiement!= '-e .':
                    requiement_lst.append(requiement)

    except FileNotFoundError:
        print(f"Error: requirements.txt not found at path {file_path}")
    return requiement_lst

print(get_requirements('requirements.txt'))


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Om Mishra',
    author_email='om.mishra.2410@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)