import csv
import json
from Src.ExamTimeSlot import ExamTimeSlot
from Src.Tool import Tool

if __name__ == "__main__":
    config_file = "./Configuration/configurations.json"
    configs = {}

    # Load configurations from JSON file
    with open(config_file) as json_file:
        configs = json.load(json_file)

    date_start_dict = {}
    tool = Tool()

    with open(configs["input_filename"], "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        with open(configs["output_filename"], "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Name", "Start Time", "End Time", "Total Time", "Session Number", "Session Duration", "Break Number", "Break Duration"])
            
            for row in reader:
                name = row[0]
                init_duration = int(row[1])
                date = row[2]

                if date not in date_start_dict:
                    date_start_dict[date] = configs["start"]

                start_time = date_start_dict[date]
                break_duration = configs["break"]

                exam = ExamTimeSlot(break_duration=break_duration, init_exam_duration=init_duration, start_time=start_time, name=name)
                date_start_dict[date] = tool.calculate_next_start(lunch_time=configs["lunch"], last_end=exam.end_time, lunch_break=configs["lunch_break"], rest=configs["rest"])

                exam_data = [
                    exam.name,
                    exam.start_time,
                    exam.end_time,
                    exam.total_duration,
                    exam.session_num,
                    exam.session_duration,
                    exam.break_num,
                    exam.break_duration
                ]
                
                writer.writerow(exam_data)
                print(str(exam))
                print()