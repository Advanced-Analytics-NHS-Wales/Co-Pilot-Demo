#install python packages script

import os
import subprocess
import sys

#install requests
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

#install pandas
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

#install matplotlib
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

#install pygame
subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])