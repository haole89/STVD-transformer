from video_libs import video_speeding, reformatting
import pandas as pd
import os

"""
Step 1: drop FPS with video speeding
step 2: re-formate video by reducing the video bitrate and resolution

Only apply video speeding to the positive of set E
For the negative, it makes no sense

"""

def generate_positive():
    
    input_path = r"F:\stvd\set_A\positive"
    output_path = r"F:\stvd\tmp_E\positive"

    

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            video_speeding(input_path, name, output_path)    

    return

def post_processing():
    
    input_path = r"F:\stvd\tmp_E\positive"
    output_path = r"F:\stvd\set_E\positive"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            reformatting(input_path, name, output_path)
    return

def main():
    
    generate_positive()   
    post_processing()
   

if __name__ == '__main__':
    main()
    
