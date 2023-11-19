from datetime import datetime, timedelta


class Tool:
    def __init__(self):
        pass

    def round_minute(self, time):
        minute = time.minute

        if 0 < minute <= 15:
            time = time.replace(minute=15)
        elif 15 < minute <= 30:
            time = time.replace(minute=30)
        elif 30 < minute <= 45:
            time = time.replace(minute=45)
        elif 45 < minute <= 59:
            time = time.replace(hour=time.hour + 1, minute=0)

        time = time.replace(second=0)
        return time

    def calculate_next_start(self,lunch_time, last_end, lunch_break, rest):
        new_start = datetime.strptime(last_end, "%H:%M:%S")
        lunch_time = datetime.strptime(lunch_time, "%H:%M:%S")
        new_start = self.round_minute(new_start)

        temp = new_start + timedelta(minutes=lunch_break)
        
        if temp.time() >= lunch_time.time():
            new_start += timedelta(minutes=lunch_break)
        else:
            new_start += timedelta(minutes=rest)
        
        return new_start.strftime("%H:%M:%S")

    def format_duration(self, durations, start):
        start_time = datetime.strptime(start, "%H:%M:%S")
        res = []

        for duration in durations:
            end_time = start_time + timedelta(minutes=duration)
            exam_str = f"{duration} mins exam {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}"
            res.append(exam_str)
            start_time = end_time
            end_time = start_time + timedelta(minutes=5)
            break_str = f"5 mins break {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}"
            res.append(break_str)
            start_time = end_time
        res.pop()
        return res

if __name__ == "__main__":
    tool = Tool()
    print(tool.calculate_next_start(lunch_time="12:00:00", last_end="11:47:31", lunch_break=60, rest=30))
    print(tool.format_duration([45,45,23], "09:00:00"))