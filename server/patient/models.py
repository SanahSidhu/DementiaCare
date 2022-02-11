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

    def insert_user(self, name: str, email: str, pwd: str, phnum: str) -> None:
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
                "Checklist": [],
                "Notes": [],
                "MedList": [],
                "Inventory": [],
                "EmergencyContacts": [],
                "Media": [],
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

    def insert_cl_nt_data(
        self,
        email: str,
        text: str,
        cl=False,
        nt=False,
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

    def get_cl_nt_data(self, email, cl=False, nt=False):
        """
        Func Desc
        """
        if cl == True:
            option = "Checklist"
        elif nt == True:
            option = "Notes"
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

        raise DataFetchingError(
            "There Are No Notes/CheckLists In The Database At This Moment"
        )

    def insert_ml_inv_emg_data(
        self,
        email: str,
        data: dict,
        ml=False,
        inv=False,
        emg=False,
        add=False,
        remove=False,
    ):
        """
        Func Desc
        """
        if ml == True:
            rec = {"MedList": data}
        elif inv == True:
            rec = {"Inventory": data}
        elif emg == True:
            rec = {"EmergencyContacts": data}
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
                    raise DataInsertionError("Error Inserting Data in Database")
            else:
                raise UserDoesNotExistError("User Does Not Exist")

        elif add == False and remove == True:
            if self.db.find_one({"Email": email}):
                try:
                    self.db.update({"Email": email}, {"$pull": {rec}})
                except Exception:
                    raise DataRemovalError("Error Removing Data From Database")
            else:
                raise UserDoesNotExistError("User Does Not Exist")

    def get_ml_inv_emg_data(self, email, ml=False, inv=False, emg=False):
        """
        Func Desc
        """
        if ml == True:
            option = "MedList"
        elif inv == True:
            option = "Inventory"
        elif emg == True:
            option = "EmergencyContacts"
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

        raise DataFetchingError(
            "There Are No MedLists/Inventories/EmergencyContacts In The Database At This Moment"
        )

    def insert_media(self, email: str, data: dict):
        """
        Func Desc
        """
        pass

    def get_media(self, email: str):
        """
        Func Desc
        """
        pass
