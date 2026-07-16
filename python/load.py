import os
from logger import logger


def load_csv(df, filename):
    output_folder = "data/processed"

    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, filename)

    df.to_csv(file_path, index=False)

    logger.info(f"{filename} saved successfully")
    print(f"Saved: {file_path}")