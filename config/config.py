from urllib.parse import quote_plus

SERVER = r"DESKTOP-U6KVQ70\SQLEXPRESS"
DATABASE = "EnterpriseReportingDB"

CONNECTION_STRING = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)