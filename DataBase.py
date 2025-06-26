
# import pypyodbc
# import pyodbc
import pymssql
import json

# Define your connection parameters
server = '41.38.197.252'  # e.g., 'localhost' or '41.38.197.252' 'DESKTOP-LMBLE4G\MERZOSQLEXPRESS'
database = 'TestDB'
username = 'merzo'    # Use None if using Windows Authentication
password = 'merzo1976'     # Use None if using Windows Authentication

# Create the connection string
# connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection_string = f'SERVER={server}; user={username}; password={password};database={database}'

# Connect to the database

try:  
    # db = pyodbc.connect(connection_string)
    
    db = pymssql.connect(server='41.38.197.252', user='merzo', password='merzo1976', database='TestDB')
    print("Connection successful!")
    
    cr = db.cursor()

    def commit_and_close():
    
     db.commit() 
      

# **********************************************************************************************************
# ********************************  Show All Data ASC ******************************************************
# **********************************************************************************************************

    def show_skills():
      
      # cr.execute(f"select ID_emp,First_Name,Last_Name,Gender,Country,Age,Last_Update from Emp_01_Table ORDER BY First_Name ASC")
      cr.execute(f"select * from Emp_01_Table ORDER BY First_Name ASC")
      return  cr.fetchall()
    

# **********************************************************************************************************
# ********************************  Show All Data DESC *****************************************************
# **********************************************************************************************************

    def show_skills_Decs():
      
      # cr.execute(f"select ID_emp,First_Name,Last_Name,Gender,Country,Age,Last_Update from Emp_01_Table ORDER BY First_Name DESC")
      cr.execute(f"select * from Emp_01_Table ORDER BY First_Name DESC")
      return  cr.fetchall()
    
# **********************************************************************************************************
# ********************************  Search in Data *********************************************************
# **********************************************************************************************************


    def Show_Filter_Emp(Search_V_01):
#     cr.execute(f"select ID_emp,First_Name,Last_Name,Gender,Country,Age,Last_Update from Emp_01_Table where First_Name LIKE  '%' + '{Search_V_01}' + '%' or Last_Name LIKE  '%' + '{Search_V_01}' + '%' ORDER BY First_Name ")
      cr.execute(f"select * from Emp_01_Table where First_Name LIKE  '%' + '{Search_V_01}' + '%' or Last_Name LIKE  '%' + '{Search_V_01}' + '%' ORDER BY First_Name ")
      return  cr.fetchall()
    
# **********************************************************************************************************
# ********************************  Filter By Country in Data **********************************************
# **********************************************************************************************************


    def Show_Filter_Emp_ByCountry(Filter_ByCountry_V_01):
    # cr.execute(f"select ID_emp,First_Name,Last_Name,Gender,Country,Age,Last_Update from Emp_01_Table where Country='{Filter_ByCountry_V_01}' ORDER BY First_Name ")
      cr.execute(f"select * from Emp_01_Table where Country='{Filter_ByCountry_V_01}' ORDER BY First_Name ")
      return  cr.fetchall()
    
# **********************************************************************************************************
# ********************************  View Emp  Data *********************************************************
# **********************************************************************************************************

    def show_Emp_Data(emp_id_v):
    
      cr.execute(f"select * from Emp_01_Table  where ID_emp = '{emp_id_v}' ORDER BY First_Name ")
      return  cr.fetchall()
    

# **********************************************************************************************************
# ********************************  Countries for combobox  Data *******************************************************
# **********************************************************************************************************

    def show_Countries():
      
      cr.execute("select * from Countries_Table ORDER BY CountryName")
      return  cr.fetchall()
    

# **********************************************************************************************************
# ********************************  Countries For Filter  Data *******************************************************
# **********************************************************************************************************

    def show_Countries_Filter():
      
      cr.execute("select * from FilterByCountry ORDER BY Country")
      return  cr.fetchall()
    


# **********************************************************************************************************
# ********************************  Updata Emp  Data *******************************************************
# **********************************************************************************************************

 
    def update_Emp_Data(Updated_First_Name,Updated_Last_Name,Updated_Telephone,Updated_Last_Email,Updated_Gender,Updated_Age,Updated_Country,Updated_Last_Update,Emp_ID,Emp_Pic):

     cr.execute(f"UPDATE  Emp_01_Table SET First_Name ='{Updated_First_Name}',Last_Name ='{Updated_Last_Name}', Telephone ='{Updated_Telephone}',Email ='{Updated_Last_Email}', Gender ='{Updated_Gender}',Age ='{Updated_Age}',Country ='{Updated_Country}',Last_Update ='{Updated_Last_Update}' , Pic ='{Emp_Pic}'  where ID_emp = '{Emp_ID}'")
     db.commit()
      

# **********************************************************************************************************
# ********************************  ADD Emp  Data **********************************************************
# **********************************************************************************************************

    def ADD_Emp_Data(New_First_Name,New_Last_Name,New_Telephone,New_Last_Email,New_Gender,New_Age,New_Country,New_Createdate,New_Last_Update,New_Img):


     cr.execute(f"insert into Emp_01_Table (First_Name, Last_Name,Telephone,Email,Gender,Age,Country,Created_on,Last_Update,Pic) values('{New_First_Name}', '{New_Last_Name}' , '{New_Telephone}' , '{New_Last_Email}' , '{New_Gender}' , '{New_Age}' , '{New_Country}' , '{New_Createdate}' , '{New_Last_Update}' , '{New_Img}')")
     db.commit()
      
       
# **********************************************************************************************************
# ********************************  Delete Emp  Data *******************************************************
# **********************************************************************************************************

    def Delete_skill(emp_id_v):
      
      cr.execute(f"delete from Emp_01_Table where ID_emp = '{emp_id_v}'")
      db.commit()


# **********************************************************************************************************


# **********************************************************************************************************
# ********************************  get Data  CountryPercentage_data ***************************************
# **********************************************************************************************************

    def Get_CountryPercentage_data():
        
     
       cr.execute(f"select  * from Emp_CountByCountry order by NoEmpCountry DESC")
      
       rows = cr.fetchall()
       return  json.dumps(rows)


# **********************************************************************************************************


# **********************************************************************************************************
# ********************************  get Data  GenderPercentage_data ***************************************
# **********************************************************************************************************

    def Get_GenderPercentage_data():
        
     
       cr.execute(f"select  * from Emp_CountByGender")
      
       rows = cr.fetchall()
       return  json.dumps(rows)


# **********************************************************************************************************


# **********************************************************************************************************
# ********************************  get Data  AgePercentage_data ***************************************
# **********************************************************************************************************

    def Get_AgePercentage_data():
        
     
       cr.execute(f"select  * from Emp_Age_Rang_Count")
      
       rows = cr.fetchall()
       return  json.dumps(rows)


# **********************************************************************************************************


except Exception as e:
    print("Error connecting to the database:", e)

# Don't forget to close the connection when done
finally:
    if 'connection' in locals():
        commit_and_close()
