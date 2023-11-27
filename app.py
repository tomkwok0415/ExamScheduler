import csv
import json
from operator import itemgetter
from Src.ExamTimeSlot import ExamTimeSlot
from Src.Tool import TimeTool

if __name__ == "__main__":
    config_file = "./Configuration/configurations.json"
    configs = {}

    # Load configurations from JSON file
    with open(config_file,"r",encoding="utf-8-sig") as json_file:
        configs = json.load(json_file)

    date_start_dict = {}
    time_tool = TimeTool()

    with open(configs["input_filename"], "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        exams = []  # Store exam data for sorting

        for row in reader:
            # # in case there is empty line, skip it
            # if row is None:
            #     continue
            date = time_tool.date_str_to_date(row[0])
            form = int(row[1])
            subject = row[2]
            student_name = row[3]
            student_class = row[4]
            student_number = row[5]
            original_start = time_tool.format_time_hms(row[6])
            original_end = time_tool.format_time_hms(row[7])

            initial_duration = time_tool.calculate_duration_minutes(original_start, original_end)
            if len(row) >= 9 and row[8] is not None and row[8] != '':
                initial_duration = int(row[8])

            composite_date_key = f"{date}_{form}_{student_class}_{student_number}_{student_name}"

            if composite_date_key not in date_start_dict:
                date_start_dict[composite_date_key] = configs["start"]

            start_time = time_tool.get_later_time(date_start_dict[composite_date_key], original_start)
            if subject == configs["painting_subject"]:
                start_time = time_tool.time_minus_minutes(start_time, rest)
            break_duration = configs["break"]
            rest = configs["rest"]

            exam = ExamTimeSlot(painting_subject=configs["painting_subject"], ratio=configs["ratio"], initial_duration=initial_duration,
                                break_duration=break_duration, start_time=start_time, subject=subject,
                                form=form, rest=rest)
            date_start_dict[composite_date_key] = time_tool.calculate_next_start_time(exam.end_time, configs["rest"])

            sessions = time_tool.format_duration_times(exam.session_durations, exam.start_time, configs["break"])
            exam_data = [
                date,
                form,
                exam.subject,
                student_name,
                student_class,
                student_number,
                exam.start_time,
                exam.end_time,
                exam.total_duration,
            ]
            exam_data.extend(sessions)
            exam_data.extend([exam.break_count, exam.session_count, exam.session_durations])

            exams.append(exam_data)

    # Sort exams by date, class, and class number
    sorted_exams = sorted(exams, key=itemgetter(0, 4, 5))

    with open(configs["output_filename"], "w", encoding="utf-8-sig", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Date", "Form", "Subject", "Student Name", "Student Class", "Student Class Number",
                         "Starting Time", "End Time", "Exam Duration", "1st start", "1st break", "2nd start",
                         "2nd break", "3rd start", "3rd break", "4th start", "4th break", "5th start", "5th break", "6th start", "6th break", "7th break", "End",
                         "Break Number", "Session Number", "Session"])

        for exam_data in sorted_exams:
            exam_data[0] = time_tool.date_to_date_str(exam_data[0])
            writer.writerow(exam_data)
            print(str(exam_data))
            print()