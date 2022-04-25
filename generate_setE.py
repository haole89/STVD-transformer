from video_libs import video_speeding, reformatting
import pandas as pd
import os

"""
Step 0: generate a new file name due to the duplicate of positive video
Step 1: drop FPS with video speeding
step 2: re-formate video by reducing the video bitrate and resolution

Only apply video speeding to the positive of set E
For the negative, it makes no sense

"""

def generate_file():

    df = pd.read_csv(r"data\\groundtruth.csv")
    # Reference_Video,Positive_Video,Reference_Length,Positive_Length,Start_Copy
    selected_list = []
    data_list = []
    for row in df.itertuples():
        old_name = str(row.Positive_Video)
        copy_length = int(row.Reference_Length)
        start_copy = int(row.Start_Copy)
        count = selected_list.count(old_name)
        selected_list.append(old_name)
        new_name = old_name.split('.')[0] + "_E" + str(count+1) + ".mp4"
        case = ({
            "Old_Name": old_name,
            "New_Name": new_name,
            "Copy_Length": copy_length,
            "Start_Copy": start_copy
        })
        data_list.append(case)
    
    output_file = r"data\\setE.csv"
    df = pd.DataFrame(data=data_list)
    df.to_csv(output_file, header=True, index=False)
    
    return

def generate_positive():
    
    input_path = r"E:\stvd\set_A\positive"
    output_path = r"E:\stvd\tmp_E\positive"

    # input_path, input_file, output_path, output_file, start_copy, copy_length
    df = pd.read_csv(r"data\\setE.csv")

    for row in df.itertuples():
        input_file = str(row.Old_Name)
        output_file = str(row.New_Name)
        start_copy = int(row.Start_Copy)
        copy_length = int(row.Copy_Length)
        video_speeding(
            input_path= input_path,
            input_file= input_file,
            output_path= output_path,
            output_file= output_file,
            start_copy= start_copy,
            copy_length= copy_length
        )

        break

    return

def post_processing():
    
    input_path = r"F:\stvd\tmp_E\positive"
    output_path = r"F:\stvd\set_E\positive"

    for roots, dirs, files in os.walk(input_path):
        for name in files:            
            reformatting(input_path, name, output_path)
    return

def main():

    # generate_file()    
    generate_positive()
    # post_processing()
   

if __name__ == '__main__':
    main()
    
