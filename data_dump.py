import pymongo
import pandas as pd
import json

# Defining the MongoDB connection(client)
client=pymongo.MongoClient("mongodb+srv://DebarghyaSikder:Nike2004$@cluster0.iwnfvfb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DATA_FILE_PATH=(r"C:\Users\KIIT\ML\Medical Insurance Tracker\Medical-Insurance-Tracker\insurance.csv")
DATABASE_NAME="INSURANCE"
COLLECTION_NAME="INSURANCE_PROJECT"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")
    
    df.reset_index(drop=True,inplace=True)
    
    json_record=list(json.loads(df.T.to_json()).values())  # transposing our data to store in MongoDB(key val pairs) converting to json and storing as list of records
    print(json_record[0])
    
    # inserting the data into MongoDB(the transposed one)
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    