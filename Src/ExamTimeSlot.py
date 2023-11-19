from datetime import datetime, timedelta
import math

class ExamTimeSlot:
    def __init__(self, ratio, init_exam_duration, break_duration, start_time, name, form):
        self.form = form
        self.start_time = start_time
        self.name = name
        self.break_duration = break_duration
        self.session_duration, self.session_num, self.break_num, self.total_duration = self.calculate_exam_schedule(ratio=ratio, total_exam_time=init_exam_duration, break_duration=break_duration, form = self.form)
        self.end_time = self.calculate_end_time(start_time, self.total_duration)

    def __str__(self):
        return f"{self.name} starts at {self.start_time}, ends at {self.end_time}, total duration: {self.total_duration} mins with {self.session_num} session(s), each session {self.session_duration} mins, {self.break_num} break(s), each break {self.break_duration} mins"

    def calculate_exam_schedule(self, ratio, total_exam_time, break_duration, form):
        if form < 4 or total_exam_time*ratio<=90:
            return [total_exam_time], 1, 0, total_exam_time

        # Multiply the exam time by ratio
        adjusted_exam_time = math.ceil(total_exam_time * ratio)

        session_duration = []
        while(adjusted_exam_time>45):
            session_duration.append(45)
            adjusted_exam_time -= 45            
        
        if adjusted_exam_time < 16:
            if len(session_duration) <= 2:
                session_duration.pop()
                adjusted_exam_time = math.ceil((adjusted_exam_time + 45) / 2)
                session_duration.extend([adjusted_exam_time, adjusted_exam_time - 1])
            else:
                session_duration.pop()
                adjusted_exam_time = math.ceil((adjusted_exam_time + 45) / 2)
                session_duration.extend([adjusted_exam_time, adjusted_exam_time])
        else:
            session_duration.append(adjusted_exam_time)



        
        sessions= len(session_duration)
        breaks = len(session_duration)-1

        # Calculate the total exam time including breaks
        total_time_with_breaks = sum(session_duration) + break_duration * breaks

        # Return the calculated schedule
        return session_duration, sessions, breaks, total_time_with_breaks

    def calculate_end_time(self, start, total):
        start_datetime = datetime.strptime(start, "%H:%M:%S")
        end_datetime = start_datetime + timedelta(minutes=total)
        end_time = end_datetime.strftime("%H:%M:%S")
        return end_time


if __name__ == "__main__":
    time_slot = ExamTimeSlot(ratio=1.25, init_exam_duration=120, break_duration=5, start_time="09:00:00", name="Math Exam", form = 4)
    print(time_slot)
    time_slot = ExamTimeSlot(ratio=1.25, init_exam_duration=75, break_duration=5, start_time="09:00:00", name="Eng Exam", form =4)
    print(time_slot)
    time_slot = ExamTimeSlot(ratio=1.25, init_exam_duration=90, break_duration=5, start_time="09:00:00", name="Eng Exam", form = 4)
    print(time_slot)