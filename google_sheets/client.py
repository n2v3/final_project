import os
import traceback

import gspread

CREDENTIALS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "credentials.json"
)

gc = gspread.service_account(filename=CREDENTIALS_PATH)


def write_to_sheet(data):
    try:
        sh = gc.open("Job Hub")
        worksheet = sh.sheet1

        columns = [
            "ID",
            "Job Title",
            "Category",
            "Company",
            "Description",
            "Requirements",
            "Location",
            "Salary",
            "Posted at",
        ]

        # Retrieve the first row (headers) from the worksheet
        existing_columns = worksheet.row_values(1)

        # Check if the existing columns match the expected columns
        if not existing_columns == columns:
            # If they don't match, append the columns
            worksheet.append_row(columns)

        # Append data to the worksheet
        worksheet.append_rows(data)

        print("Data successfully written to Google Sheet!")
        print(f"Written data: {data}")
    except Exception as e:
        print(f"Error writing to Google Sheet: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    write_to_sheet([["Vacancy1", "Vacancy2"], ["Vacancy3", "Vacancy4"]])
