from datetime import datetime, timedelta
import math


class ExamTimeSlot:
    def __init__(self,painting_subject, ratio, initial_duration, break_duration, start_time, subject, form, rest):
        self.form = form
        self.start_time = start_time
        self.subject = subject
        self.break_duration = break_duration
        self.session_durations, self.session_count, self.break_count, self.total_duration = self.calculate_exam_schedule(
            ratio=ratio, total_exam_time=initial_duration, break_duration=break_duration, form=self.form, rest=rest, subject=subject, painting_subject= painting_subject)
        self.end_time = self.calculate_end_time(start_time, self.total_duration)

    def __str__(self):
        return f"{self.subject} starts at {self.start_time}, ends at {self.end_time}, total duration: {self.total_duration} mins with {self.session_count} session(s), each session {self.session_durations} mins, {self.break_count} break(s), each break {self.break_duration} mins"

    def calculate_exam_schedule(self, ratio, total_exam_time, break_duration, form, rest, subject, painting_subject):
        """
        Calculate the exam schedule based on the given parameters.
        """
        if subject == painting_subject:
            ratio = 1.05
        # Multiply the exam time by ratio
        adjusted_exam_time = math.ceil(total_exam_time * ratio)

        if form < 4 or adjusted_exam_time < 90:
            return [adjusted_exam_time], 1, 0, adjusted_exam_time

        session_durations = []
        while adjusted_exam_time > rest:
            session_durations.append(rest)
            adjusted_exam_time -= rest

        if adjusted_exam_time < 16:
            if len(session_durations) <= 2:
                session_durations.pop()
                if ((adjusted_exam_time + rest) % 2) !=0 :                    
                    adjusted_exam_time = math.ceil((adjusted_exam_time + rest) / 2)
                    session_durations.extend([adjusted_exam_time, adjusted_exam_time - 1])
                else:
                    adjusted_exam_time = int((adjusted_exam_time + rest) / 2)
                    session_durations.extend([adjusted_exam_time, adjusted_exam_time])
            else:
                session_durations.pop()
                adjusted_exam_time = math.ceil((adjusted_exam_time + rest) / 2)
                session_durations.extend([adjusted_exam_time, adjusted_exam_time])
        else:
            session_durations.append(adjusted_exam_time)

        session_count = len(session_durations)
        break_count = len(session_durations) - 1

        # Calculate the total exam time including breaks
        total_time_with_breaks = sum(session_durations) + math.ceil(break_duration * break_count)

        # Return the calculated schedule
        return session_durations, session_count, break_count, total_time_with_breaks

    def calculate_end_time(self, start, total):
        """
        Calculate the end time based on the start time and total duration.
        """
        start_datetime = datetime.strptime(start, "%H:%M:%S")
        end_datetime = start_datetime + timedelta(minutes=total)
        end_time = end_datetime.strftime("%H:%M:%S")
        return end_time


if __name__ == "__main__":
    time_slot = ExamTimeSlot(painting_subject = "VA (畫畫部分)", ratio=1.25, initial_duration=120, break_duration=5, start_time="09:00:00",
                             subject="Math Exam", form=4, rest=45)
    print(time_slot)
    time_slot = ExamTimeSlot(painting_subject = "VA (畫畫部分)", ratio=1.25, initial_duration=75, break_duration=5, start_time="09:00:00",
                             subject="Eng Exam", form=4, rest=45)
    print(time_slot)
    time_slot = ExamTimeSlot(painting_subject = "VA (畫畫部分)", ratio=1.25, initial_duration=90, break_duration=5, start_time="09:00:00",
                             subject="Eng Exam", form=4, rest=45)
    print(time_slot)
    time_slot = ExamTimeSlot(painting_subject = "VA (畫畫部分)", ratio=1.25, initial_duration=90, break_duration=5, start_time="09:00:00",
                             subject="VA (畫畫部分)", form=4, rest=45)
    print(time_slot)