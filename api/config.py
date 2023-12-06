from os import environ


class Config:
    def __init__(self):
        self.DB_USERNAME = (
            environ["TRAN_DATA_SYNC_DB_USERNAME"]
            if environ.get("TRAN_DATA_SYNC_DB_USERNAME")
            else "postgres"
        )
        self.DB_PASSWORD = (
            environ["TRAN_DATA_SYNC_DB_PASSWORD"]
            if environ.get("TRAN_DATA_SYNC_DB_PASSWORD")
            else "postgres"
        )
        self.DB_HOST = (
            environ["TRAN_DATA_SYNC_DB_HOST"]
            if environ.get("TRAN_DATA_SYNC_DB_HOST")
            else "localhost"
        )
        self.DB_PORT = (
            environ["TRAN_DATA_SYNC_DB_PORT"]
            if environ.get("TRAN_DATA_SYNC_DB_PORT")
            else "5432"
        )
