from video_libs import high_downscale_compress
import os
import numpy as np

def generate_positive():

    input_path = r"E:\stvd\set_A\positive"
    output_path = r"E:\stvd\set_C\positive"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            high_downscale_compress(input_path, name, output_path, "C")

    return
"""

"""
def generate_negative():

    input_path = r"E:\stvd\set_A\negative"
    output_path = r"E:\stvd\set_C\negative"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            high_downscale_compress(input_path, name, output_path, "C")    

def main():
    generate_positive()
    generate_negative()

if __name__ == '__main__':
    main()
    