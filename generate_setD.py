from video_libs import global_tranformation, reformatting
import os
import numpy as np

"""
Step 1: global tranformation with filling, border adding, ...
step 2: re-formate video by reducing the video bitrate and resolution
"""

def generate_positive():
    
    input_path = r"F:\stvd\set_A\positive"
    output_path = r"F:\stvd\tmp_D\positive"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            global_tranformation(input_path, name, output_path)    

    return
"""

"""

def generate_negative():

    input_path = r"F:\stvd\set_A\negative"
    output_path = r"F:\stvd\tmp_D\negative"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            global_tranformation(input_path, name, output_path)
    
    return
""""
"""
def post_processing():
    
    input_path = r"F:\stvd\tmp_D\positive"
    output_path = r"F:\stvd\set_D\positive"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            reformatting(input_path, name, output_path)

    input_path = r"F:\stvd\tmp_D\negative"
    output_path = r"F:\stvd\set_D\negative"
    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            reformatting(input_path, name, output_path)
    return

def main():
    
    generate_positive()
    generate_negative()
    post_processing()
   

if __name__ == '__main__':
    main()
    
