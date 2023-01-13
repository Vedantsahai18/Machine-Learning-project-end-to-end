from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Balaji haridasan"
DESRCIPTION="This is a my full scale Machine Learning Project"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."  # to run the packages in the requirements.txt


def get_requirements_list() -> List[str]: # return output of the function as list
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines() # readlines in the requirments.txt file
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list] # 
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(),  
install_requires=get_requirements_list() # install required library 
)