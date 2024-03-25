from setuptools import setup, find_packages
from typing import List

# Function to read the requirements from the requirements.txt file
# remove "-e ." from the requirements
def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        requirements = [line.strip() for line in lines if line.strip() and not line.startswith('-e')]
    return requirements
get_requirements('requirements.txt')
    
    
setup(
    
    name = "mlproject1",
    version = "0.1",
    author="Arash",
    author_email="arash.d83@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)