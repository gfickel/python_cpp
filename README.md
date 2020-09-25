# python_cpp
Simple Python / Cpp integration

This repo shows how easy it is to integrate C/CPP code on Python. All of the explanations can be found on the following Medium: https://medium.com/p/f83136545023

## Replicate Results

First you need to install the Python dependencies that can be found on requirements.txt . Then you may just do the following (on Linux):
```
g++ -Wall -O2 -c -fPIC contrast_image.cpp
g++ contrast_image.o -shared -o libcontrast_image.so
python run.py
```
