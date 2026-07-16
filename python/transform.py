import pandas as pd
from logger import logger


def clean_data(df):
    logger.info("Cleaning Started")
    print("Cleaning data...")
    logger.info("Cleaning Completed")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Unknown")

    return df


def transform_orders(orders_df):
    print("Transforming Orders...")
    logger.info("Transforming Orders Table")

    # Add a calculated column
    orders_df["AveragePrice"] = (
        orders_df["TotalAmount"] / orders_df["Quantity"]
    )

    return orders_df