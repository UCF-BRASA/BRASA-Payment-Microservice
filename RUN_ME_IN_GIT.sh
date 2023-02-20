#!/bin/bash

# contants
NC='\033[0m' # No Color
RED='\033[0;31m' 
GREEN='\033[0;32m' 

############################################
# Install 'pip' and asks user to validate the installation
# GLOBALS:
#   (No Global Variables used)
# ARGUMENTS:
#   (No Arguments)
# OUTPUTS:
#   Indicates next steps to user
# RETURN:
#   0 if print succeeds, non-zero on error.
############################################
function install_and_validate_pip()
{
  echo "Running curl command to get 'get-pip.py' file"
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

  echo "Running 'python get-pip.py' file"
  python get-pip.py

  echo ""
  echo -e "${RED}Open another terminal window and check if 'pip --version' returns something.${NC}"
  echo "Is pip properly installed? [Y/n]"

  while [ true ] 
  do
    read USER_ANS

    if [ "${USER_ANS}" == "Y" ] || [ "${USER_ANS}" == "y" ]
    then
      echo "Continuing with script..."
      rm get-pip.py
      return 0

    elif [ "${USER_ANS}" == "N" ] || [ "${USER_ANS}" == "n" ]
    then
      echo "Follow the steps in the following page: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/"
      rm get-pip.py
      return 0

    else
      echo ""
      echo -e "${RED}Invalid Input ${NC}"
      echo "Is pip properly installed [Y/n]"
    fi
  done
}


############################################
# Install packages
# GLOBALS:
#   (No Global Variables used)
# ARGUMENTS:
#   (No Arguments)
# OUTPUTS:
#   Indicates next steps to user
# RETURN:
#   0 if print succeeds, non-zero on error.
############################################
function install_packages() 
{
  # install pipenv package
  pip install pipenv

  # install all the project's packages
  python -m pipenv install
}


############################################################################################################################################################################################################################


# 1. Install pip 
install_and_validate_pip

# 2. Install all required packages
install_packages
