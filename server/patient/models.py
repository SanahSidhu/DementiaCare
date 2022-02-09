from django.http import response
from dotenv import load_dotenv
import hashlib, binascii
import pymongo
import os

from core.settings import DATABASE
from .errors import (
    InvalidUserCredentialsError,
    InvalidInsertionError,
    UserDoesNotExistError,
    DataInsertionError,
    DataFetchingError,
    InvalidFieldError,
    DataRemovalError,
    UserExistsError,
)

load_dotenv()


class UserData:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("PATIENT_DATA_COLLECTION")]

    def insert_user(
        self, name: str, email: str, pwd: str, phnum: str, emergencynum: str
    ) -> None:
        """Insert user into collection

        Args:
            name: User Name
            email: User Email ID
            pwd: User Account Password
            phnum: User Phone Number
            emergencynum: Emergency Contact Number

        Returns:
            None: inserts user data into db
        """
        if self.db.find_one({"Email": email}):
            raise UserExistsError("User Already Exists")
        else:
            pwd = self.hash_password(pwd)
            rec = {
                "Name": name,
                "Email": email,
                "Password": pwd,
                "PhoneNumber": phnum,
                "EmergencyContact": phnum,
                "Checklist": [],
                "Notes": [],
                "MedList": [],
                "Inventory": [],
            }
            self.db.insert_one(rec)

    def hash_password(self, pwd: str) -> str:
        """Hashes password using salted password hashing (SHA512 & PBKDF_HMAC2)

        Args:
            pwd: Password to be hashed

        Returns:
            str: Hashed password
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        pwd_hash = hashlib.pbkdf2_hmac("sha512", pwd.encode("utf-8"), salt, 100000)
        pwd_hash = binascii.hexlify(pwd_hash)
        final_hashed_pwd = (salt + pwd_hash).decode("ascii")
        return final_hashed_pwd

    def check_hash(self, email: str, pwd: str) -> bool:
        """Verifies hashed password with stored hash & verifies user before login

        Args:
            email: Email ID of User
            pwd: Password to be checked

        Returns:
            bool
        """
        if value := self.db.find_one({"Email": email}):
            dbpwd = value["Password"]
            salt = dbpwd[:64]
            dbpwd = dbpwd[64:]

            pwd_hash = hashlib.pbkdf2_hmac(
                "sha512", pwd.encode("utf-8"), salt.encode("ascii"), 100000
            )
            pwd_hash = binascii.hexlify(pwd_hash).decode("ascii")

            if pwd_hash == dbpwd:
                return True
            else:
                raise InvalidUserCredentialsError("Invalid Login Credentials")

        else:
            raise UserDoesNotExistError("User Does Not Exist")

    def insert_data(
        self,
        email: str,
        text: str,
        cl=False,
        nt=False,
        ml=False,
        inv=False,
        add=False,
        remove=False,
    ):
        """
        Func Desc
        """
        data = {"Text": text}

        if cl == True:
            rec = {"Checklist": data}
        elif nt == True:
            rec = {"Notes": data}
        elif ml == True:
            rec = {"MedList": data}
        elif inv == True:
            rec = {"Inventory": data}
        else:
            raise InvalidInsertionError("Invalid Insert Function Requested")

        if add == True and remove == False:
            if self.db.find_one({"Email": email}):
                try:
                    self.db.update_one(
                        {"Email": email},
                        {"$push": {rec}},
                    )
                except Exception:
                    raise DataInsertionError("Error Inserting Text in Database")
            else:
                raise UserDoesNotExistError("User Does Not Exist")

        elif add == False and remove == True:
            if self.db.find_one({"Email": email}):
                try:
                    self.db.update({"Email": email}, {"$pull": {rec}})
                except Exception:
                    raise DataRemovalError("Error Removing Text From Database")
            else:
                raise UserDoesNotExistError("User Does Not Exist")

    def get_db_data(self, email, cl=False, nt=False, ml=False, inv=False):
        """
        Func Desc
        """
        if cl == True:
            option = "Checklist"
        elif nt == True:
            option = "Notes"
        elif ml == True:
            option = "MedList"
        elif inv == True:
            option = "Inventory"
        else:
            raise InvalidFieldError("Invalid Field Requested")

        if data := self.db.find(
            {"Email", email},
            {
                "_id": 0,
            },
        ):
            docs = data[option]
            json_data = response.JsonResponse(docs, safe=False)
            return json_data

        raise DataFetchingError("There Are No Posts In The Database At This Moment")
