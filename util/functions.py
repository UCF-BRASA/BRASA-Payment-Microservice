
import json
import sys
from bson import json_util
from termcolor import colored

# def get_base_prefix_compat():
#     """Get base/real prefix, or sys.prefix if there is none."""
#     return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

# def in_virtualenv():
#     return get_base_prefix_compat() != sys.prefix

# def check_venv():
#     if in_virtualenv() is False:
#         text = colored('YOU HAVE NOT ACTIVATED THE VIRTUAL ENVIRONMENT', 'red')
#         sys.exit(text)

# def get_project_requirements():
#     """Build the requirements list for this project"""
#     requirements_list = []

#     with open('requirements.txt',  encoding = "utf-8") as requirements:
#         for install in requirements:
#             requirements_list.append(install.strip())

#     return requirements_list


def parse_json(data):
    return json.loads(json_util.dumps(data))
