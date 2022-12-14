import pandas as pd
import json
import os

counter = 0

for f_files in os.listdir():
    if f_files.endswith(".txt"):
        #Open original file. read line by line and make appropriate adjustents
        file = open(f_files, 'r')
        starting = True
        num_lines = sum(1 for line in open('m.txt'))
        current_line = 1
        newf = ""
        for line in file:
            if starting:
                newf += "{\"values\":[" + line.strip() + ",\n"
                starting = False
            elif current_line == num_lines:
                newf += line.strip() + "]}"
            else:
                newf += line.strip() + ",\n"
            current_line += 1
        file.close()
        #convert string into json object
        json_object = json.loads(newf)

    

        json_object["values"][0]["values"]
        file_data = []
        for recording in json_object["values"]:
            if recording["category"] == "tracker":
                line_data = []
                data = recording["values"]
                line_data.append(data["frame"]["avg"]["x"])#Smoothed averaged x coordinates of BOTH eyes
                line_data.append(data["frame"]["avg"]["y"])#Smoothed averaged Y coordinates of BOTH eyes
                line_data.append(data["frame"]["raw"]["x"])
                line_data.append(data["frame"]["raw"]["y"])

                line_data.append(data["frame"]["lefteye"]["avg"]["x"])#Smoothed averaged x coordinates of the LEFT eye
                line_data.append(data["frame"]["lefteye"]["avg"]["y"])#Smoothed averaged y coordinates of the LEFT eye
                line_data.append(data["frame"]["lefteye"]["pcenter"]["x"])# x coordinates of the LEFT PUPIL
                line_data.append(data["frame"]["lefteye"]["pcenter"]["y"])# y coordinates of the LEFT PUPIL
                line_data.append(data["frame"]["lefteye"]["psize"])# size of the LEFT PUPIL
                line_data.append(data["frame"]["lefteye"]["raw"]["x"])#Smoothed averaged x coordinates of the LEFT eye
                line_data.append(data["frame"]["lefteye"]["raw"]["y"])#Smoothed averaged Y coordinates of the LEFT eye

                line_data.append(data["frame"]["righteye"]["avg"]["x"])#Smoothed averaged x coordinates of the RIGHT eye
                line_data.append(data["frame"]["righteye"]["avg"]["y"])#Smoothed averaged y coordinates of the RIGHT eye
                line_data.append(data["frame"]["righteye"]["pcenter"]["x"])# x coordinates of the RIGHT PUPIL
                line_data.append(data["frame"]["righteye"]["pcenter"]["y"])# y coordinates of the RIGHT PUPIL
                line_data.append(data["frame"]["righteye"]["psize"])# size of the RIGHT PUPIL
                line_data.append(data["frame"]["righteye"]["raw"]["x"])#Smoothed averaged x coordinates of the RIGHT eye
                line_data.append(data["frame"]["righteye"]["raw"]["y"])#Smoothed averaged Y coordinates of the RIGHT eye

                line_data.append(data["frame"]["time"])
                line_data.append(data["frame"]["timestamp"])

                file_data.append(line_data)



        dataframe = pd.DataFrame(file_data, columns= ["both_avg_x", "both_avg_y", "both_raw_x","both_raw_y", "left_avg_x", "left_avg_y", "left_pupil_avg_x", "left_pupil_avg_y", "left_pupil_size", "left_raw_x", "left_raw_y", "right_avg_x", "right_avg_y", "right_pupil_avg_x", "right_pupil_avg_y", "right_pupil_size", "right_raw_x", "right_raw_y", "time", "timestampt"])
        dataframe.to_csv(f_files + ".csv")
        counter += 1
        print("Files converted: ", counter)

