from datetime import datetime, timedelta
import math

class ExamTimeSlot:
    def __init__(self, ratio, init_exam_duration, break_duration, start_time, name):
        self.start_time = start_time
        self.name = name
        self.break_duration = break_duration
        self.session_duration, self.session_num, self.break_num, self.total_duration = self.calculate_exam_schedule(ratio=ratio, total_exam_time=init_exam_duration, break_duration=break_duration)
        self.end_time = self.calculate_end_time(start_time, self.total_duration)

    def __str__(self):
        return f"{self.name} starts at {self.start_time}, ends at {self.end_time}, total duration: {self.total_duration} mins with {self.session_num} session(s), each session {self.session_duration} mins, {self.break_num} break(s), each break {self.break_duration} mins"

    def calculate_exam_schedule(self, ratio, total_exam_time, break_duration):
        # Step 1: Multiply the exam time by ratio
        adjusted_exam_time = total_exam_time * ratio

        sessions = int(adjusted_exam_time // 45)
        session_duration = math.ceil(adjusted_exam_time / sessions)
        breaks = sessions - 1

        while session_duration > 45:
            session_duration /= 2
            breaks += (breaks + 1)
            sessions *= 2
            session_duration = math.ceil(session_duration)

        # Calculate the total exam time including breaks
        total_time_with_breaks = session_duration * sessions + break_duration * breaks

        # Return the calculated schedule
        return session_duration, sessions, breaks, total_time_with_breaks

    def calculate_end_time(self, start, total):
        start_datetime = datetime.strptime(start, "%H:%M:%S")
        end_datetime = start_datetime + timedelta(minutes=total)
        end_time = end_datetime.strftime("%H:%M:%S")
        return end_time


if __name__ == "__main__":
    time_slot = ExamTimeSlot(init_exam_duration=120, break_duration=15, start_time="09:00:00", name="Math Exam")
    print(time_slot)