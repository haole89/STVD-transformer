from video_libs import low_downscale_compress
import os
import numpy as np

"""
generate all of the videos in the positive of set A 
"""

def generate_positive():

    input_path = r"E:\stvd\set_A\positive"
    output_path = r"E:\stvd\set_B\positive"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            low_downscale_compress(input_path, name, output_path, "B")  
    return
"""
pick up 3780 negative videos and generate
"""
def generate_negative():
    negative_list = []
    input_path = r"E:\stvd\set_A\negative"
    output_path = r"E:\stvd\set_B\negative"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            negative_list.append(name)
    
    np.random.shuffle(negative_list)
    selected_list = negative_list[:3780]
    # print(len(selected_list))
    for item in selected_list: 
        low_downscale_compress(input_path, item.strip(), output_path, "B")


def main():
    generate_positive()
    generate_negative()

if __name__ == '__main__':
    main()
    