from sqlalchemy import create_engine, exc, inspect
from sqlalchemy.orm import sessionmaker
import configparser
import mysql.connector
from models.customers import Base
from models.user import User
from models.customers import Customer
from models.contract import Contract

import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

config = configparser.ConfigParser()
config.read("config.ini")

DATABASE_USERNAME = config.get("database", "username")
DATABASE_PASSWORD = config.get("database", "password")
DATABASE_HOST = config.get("database", "host")
DATABASE_NAME = config.get("database", "database_name")

DATABASE_URL = f"mysql+mysqlconnector://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"


def create_database_if_not_exists():
    try:
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD,
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
        print(f"Base de données '{DATABASE_NAME}' créée avec succès.")
    except mysql.connector.Error as e:
        print(f"Erreur lors de la création de la base de données : {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def init_db():
    create_database_if_not_exists()

    try:
        engine = create_engine(DATABASE_URL)
        print("Connexion à la base de données établie avec succès.")

        # Vérifier si les tables existent déjà
        inspector = inspect(engine)

        # Liste des tables
        tables = {
            User.__tablename__: User.__table__,
            Customer.__tablename__: Customer.__table__,
            Contract.__tablename__: Contract.__table__,
        }

        # Utiliser une session pour créer les tables dans une transaction
        SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )
        session = SessionLocal()

        for table_name, table in tables.items():
            if not inspector.has_table(table_name):
                table.create(bind=engine)
                print(f"Table {table_name} créée avec succès.")
            else:
                print(
                    f"Table {table_name} existe déjà, elle ne sera pas recréée."
                )

        session.commit()
        print("Tables créées avec succès.")
        session.close()

        return SessionLocal
    except Exception as e:
        print(
            f"Une erreur s'est produite lors de l'initialisation de la base de données : {e}"
        )
