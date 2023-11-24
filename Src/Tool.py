from datetime import datetime, timedelta


class TimeTool:
    def calculate_duration_minutes(self, start_time_str, end_time_str):
        start_time = datetime.strptime(start_time_str, "%H:%M:%S")
        end_time = datetime.strptime(end_time_str, "%H:%M:%S")
        duration = end_time - start_time
        return duration.seconds // 60

    def get_later_time(self, time1_str, time2_str):
        time1 = datetime.strptime(time1_str, "%H:%M:%S")
        time2 = datetime.strptime(time2_str, "%H:%M:%S")

        if time1 >= time2:
            return time1_str
        else:
            return time2_str

    def format_time_hms(self, time_str):
        time = datetime.strptime(time_str, "%H:%M")
        return time.strftime("%H:%M:%S")
    
    def date_str_to_date(sef, date_str):
        date = datetime.strptime(date_str, "%d/%m/%Y")
        return date
    
    def date_to_date_str(sef, date):
        return date.strftime("%d/%m/%Y")

    def calculate_next_start_time(self, last_end_time_str, rest_duration):
        last_end_time = datetime.strptime(last_end_time_str, "%H:%M:%S")
        rounded_start_time = last_end_time
        new_start_time = rounded_start_time + timedelta(minutes=rest_duration)
        return new_start_time.strftime("%H:%M:%S")

    def format_duration_times(self, durations, start_time_str, break_duration):
        start_time = datetime.strptime(start_time_str, "%H:%M:%S")
        result = []

        for duration in durations:
            result.append(datetime.strftime(start_time, "%H:%M"))
            break_time = start_time + timedelta(minutes=duration)
            result.append(datetime.strftime(break_time, "%H:%M"))
            start_time = break_time + timedelta(minutes=break_duration)

        result.pop()
        end_time = start_time - timedelta(minutes=break_duration)

        while len(result) < 9:
            result.append(None)

        result.append(datetime.strftime(end_time, "%H:%M"))
        return result


if __name__ == "__main__":
    tool = TimeTool()
    print(tool.calculate_next_start_time(last_end_time_str="11:47:31", rest_duration=30))
    print(tool.format_duration_times([45, 45, 23], start_time_str="09:00:00", break_duration=5))