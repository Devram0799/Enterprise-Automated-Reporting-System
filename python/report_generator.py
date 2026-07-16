import os
import pandas as pd

RAW_FOLDER = "data/processed"
REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_excel_report():

    report_path = os.path.join(REPORT_FOLDER, "Enterprise_Report.xlsx")

    with pd.ExcelWriter(report_path, engine="openpyxl") as writer:

        files = [
            "Customers.csv",
            "Products.csv",
            "Employees.csv",
            "Orders.csv",
            "Transactions.csv"
        ]

        for file in files:

            csv_path = os.path.join(RAW_FOLDER, file)

            df = pd.read_csv(csv_path)

            sheet_name = file.replace(".csv", "")

            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Excel Report Generated Successfully!")