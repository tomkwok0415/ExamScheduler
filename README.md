# Special Student Examination Scheduler

This program is designed to assist in scheduling examinations for special students. The scheduler takes into account the following requirements:

## 1. Exam Time for Special Students

The examination time for special students needs to be extended by a factor of 1.25. For example, if the regular exam duration is 90 minutes, the special student exam duration will be calculated as follows:

Regular Exam Duration: 90 minutes
Special Student Exam Duration: 90 * 1.25 = 112.5 minutes = 113 minutes (Rounding up)

## 2. Break Time for Special Students

Special students are allowed a maximum of 45 minutes of continuous exam time, after which they are required to take a 5-minute break. However, there are some exceptions based on the student's form level:

- For Low Form Students (Form 1-3): They will not have break time. Their exam time is simply multiplied by the ratio.

- For High Form Students (Form 4-6): If their adjusted exam duration is less than 90 minutes, they will also not have a break.

For High Form Students with an adjusted exam duration of 90 minutes or more, the break schedule is as follows:

Special Student Exam Duration: 90 * 1.25 = 112.5 minutes = 113 minutes (Rounding up)
Breaks: 45 minutes + 5 minutes + 45 minutes + 5 minutes + Remaining Time

Note that the Remaining Time is the duration after accommodating the maximum number of breaks.

- For the VA Exam, it has two subjects: VA (評賞部分) and VA (畫畫部分).
It will be input as 2 subjects:
VA (評賞部分) * 1.25
VA (畫畫部分) * 1.05
Form 4: 30 mins + 2h 30 mins
Form 6: 45 mins + 3h 15 mins

For example, for Form 4:
VA (評賞部分) 8:30 - 9:00 => 8:30 - 9:08 (38 mins)
VA (畫畫部分) * 1.05 + some 5 mins breaks

For Form 6:
VA (評賞部分) 8:30 - 9:15 => 8:30 - 9:27 (57 mins)
VA (畫畫部分) * 1.05 + some 5 mins breaks

- For Putonghua and Visual Art Exam, there will be no rest between them but a break.

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
- `visual_art_painting_subject`: The subject name for the VA painting exam (e.g., "VA (畫畫部分)")
- `visual_art_comment_subject`: The subject name for the VA painting comment exam (e.g., "VA (評賞部分)")
- `putonghua_subject`: The subject name for the Putonghua exam (e.g., "普通話")

## Getting Started

To use the scheduler, follow these steps:

1. Configure the Scheduler:
   - Open the `Configuration/configurations.json` file.
   - Set the desired configuration options according to your requirements.

2. Install Dependencies:
   - Make sure you have the necessary dependencies installed.
   - Open your terminal or command prompt.
   - Run the following command to install the `datetime` package:
     ```
     pip install datetime
     ```

3. Execute the Scheduler:
   - In your terminal or command prompt, navigate to the project directory.
   - Run the following command to start the scheduler:
     ```
     python app.py
     ```

4. Handling Chinese Word Displaying Issues:
   - If you encounter problems with Chinese word display in the input file:
     - Open the file in Excel.
     - Select "Save As" and choose "CSV UTF-8" as the file format.

5. Resolving Date Displaying Problems:
   - If you encounter date displaying issues (e.g., `1/12/2023` appears as `#########`):
     - Open the file in Excel.
     - Select the date column.
     - Right-click and choose "Format Cells."
     - Select the "Date" category and choose the appropriate date format (e.g., `d/m/yyyy` for `14/3/2012`).

Note: Avoid running the program while opening the input/output file in Excel, as it may cause bugs due to file permission conflicts.