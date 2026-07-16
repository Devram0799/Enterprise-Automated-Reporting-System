from extract import extract_table
from transform import clean_data, transform_orders
from load import load_csv
from logger import logger
from report_generator import generate_excel_report


TABLES = [
    "Customers",
    "Products",
    "Employees",
    "Orders",
    "Transactions"
]


def run_pipeline():

    print("=" * 50)
    print("ENTERPRISE ETL PIPELINE STARTED")
    print("=" * 50)
    logger.info("ETL Pipeline Started")

    for table in TABLES:

        df = extract_table(table)

        df = clean_data(df)

        if table == "Orders":
            df = transform_orders(df)

        load_csv(df, f"{table}.csv")

    print("=" * 50)
    print("ETL COMPLETED SUCCESSFULLY")
    print("=" * 50)
logger.info("ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    run_pipeline()
    
generate_excel_report()

print("="*50)
print("ETL COMPLETED SUCCESSFULLY")
print("="*50)