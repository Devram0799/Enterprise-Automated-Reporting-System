import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sqlalchemy import create_engine
from config.config import CONNECTION_STRING
from logger import logger

engine = create_engine(CONNECTION_STRING)


def extract_table(table_name):
    query = f"SELECT * FROM {table_name}"

    df = pd.read_sql(query, engine)

    folder = "data/raw"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, f"{table_name}.csv")
    df.to_csv(file_path, index=False)

    logger.info(f"{table_name} extracted successfully")
    print(f"✅ {table_name} exported successfully")

    return df


if __name__ == "__main__":
    tables = [
        "Customers",
        "Products",
        "Employees",
        "Orders",
        "Transactions"
    ]

    for table in tables:
        extract_table(table)