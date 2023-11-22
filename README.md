# Special Student Examination Scheduler

This program is designed to assist in scheduling examinations for special students. The scheduler takes into account the following requirements:

## 1. Exam Time for Special Students

The examination time for special students needs to be extended by a factor of 1.25. For example, if the regular exam duration is 90 minutes, the special student exam duration will be calculated as follows:

Regular Exam Duration: 90 minutes
Special Student Exam Duration: 90 * 1.25 = 112.5 minutes = 113 minutes (Rounding up)

## 2. Break Time for Special Students

Special students are allowed a maximum of 45 minutes of continuous exam time, after which they are required to take a 15-minute break. However, there are some exceptions based on the student's form level:

- For Low Form Students (Form 1-3): They will not have break time. Their exam time is simply multiplied by the ratio.

- For High Form Students (Form 4-6): If their regular exam duration is less than 90 minutes, they will also not have a break, and their exam time is multiplied by the ratio, similar to Low Form Students.

For High Form Students with a regular exam duration of 90 minutes or more, the break schedule is as follows:

Special Student Exam Duration: 90 * 1.25 = 112.5 minutes = 113 minutes (Rounding up)
Breaks: 45 minutes + 5 minutes + 45 minutes + 5 minutes + Remaining Time

Note that the Remaining Time is the duration after accommodating the maximum number of breaks.

## 3. Handling of Remaining Exam Session Duration

If there is a remainder of less than 16 minutes after scheduling the exam sessions, it needs to be handled in the following way:

- Calculate the adjusted exam time as the rounded-up average of the original last session duration and 45 minutes.

If there are less than 2 exam sessions of 45 minutes each:

- Append two new session durations to the schedule. The first duration is the adjusted exam time, and the second duration is the adjusted exam time minus 1 minute.

If there are 2 or more exam sessions of 45 minutes each:

- Append two new session durations to the schedule, both set to the adjusted exam time.

If the remainder is 16 minutes or greater, the duration of the last session remains unchanged.

Please note that the adjusted exam time is calculated based on the regular exam duration and the specified ratio.

## Configuration

The scheduler requires certain configuration parameters to function correctly. These parameters can be set in the `Configuration/configurations.json` file. Here are the available configuration options:

- `start`: The start time for the examinations (e.g., "8:30:00").
- `ratio`: The ratio of the exam duration (e.g., 1.25).
- `break`: The duration of regular breaks in the exam in minutes (e.g., 5).
- `rest`: The duration of rest periods between exam sessions in minutes (e.g., 30).
- `input_filename`: The file path for the input data containing the exam details (e.g., "./Timeslot/Input/timeslot.csv").
- `output_filename`: The file path for the output data containing the scheduled exam sessions (e.g., "./Timeslot/Output/timeslot.csv").

## Getting Started

To use the scheduler, follow these steps:

1. Set the desired configuration options in the `Configuration/configurations.json` file.
2. Ensure you have the required dependencies installed by running the command `pip install datetime`.
3. Run the command `python app.py` to execute the scheduler.