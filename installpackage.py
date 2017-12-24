import os
import sys
import subprocess

def main1():
    print("install package in script")

def install_package():
    sudopassword='9121170207'
    sudo1=subprocess.Popen(['sudo -s'],shell=True, stdout=subprocess.PIPE)
    sudo1.communicate()

    pass1=subprocess.Popen(sudopassword,shell=True,stdout=subprocess.PIPE)
    pass1.communicate()

    process=subprocess.Popen(['sudo apt-get update'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    disk=process.communicate()
    print(disk)

def accses_root():
    echo = subprocess.Popen(['echo', '9121170207'],
                            stdout=subprocess.PIPE,
                            )

    sudo = subprocess.Popen(['sudo -s apt-get update'],
                            stdin=echo.stdout,
                            stdout=subprocess.PIPE,shell=True
                            )


if __name__=="__main__":
    main1()
    #install_package()
    accses_root()