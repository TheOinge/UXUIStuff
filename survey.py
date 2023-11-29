import csv
import os

def survey():
    survey_data = []

    while True:
        person_name = input("Enter the person's name (or 'done' to finish): ")
        if person_name.lower() == 'done':
            break

        person_data = {"Name": person_name}

        # Collect survey information for the current person
        person_data["FailedPages"] = input("Were there any pages that failed to show or function? (y/n)").lower() == 'y'
        person_data["Easiness"] = how_easy()
        person_data["Time"] = how_long()
        person_data["Clicks"] = how_many_clicks()
        person_data["Errors"] = how_many_errors()

        survey_data.append(person_data)

    # Write data to CSV file
    append_to_csv(survey_data)

def append_to_csv(survey_data):
    file_exists = os.path.isfile('data.csv')

    with open('data.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # If the file doesn't exist, write the header
        if not file_exists:
            header = ["Name", "FailedPages", "Easiness", "Time", "Clicks", "Errors"]
            csv_writer.writerow(header)

        # Write the data
        for person_data in survey_data:
            csv_writer.writerow([
                person_data["Name"],
                person_data["FailedPages"],
                person_data["Easiness"],
                person_data["Time"],
                person_data["Clicks"],
                person_data["Errors"]
            ])

def how_easy():
    return input("How easy was the task? 1 - 10: ")

def how_long():
    return input("How long did it take for the person to get familiar with the app? (seconds): ")

def how_many_clicks():
    return input("How many total clicks did the user do? : ")

def how_many_errors():
    return input("How many errors did the user encounter? : ")

def main():
    survey()

if __name__ == "__main__":
    main()
