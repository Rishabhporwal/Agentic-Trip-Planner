from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
        This function returns a list of requirements from the 'requirements.txt' file.
    """

    requirement_list: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines = file.readlines()

            # Process each line
            for line in lines:
                # Strip whitespace and ignore empty lines
                requirement = line.strip()
                if requirement and requirement != '-e .' and not line.startswith('#'):
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirements.txt file not found.')

    return requirement_list

print(get_requirements())

setup(
    name= 'Agentic Trip Planner',
    version = '0.0.1',
    author= 'Rishabh Porwal',
    author_email= 'rishabhporwal95@gmail.com',
    description = 'An AI-based Trip Planner that helps users plan their trips efficiently by providing personalized recommendations and itineraries based on user preferences and interests.',
    packages=find_packages(),
    install_requires=get_requirements(),
)