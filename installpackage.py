import os
import sys
import subprocess

def main():
    print("install package in script")

def install_pip():
    print('start install package_pip')
    cmd = 'pip3 install -r requirements.txt'
    pip = subprocess.check_output(cmd, shell=True)
    print(pip)

def install_package():
    print('start install package')
    cmd = ['apt-get update']
    package = subprocess.check_output(cmd,shell=True)
    print(package)

if __name__=="__main__":
    main()
    install_package()
    install_pip()
