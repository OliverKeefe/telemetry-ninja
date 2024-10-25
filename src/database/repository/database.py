from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    Float,
    String,
    Boolean,
    select,
    insert,
    update,
    delete,
)
from sqlalchemy.orm import sessionmaker  # Import sessionmaker
from model.iracing_telemetry_model import IracingTelemetry


class Database:
    def __init__(self, user: str, password: str, host: str, port: int, database_name: str):
        self.engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/database_name")
        self.metadata = MetaData(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def insert_telemetry(self, telemetry: IracingTelemetry) -> int:
        """
        Inserts a telemetry record into the database.
        :param telemetry: An instance of IracingTelemetry.
        :return: The inserted record's ID.
        """
        self.session.add(telemetry)
        self.session.commit()
        return telemetry.id

    def get_by_field(self, telemetry_model, field_name: str, value) -> list:
        field = getattr(telemetry_model, field_name)
        return self.session.query(telemetry_model).filter(field == value).all()

    def close(self):
        """
        Closes the database session and engine
        """
        self.session.close()
        self.engine.dispose()
