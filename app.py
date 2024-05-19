import csv
import json
from operator import itemgetter
from Src.ExamType import ExamType
from Src.ExamTimeSlot import ExamTimeSlot
from Src.Tool import TimeTool
from Src.Tool import ReadTool

if __name__ == "__main__":
    config_file = "./Configuration/configurations.json"
    configs = {}

    try:
        # Load configurations from JSON file
        with open(config_file, encoding="utf-8-sig") as json_file:
            configs = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in configuration file '{config_file}'.")
        exit(1)

    date_start_dict = {}
    time_tool = TimeTool()
    read_tool = ReadTool()

    # Sort the input data
    rows = []
    try:
        with open(configs["input_filename"], "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            rows = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: Input file '{configs['input_filename']}' not found.")
        exit(1)

    sorted_rows = sorted(rows, key=lambda row: (time_tool.date_str_to_date(row[0]), int(row[1]), row[4], row[5], time_tool.hm_str_to_hm(row[6])))

    # Process the sorted rows
    exams = []  # Store exam data for sorting
    for row in sorted_rows:
        try:
            # in case there is an empty line, skip it
            if row is None or len(row) == 0 or row[0] is None or row[0] == '':
                continue
            
            date, form, subject, student_name, student_class, student_number, original_start, original_end, room, situation, ratio, rest, green_pen = read_tool.read(time_tool, row, configs)
            initial_duration = time_tool.calculate_duration_minutes(original_start, original_end)

            composite_date_key = f"{date}_{form}_{student_class}_{student_number}_{student_name}"

            if composite_date_key not in date_start_dict:
                date_start_dict[composite_date_key] = configs["start"]

            start_time = time_tool.get_later_time(date_start_dict[composite_date_key], original_start)
            break_duration = configs["break"]

            exam = ExamTimeSlot(ratio=ratio, initial_duration=initial_duration, break_duration=break_duration,
                                start_time=start_time, subject=subject, form=form, rest=rest, situation=situation)
        
            if subject in configs["no_end_time_rounding_subjects"]:
                if subject == configs["eng_paper3"] and form > 2:
                    date_start_dict[composite_date_key] = time_tool.calculate_next_start_time(exam.end_time, rest)
                else:
                    date_start_dict[composite_date_key] = time_tool.calculate_next_start_time_without_round(exam.end_time, rest)
            elif subject in configs["no_rest_subjects"]:
                date_start_dict[composite_date_key] = exam.end_time
            else:
                date_start_dict[composite_date_key] = time_tool.calculate_next_start_time(exam.end_time, rest)

            sessions = time_tool.format_duration_times(exam.session_durations, exam.start_time, break_duration)
            exam_data = [
                date,
                form,
                exam.subject,
                student_name,
                student_class,
                student_number,
                room,
                original_start,
                original_end,
                exam.start_time,
                exam.end_time,
                exam.total_duration,
            ]
            sessions.insert(-1,time_tool.time_minus_minutes(exam.end_time, 15))
            sessions.insert(-1,time_tool.time_minus_minutes(exam.end_time, 5))
            if form >= 4 and form <= 6:
                sessions.insert(-1,exam.green_pen_time)
            else:
                sessions.insert(-1,"")
            if green_pen:
                sessions.insert(-1,exam.green_pen_time)
            else:
                sessions.insert(-1,"")

            exam_data.extend(sessions)
            exam_data.extend([exam.break_count, exam.session_count, exam.session_durations])

            exams.append(exam_data)
        except (ValueError, IndexError):
            print(f"Error: Invalid data format in input file at row {row}.")
            exit(1)


    try:
        with open(configs["output_filename"], "w", encoding="utf-8-sig", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Date", "Form", "Subject", "Student Name", "Student Class", "Student Class Number", "Room", "Orginial Start Time", "Orginial End Time",
                             "Start Time", "End Time", "Exam Duration", "1st start", "1st break", "2nd start",
                             "2nd break", "3rd start", "3rd break", "4th start", "4th break", "5th start", "5th break",
                             "6th start", "6th break", "7th break", "15 minutes Leave", "5 minutes Leave", "Early Leave Time", "Green Pen Time", "End", "Break Number", "Session Number", "Session"])

            for exam_data in exams:
                exam_data[0] = time_tool.date_to_date_str(exam_data[0])
                writer.writerow(exam_data)
                print(str(exam_data))
                print()
    except IOError:
        print(f"Error: Failed to write to output file '{configs['output_filename']}'.")
        exit(1)