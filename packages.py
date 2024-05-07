import subprocess
import time
pip_commands=[
    "pip list",
    "python -m pip install --upgrade pip",
    "pip install seaborn",
    "pip install imagehash",
    "pip install opencv-python",
    "pip install flask",
    "pip install flask-mail",
    "pip install scikit-image",
    "pip install scikit-learn",
    "pip install plotly",
    "pip install mysql-connector",
    "pip install imutils",
    "pip install pytesseract",
    "pip install stepic",
    "pip install opencv-contrib-python",
    "pip install face-recognition",
    "pip install face-recognizer",
    "pip list",

    ]
print(
"""
MUTHU

     -DEVELOPER
"""


    )
time.sleep(7)
for commands in pip_commands:
    if commands==pip_commands[0]:
        print("==============| YOUR PREVIOUS PIP LIST |=============")
    elif commands==pip_commands[7]:
        print("==========| YOUR INSTALLED PIP LIST  |===========")
    subprocess.run(commands,shell=True)
print("developer:\>Muthu")
#developed by abu>>developer

"""
THIS IS FOR PACKAGES INSTALLER
WRITE SINGLE LINE COMMAND TO DO EXECUTE MORE PIP COMMANDS


C:\>python packages.py

"""
