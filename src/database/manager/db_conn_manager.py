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
import time
import uuid



class DatabaseConnectionManager:
    def __init__(self, user: str, password: str, host: str, port: int, database_name: str):
        # Corrected the connection string to use the database_name variable
        self.engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"
        )
        self.metadata = MetaData(bind=self.engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=self.engine)
        # Create a Session
        self.session = Session()

    def insert_telemetry(self, telemetry) -> int:
        try:
            self.session.add(telemetry)
            self.session.commit()
            return telemetry.id
        except Exception as e:
            self.session.rollback()
            print(f"Error inserting telemetry: {e}")
            return None

    def get_by_field(self, telemetry_model, field_name: str, value) -> list:
        try:
            field = getattr(telemetry_model, field_name)
            return self.session.query(telemetry_model).filter(field == value).all()
        except AttributeError:
            print(f"Model {telemetry_model.__name__} has no field {field_name}")
            return []
        except Exception as e:
            print(f"Error querying by field: {e}")
            return []

    def uuid_create(self) -> str:
        t = time.localtime()
        time_now = time.strftime("%H:%M:%S", t)
        return f"{time_now}:{uuid.uuid4()}"

    def close(self):
        self.session.close()
        self.engine.dispose()