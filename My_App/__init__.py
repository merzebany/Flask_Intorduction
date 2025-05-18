from flask import Flask , render_template, url_for,request,jsonify,redirect
from flask_cors import CORS
import os
import json
import requests
from supabase import create_client, Client

import uuid # For generating unique names
from pathlib import Path

app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/My_App')

# Supabase config

SUPABASE_URL = "https://elolabnvelujlzrdtgdu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVsb2xhYm52ZWx1amx6cmR0Z2R1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NjgwNTYyNywiZXhwIjoyMDYyMzgxNjI3fQ.3m0UbcvKdKyQ19Sde6vD0VO_kWmcEFOTQQFeZjMJDws"
BUCKET = "images"
HEADERS = {
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/octet-stream",
    "apikey": SUPABASE_KEY
}
image_url = ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# CORS(app, methods=["GET", "POST", "PUT", "DELETE"])


app.config['UPLOAD_FOLDER'] = os.path.join('My_App/static', 'images')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)




# ***********************************************************************************************************************
# ******************************* Main Page Route ***********************************************************************
# ***********************************************************************************************************************

@app.route("/")
def Index():
    class_For_01="active" 
    class_For_02="text-white"
    Title_V = "Home"
    
    
    from DataBase import show_skills
    my_Skill = show_skills()
  
    from DataBase import  show_Countries_Filter
    Countries_Filter =  show_Countries_Filter()

 

    return render_template( template_name_or_list= "index.html" , 
                           class_For_01=class_For_01, 
                           class_For_02=class_For_02,
                           Title_V = Title_V,
                           skills = my_Skill,
                           Countries = Countries_Filter )


# ***********************************************************************************************************************
# ******************************* Show Data Sort By Firstname Decs ******************************************************
# ***********************************************************************************************************************

@app.route("/ShowDataDecs")
def ShowDataDecs():
    class_For_01="active" 
    class_For_02="text-white"
    Title_V = "Home"
    
    
    from DataBase import show_skills_Decs
    my_Skill = show_skills_Decs()

    from DataBase import  show_Countries_Filter
    Countries_Filter =  show_Countries_Filter()

    return render_template( template_name_or_list= "index.html" , 
                           class_For_01=class_For_01, 
                           class_For_02=class_For_02,
                           Title_V = Title_V,
                           skills = my_Skill, 
                           Countries = Countries_Filter )

# ***********************************************************************************************************************
# ******************************* ADD Page Route ************************************************************************
# ***********************************************************************************************************************


@app.route("/Add")
def add_fun():
    
    class_For_01="text-white"
    class_For_02="active"
    Title_V = "Add User"

    from DataBase import show_Countries
    Countries_V1 = show_Countries()

    return render_template( template_name_or_list= "Add.html" , 
                           class_For_01=class_For_01, 
                           class_For_02=class_For_02 , 
                           Title_V= Title_V,
                           Countries=Countries_V1)

# ***********************************************************************************************************************
# ******************************* EditUser Page Route *******************************************************************
# ***********************************************************************************************************************


@app.route("/EditUser", methods=[ 'POST' ,'GET'])

def EditUser_Fun(): 

    class_For_01="text-white"
    class_For_02="text-white"
    Title_V = "Edit User"

    TT = request.args.get('EE')

    from DataBase import show_Emp_Data
    my_Skill= show_Emp_Data(TT)
   
    from DataBase import show_Countries
    Countries_V1 = show_Countries()

    return render_template( template_name_or_list="EditUser.html",
                            class_For_01=class_For_01,
                            class_For_02=class_For_02,
                            Title_V=Title_V,
                            skills=my_Skill,
                            Countries=Countries_V1)



# ***********************************************************************************************************************
# ******************************* View Page Route ***********************************************************************
# ***********************************************************************************************************************


@app.route("/ViewPage" , methods=[ 'POST' ,'GET'])

def ViewPage_Fun():


    class_For_01="text-white"
    class_For_02="text-white"
    Title_V = "View User Data"

    TT = request.args.get('TT')

    from DataBase import show_Emp_Data
    my_Skill= show_Emp_Data(TT) 
    

    return render_template(
        template_name_or_list="ViewPage.html",
        class_For_01=class_For_01,
        class_For_02=class_For_02,
        Title_V=Title_V,
        skills=my_Skill,
    )

# ***********************************************************************************************************************
# ******************************* Updata Route **************************************************************************
# ***********************************************************************************************************************

@app.route("/UpdataUserData", methods=[ 'POST' ,'GET'])

def UpdataUserData_Fun(): 
     
      class_For_01="active" 
      class_For_02="text-white"
      Title_V = "Home"

      # Data_V = request.get_json('data')
      

      first_name = request.form.get('Updated_First_Name')
      last_name = request.form.get('Updated_Last_Name')
      Telephone = request.form.get('Updated_Telephone')
      Last_Email = request.form.get('Updated_Last_Email')
      Gender = request.form.get('Updated_Gender')
      Age = request.form.get('Updated_Age')
      Country = request.form.get('Updated_Country')
      Last_Update = request.form.get('Updated_Last_Update')
      Emp_ID_01 = request.form.get('Emp_ID')
      
      Emp_Old_pic_01 = request.form.get('Emp_Old_pic')
      Emp_Old_fileInput_01 = request.form.get('Emp_Old_fileInput')
                    

      # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

      image_01 = request.form.get('image') 

      if image_01 == '' :
        final_Pic_Path = Emp_Old_fileInput_01
        
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++ Delete Old Pic +++++++++++++++++++++++++++++++++++++
    
        if Emp_Old_pic_01 != "ProfileIcon.webp" :
         supabase.storage.from_(BUCKET).remove([Emp_Old_pic_01])
         
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         
      else:
        
        file = request.files['image'] 
        file_extension = Path(file.filename).suffix
        new_filename = f"{uuid.uuid4()}{file_extension}"
        
        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        # file.save(filepath)
        # final_Pic_Path = f"images/" + new_filename
       
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
        file_data = file.read()
        upload_url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{new_filename}"
        response = requests.post(upload_url, headers=HEADERS, data=file_data)
       
        if response.status_code != 200:
            return f"Upload failed: {response.text}", 500
        
        # Public image URL
        final_Pic_Path = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{new_filename}"
    
  
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++ Delete Old Pic +++++++++++++++++++++++++++++++++++++
    
        if Emp_Old_pic_01 != "ProfileIcon.webp" :
         supabase.storage.from_(BUCKET).remove([Emp_Old_pic_01])
         
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
      from DataBase import update_Emp_Data   
      update_Emp_Data ( first_name,
                        last_name,
                        Telephone,
                        Last_Email,
                        Gender,
                        Age,
                        Country,
                        Last_Update,
                        Emp_ID_01,
                        final_Pic_Path
                   )
    

      from DataBase import show_skills
      my_Skill = show_skills()
     
      from DataBase import  show_Countries_Filter
      Countries_Filter =  show_Countries_Filter()
      
      return render_template( template_name_or_list= "index.html" , 
                              class_For_01=class_For_01, 
                              class_For_02=class_For_02,
                              Title_V = Title_V,
                              skills = my_Skill,
                              Countries = Countries_Filter )

# ***********************************************************************************************************************
# ******************************* ADD Route *****************************************************************************
# ***********************************************************************************************************************

@app.route("/ADDNewUserData", methods=[ 'POST' ,'GET'])

def ADDNewUserData_Fun(): 
     
      class_For_01="active" 
      class_For_02="text-white"
      Title_V = "Home"
      
      # Data_V = request.get_json('data')
      
      # from DataBase import ADD_Emp_Data   
     
      # ADD_Emp_Data (    Data_V['New_First_Name'],
      #                   Data_V['New_Last_Name'],
      #                   Data_V['New_Telephone'],
      #                   Data_V['New_Last_Email'],
      #                   Data_V['New_Gender'],
      #                   Data_V['New_Age'],
      #                   Data_V['New_Country'],
      #                   Data_V['New_Createdate'],
      #                   Data_V['New_Last_Update'],
      #                   filepath)
      
      first_name = request.form.get('New_First_Name')
      last_name = request.form.get('New_Last_Name')
      Telephone = request.form.get('New_Telephone')
      Last_Email = request.form.get('New_Last_Email')
      Gender = request.form.get('New_Gender')
      Age = request.form.get('New_Age')
      Country = request.form.get('New_Country')
      Createdate = request.form.get('New_Createdate')
      Last_Update = request.form.get('New_Last_Update')
      image_01 = request.form.get('image') 

      if image_01 == '' :
        image_url = "https://elolabnvelujlzrdtgdu.supabase.co/storage/v1/object/public/images/ProfileIcon.webp"
      else:
        file = request.files['image']  
     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if 'image' not in request.files:
          # return "No file part", 400
          image_url = "https://elolabnvelujlzrdtgdu.supabase.co/storage/v1/object/public/images/ProfileIcon.webp"
      
        if file.filename == '' :
        #  return "No selected file", 400
         image_url = "https://elolabnvelujlzrdtgdu.supabase.co/storage/v1/object/public/images/ProfileIcon.webp"

        else:
    # Save the file to the upload folder

          file_extension = Path(file.filename).suffix
        # new_filename = f"{first_name} _ {last_name}{file_extension}" 
          new_filename = f"{uuid.uuid4()}{file_extension}"
        
        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        # file.save(filepath)
        # final_Pic_Path = filepath[14:]
        # final_Pic_Path = f"images/" + new_filename
        
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
        file_data = file.read()
        upload_url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{new_filename}"
        response = requests.post(upload_url, headers=HEADERS, data=file_data)
        
        if response.status_code != 200:
            return f"Upload failed: {response.text}", 500

        # Public image URL
        image_url = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{new_filename}"
    
  
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  

      from DataBase import ADD_Emp_Data   

      ADD_Emp_Data (   first_name,
                       last_name,
                        Telephone,
                        Last_Email,
                        Gender,
                        Age,
                        Country,
                        Createdate,
                        Last_Update,
                        image_url)


      from DataBase import show_skills
      my_Skill = show_skills()


      return render_template( template_name_or_list= "index.html" , 
                              class_For_01=class_For_01, 
                              class_For_02=class_For_02,
                              Title_V = Title_V,
                              skills = my_Skill )



# ***********************************************************************************************************************
# ******************************* Delete Route **************************************************************************
# ***********************************************************************************************************************



@app.route('/delete_Fun', methods = ['POST'])

def delete_Fun():

  # V1 = request.get_json()
  # result_01 = json.loads(V1)
  
  
  Emp_ID_01 = request.form.get('Emp_ID')
  Old_Pic_01 = request.form.get('Old_Pic')
      
  print(Old_Pic_01)    
  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # ++++++++++++++++++++++ Delete Old Pic +++++++++++++++++++++++++++++++++++++
    
  if Old_Pic_01 != "ProfileIcon.webp" :
      supabase.storage.from_(BUCKET).remove([Old_Pic_01])

  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
  from DataBase import Delete_skill
  Delete_skill(Emp_ID_01)

  
  from DataBase import show_skills

  my_Skill = show_skills()
  class_For_01="active" 
  class_For_02="text-white"
  Title_V = "Home"

  return render_template( template_name_or_list = "index.html" , 
                           class_For_01=class_For_01, 
                           class_For_02=class_For_02,
                           Title_V = Title_V,
                           skills = my_Skill )


# ***********************************************************************************************************************
# ******************************* Search Route **************************************************************************
# ***********************************************************************************************************************


@app.route('/Search_Data',  methods=[ 'POST' ,'GET'])

def Search_Fun():
  

  class_For_01="active" 
  class_For_02="text-white"
  Title_V = "Home"

#   Data_V = request.get_json('data')
  
  TT = request.args.get('TT')

  from DataBase import Show_Filter_Emp

  my_Skill = Show_Filter_Emp(TT)
  

  return render_template( template_name_or_list = "index.html" , 
                           class_For_01=class_For_01, 
                           class_For_02=class_For_02,
                           Title_V = Title_V,
                           skills = my_Skill )




# ***********************************************************************************************************************
# ******************************* Filter By Country *********************************************************************
# ***********************************************************************************************************************


@app.route('/Filter_Data_ByCountry',  methods=[ 'POST' ,'GET'])

def Filter_Data_ByCountry_Fun():
  

  class_For_01="active" 
  class_For_02="text-white"
  Title_V = "Home"

#   Data_V = request.get_json('data')
  
  TT = request.args.get('TT')

  from DataBase import Show_Filter_Emp_ByCountry
  my_Skill = Show_Filter_Emp_ByCountry(TT)
  
  from DataBase import  show_Countries_Filter
  Countries_Filter =  show_Countries_Filter()

  return render_template( template_name_or_list = "index.html" , 
                           class_For_01=class_For_01, 
                           class_For_02=class_For_02,
                           Title_V = Title_V,
                           skills = my_Skill,
                           Countries = Countries_Filter )



# # ***********************************************************************************************************************
# # ******************************* Upload pic        *********************************************************************
# # ***********************************************************************************************************************

    

# @app.route('/upload', methods=['POST'])
# def upload_fun():

  
#     if 'file' not in request.files:
#         return "No file part", 400
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return "No selected file", 400
    
#     # Save the file to the upload folder
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
   
#     file.save(filepath)
    
#     # with open(filepath, "rb") as image_file:
#     #  encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
#     return  render_template("Add.html")
  
  
  
  