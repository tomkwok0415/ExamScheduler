import csv
import json
from operator import itemgetter
from Src.ExamTimeSlot import ExamTimeSlot
from Src.Tool import TimeTool

if __name__ == "__main__":
    config_file = "./Configuration/configurations.json"
    configs = {}

    # Load configurations from JSON file
    with open(config_file, encoding="utf-8-sig") as json_file:
        configs = json.load(json_file)

    date_start_dict = {}
    time_tool = TimeTool()

    # Sort the input data
    rows = []
    with open(configs["input_filename"], "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        rows = [row for row in reader]

    sorted_rows = sorted(rows, key=lambda row: (time_tool.date_str_to_date(row[0]), int(row[1]), row[4], row[5], time_tool.hm_str_to_hm(row[6])))

    # Process the sorted rows
    exams = []  # Store exam data for sorting
    for row in sorted_rows:
        # # in case there is empty line, skip it
        if row is None or len(row) == 0 or row[0] is None or row[0] == '':
            continue
        date = time_tool.date_str_to_date(row[0])
        form = int(row[1])
        subject = row[2]
        student_name = row[3]
        student_class = row[4]
        student_number = row[5]
        original_start = time_tool.hm_str_to_hms_str(row[6])
        original_end = time_tool.hm_str_to_hms_str(row[7])
        room = row[8]

        rest = configs["rest"]
        initial_duration = time_tool.calculate_duration_minutes(original_start, original_end)

        composite_date_key = f"{date}_{form}_{student_class}_{student_number}_{student_name}"

        if composite_date_key not in date_start_dict:
            date_start_dict[composite_date_key] = configs["start"]

        start_time = time_tool.get_later_time(date_start_dict[composite_date_key], original_start)
        break_duration = configs["break"]

        exam = ExamTimeSlot(visual_art_painting_subject=configs["visual_art_painting_subject"], ratio=configs["ratio"],
                            initial_duration=initial_duration, break_duration=break_duration,
                            start_time=start_time, subject=subject, form=form, rest=rest)
        if subject == configs["paintint_comment_subject"]:
            date_start_dict[composite_date_key] = exam.end_time
        elif subject == configs["putonghua_subject"]:
            date_start_dict[composite_date_key] = time_tool.calculate_next_start_time_without_round(exam.end_time,
                                                                                      break_duration)
        else:
            date_start_dict[composite_date_key] = time_tool.calculate_next_start_time(exam.end_time,
                                                                                      configs["rest"])

        sessions = time_tool.format_duration_times(exam.session_durations, exam.start_time, configs["break"])
        exam_data = [
            date,
            form,
            exam.subject,
            student_name,
            student_class,
            student_number,
            room,
            exam.start_time,
            exam.end_time,
            exam.total_duration,
        ]
        exam_data.extend(sessions)
        exam_data.extend([exam.break_count, exam.session_count, exam.session_durations])

        exams.append(exam_data)

    with open(configs["output_filename"], "w", encoding="utf-8-sig", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Date", "Form", "Subject", "Student Name", "Student Class", "Student Class Number", "Room",
                         "Starting Time", "End Time", "Exam Duration", "1st start", "1st break", "2nd start",
                         "2nd break", "3rd start", "3rd break", "4th start", "4th break", "5th start", "5th break",
                         "6th start", "6th break", "7th break", "End", "Break Number", "Session Number", "Session"])

        for exam_data in exams:
            exam_data[0] = time_tool.date_to_date_str(exam_data[0])
            writer.writerow(exam_data)
            print(str(exam_data))
            print()