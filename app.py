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
            writer.writerow(["Name", "Start Time", "End Time", "Total Time", "Session", "Break Number", "Break Duration", "Session Number", "Session Duration"])
            
            for row in reader:
                form = int(row [0])
                name = row[1]
                init_duration = int(row[2])
                date = row[3]
                
                 # Generate a combined key for date and form
                date_form_key = f"{date}_{form}"

                if date_form_key not in date_start_dict:
                    date_start_dict[date_form_key] = configs["start"]

                start_time = date_start_dict[date_form_key]
                break_duration = configs["break"]

                exam = ExamTimeSlot(ratio=configs["ratio"], break_duration=break_duration, init_exam_duration=init_duration, start_time=start_time, name=name, form=form)
                date_start_dict[date_form_key] = tool.calculate_next_start(lunch_time=configs["lunch"], last_end=exam.end_time, lunch_break=configs["lunch_break"], rest=configs["rest"])
                
                sessions = tool.format_duration(exam.session_duration, exam.start_time)
                exam_data = [
                    exam.name,
                    exam.start_time,
                    exam.end_time,
                    exam.total_duration,
                    sessions,
                    exam.break_num,                
                    exam.break_duration,
                    exam.session_num,
                    exam.session_duration,
                ]
                
                writer.writerow(exam_data)
                print(str(exam))
                print()