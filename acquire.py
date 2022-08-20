import numpy as np
import pandas as pd
import env
import os

#connect to sql function used with in the get telcodata function to connect to sql/mysql server 
#needed to pull data from server. 

def connect(db):
   
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'








#pulling from sql the data for telco churn. 
#needs to have sections joined 




def get_telco_data():
    
  
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
            SELECT * FROM customers
            JOIN contract_types 
                USING (contract_type_id)
            JOIN payment_types 
                USING (payment_type_id)
            JOIN internet_service_types 
                USING (internet_service_type_id);  
        '''
        df = pd.read_sql(query, connect('telco_churn')) 
        df.to_csv(filename)
        return df