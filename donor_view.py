
from mysql import connector
from datetime import datetime

class BloodDonorManager:

    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="C@rp3nt3r",
            database="blood_db_aug2026"
        )
        print("Connected to the database successfully!")
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from Donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record==None:
                print("No records found!")
            return record
        except Exception as e:
            print(e)
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
            INSERT INTO donor
            (name, blood_group, phone, city, last_donation)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Donor added successfully!")

        except Exception as e:
            print(e)
    def get(self):
            self.cursor=self.connection.cursor()
            query="""SELECT * FROM Donor"""
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            return records
        

    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record is None:
                print("No records found!")
            print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            if record!=None:
                query="delete from Donor where id=%s"
                self.cursor.execute(query,(id,))
                self.connection.commit()
                print("Donor deleted successfully!")
            else:
                print("No Donors found!")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder=placeholder.rstrip(", ")
                query=f"update donor set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                return True, "Donor updated successfully!"
            else:
                return False, "No donors found!"
        except Exception as e:
            print(e)
            


donor_instance = BloodDonorManager()
#donor_instance.post(name="Arjun",blood_group="B+",phone="8934898790",city="Trivandrum",last_donation=datetime.today())
donor_instance.get()
#donor_instance.retrieve(id=2)
#donor_instance.delete(id=3)
#donor_instance.put(id=1,name="Bharath",blood_group="AB+",phone="9999898790",city="Kollam",last_donation=datetime.today())
#self.connection.close()