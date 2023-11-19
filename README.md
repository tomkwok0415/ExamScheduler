# Special Student Examination Scheduler

This program is designed to assist in scheduling examinations for special students. The scheduler takes into account the following requirements:

## 1. Exam Time for Special Students

The examination time for special students needs to be extended by a factor of 1.25. For example, if the regular exam duration is 90 minutes, the special student exam duration will be calculated as follows:

Regular Exam Duration: 90 minutes
Special Student Exam Duration: 90 * 1.25 = 112.5 minutes

## 2. Break Time for Special Students

Special students are allowed a maximum of 45 minutes of continuous exam time, after which they are required to take a 15-minute break. For example, if the special student exam duration is 90 minutes:

Special Student Exam Duration: 90 * 1.25 = 112.5 minutes
Breaks: 45 minutes + 15 minutes + 45 minutes + 15 minutes + 22.5 minutes

## 3. Equally Distributed Exam Sessions

To ensure fairness, each exam session needs to be equally distributed. For example, if the special student exam duration is 90 minutes:

Special Student Exam Duration: 90 * 1.25 = 112.5 minutes
Breaks: 45 minutes + 15 minutes + 45 minutes + 15 minutes + 22.5 minutes
Equally Distributed Sessions: 28.125 minutes + 15 minutes + 28.125 minutes + 15 minutes + 28.125 minutes + 15 minutes + 28.125 minutes

By following the above rules, the exam sessions for special students will be divided as follows:

- First Session: 28 minutes 7 seconds 5 (28'7'5) * 4
- Break: 15 minutes
- Second Session: 28 minutes 7 seconds 5 (28'7'5) * 4
- Break: 15 minutes
- Third Session: 28 minutes 7 seconds 5 (28'7'5) * 4
- Break: 15 minutes
- Fourth Session: 28 minutes 7 seconds 5 (28'7'5) * 4

## Configuration
The scheduler requires certain configuration parameters to function correctly. These parameters can be set in the Configuration/configurations.json file. Here are the available configuration options:

start: The start time for the examinations (e.g., "9:00:00").
lunch: The time for the lunch break (e.g., "12:00:00").
lunch_break: The duration of the lunch break in minutes (e.g., 60).
ratio: The ratio of the exam duration (e.g., 1.25).
break: The duration of regular breaks in exam in minutes (e.g., 15).
rest: The duration of rest periods between exam sessions in minutes (e.g., 30).
input_filename: The file path for the input data containing the exam details (e.g., "./Timeslot/Input/timeslot.csv").
output_filename: The file path for the output data containing the scheduled exam sessions (e.g., "./Timeslot/Output/timeslot.csv").


## Getting Started

Go to Configurartion/configurations.json can setup the configs:
To use the scheduler, follow these steps:

1. Go to project directory
1. run "pip install datetime" command
2. run "python app.py" command