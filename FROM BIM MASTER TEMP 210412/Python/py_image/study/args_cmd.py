#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os
os.chdir(os.getcwd())
import argparse

ap = argparse.ArgumentParser()# construct the argument parser and parse the arguments
ap.add_argument("--nonImage","--image", required=True, help="Path to the image")
args = vars(ap.parse_args()) # --image

print(args)