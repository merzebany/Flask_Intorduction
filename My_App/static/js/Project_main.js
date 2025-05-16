
let classValue_V = ""
let Old_Pic_V =""

$(document).ready(function () {

  $(".Delete_View_But").on('click', function () {

    classValue_V = $(this).data('class-value');
    
    
  });


  $(document).on('click', '#DeleteViewBut01', function () {

    classValue_V = $(this).data('class-value_01');
   

  });

});


// ***************************************************************************************************
// ******************  Delete Data *******************************************************************
// ***************************************************************************************************


function delete_Fun() {

  
 
 
  let Del_Pic_Name = document.getElementById("Final_Delete")
  let Del_Pic_Name_V= Del_Pic_Name.getAttribute("data-Pic-Name")
  // let Old_Pic02 = document.querySelector(".Delete_View_But").dataset('old-pic')
  let Old_Pic = Del_Pic_Name_V.split('/').pop();


  var formData = new FormData();
  formData.append('Emp_ID', classValue_V);
  formData.append('Old_Pic', Old_Pic);
  
  $.ajax({

    url: "/delete_Fun",
    type: "POST",

    contentType: "application/json",
    context: document.body,
    data: formData,
    processData: false, 
    contentType: false
  

  }).done(function (response) {
      // Assuming the server returns the rendered HTML
      document.body.innerHTML = response; // Replace the entire page content
      window.location.href = "/"
    }).fail(function (error) {
      
      console.error("Error:", error);
    }); 
  // window.location.href = "/"
 };


// function delete_Fun_01() {

//   const dir_value = { classValue_V };
//   const s = JSON.stringify(dir_value);

//   $.ajax({

//     url: "/delete_Fun",
//     type: "POST",

//     contentType: "application/json",
//     context: document.body,
//     data: JSON.stringify(s)

//   }).done(function (response) {
//     // Assuming the server returns the rendered HTML
//     document.body.innerHTML = response; // Replace the entire page content
//   }).fail(function (error) {
//     console.error("Error:", error);
//   });

// };


// ********************************************************************************************************************
// ********************************************************************************************************************

// function View_Emp_Data_Fun(TT) {

//   const dir_value = { TT };
//   // const R = JSON.stringify(dir_value);

//   console.log(dir_value)

//   // console.log(typeof (R))

//   // console.log(R)



//   $.ajax({


//     url: "/ViewPage",
//     type: "POST",
//     headers: {
//       'Content-Type': 'application/json', // Must be exactly this
//     },
//     contentType: "application/json",
//     context: document.body,

//     data: JSON.stringify(dir_value),

//   }).done(function (response) {
//     // Assuming the server returns the rendered HTML
//     document.body.innerHTML = response; // Replace the entire page content
//   }).fail(function (error) {
//     console.error("Error:", error);
//   });

// };

// ********************************************************************************************************************
// ********************************************************************************************************************

// function Edit_Emp_Data_Fun(EE) {

//   const dir_value = { EE };
//   // const R = JSON.stringify(dir_value);

//   console.log(dir_value)


//   $.ajax({

//     url: "/EditUser",
//     type: "POST",
//     headers: {
//       'Content-Type': 'application/json', // Must be exactly this
//     },
//     contentType: "application/json",
//     context: document.body,

//     data: JSON.stringify(dir_value),

//   }).done(function (response) {
//     // Assuming the server returns the rendered HTML
//     document.body.innerHTML = response; // Replace the entire page content
//   }).fail(function (error) {
//     console.error("Error:", error);
//   });


// };

// ***************************************************************************************************
// ******************  Updata Data *******************************************************************
// ***************************************************************************************************

function Updata_Fun() {

  const now = new Date();

  const year = now.getFullYear(); // e.g., 2023
  const month = now.getMonth() + 1; // Months are zero-indexed (0 = January, 11 = December)
  const day = now.getDate(); // Day of the month (1–31)
  const hours = now.getHours(); // Hours (0–23)
  const minutes = now.getMinutes(); // Minutes (0–59)
  const seconds = now.getSeconds(); // Seconds (0–59)


  let ID_V = document.querySelector(".IDClass").childNodes[1].textContent.trim()

  let FirstName_V = document.querySelector(".FirstNameClass").value.trim()
  let FirstName_V_L = document.querySelector(".FirstName_errorlabel")

  let LastName_V = document.querySelector(".LastNameClass").value.trim()
  let LastName_V_L = document.querySelector(".LastName_errorlabel")

  let Email_V = document.querySelector(".EmailClass").value.trim()
  let Email_V_L = document.querySelector(".Email_errorlabel")

  let Telephone_V = document.querySelector(".TelephoneClass").value.trim()
  let Telephone_V_L = document.querySelector(".Telephone_errorlabel")


  let Age_V = document.querySelector(".AgeClass").value.trim()
  let Age_V_L = document.querySelector(".Age_errorlabel")
  let Age_V_L_01 = document.querySelector(".Age_errorlabel_01")


  let Country_V = document.querySelector(".CountryClass").value.trim()
  let Gender_V = document.querySelector(".GenderClass").value.trim()
  let LastUpdate_V = `${year}-${month}-${day}` + " " + `${hours}:${minutes}`

  let Pic_V = document.querySelector(".pic_for_emp").getAttribute("data-picPath")
  let Old_Pic_V = document.querySelector(".pic_for_emp").getAttribute("data-OldpicPath")

   let Old_fileInput = document.querySelector(".pic_for_emp").src;
    
 

  if (FirstName_V == "") {
    FirstName_V_L.style.display = ""
    LastName_V_L.style.display = "none"
    Email_V_L.style.display = "none"
    Telephone_V_L.style.display = "none"
    Age_V_L.style.display = "none"
    Age_V_L_01.style.display = "none"

  } else if (LastName_V == "") {
    LastName_V_L.style.display = ""
    FirstName_V_L.style.display = "none"
    Email_V_L.style.display = "none"
    Telephone_V_L.style.display = "none"
    Age_V_L.style.display = "none"
    Age_V_L_01.style.display = "none"

  } else if (Email_V == "") {
    Email_V_L.style.display = ""
    FirstName_V_L.style.display = "none"
    LastName_V_L.style.display = "none"
    Telephone_V_L.style.display = "none"
    Age_V_L.style.display = "none"
    Age_V_L_01.style.display = "none"

  } else if (Telephone_V == "") {
    Telephone_V_L.style.display = ""
    FirstName_V_L.style.display = "none"
    LastName_V_L.style.display = "none"
    Email_V_L.style.display = "none"
    Age_V_L.style.display = "none"
    Age_V_L_01.style.display = "none"

  } else if (Age_V == "") {
    Age_V_L.style.display = ""
    FirstName_V_L.style.display = "none"
    LastName_V_L.style.display = "none"
    Email_V_L.style.display = "none"
    Telephone_V_L.style.display = "none"
    Age_V_L_01.style.display = "none"

  } else if (Age_V < 5 || Age_V > 100) {
    Age_V_L_01.style.display = ""
    FirstName_V_L.style.display = "none"
    LastName_V_L.style.display = "none"
    Email_V_L.style.display = "none"
    Telephone_V_L.style.display = "none"
    Age_V_L.style.display = "none"

  } else {


    var formData = new FormData();
    const fileInput = document.getElementById('imgInput');
    
    let file = fileInput.files[0];
           
            if (!file) {
               
              // alert("Please select a file.");   ProfileIcon.webp
              console.log("++++++++++++++++++++++++++++")
              console.log(Old_Pic_V)
              console.log(Old_fileInput)
              console.log(Pic_V)

              formData.append('image','');
    
            } else {
               console.log("*************************** ")
               formData.append('image',file);
    }
    
            formData.append('Updated_First_Name', FirstName_V);
            formData.append('Updated_Last_Name', LastName_V);
            formData.append('Updated_Telephone', Telephone_V);
            formData.append('Updated_Last_Email', Email_V);
            formData.append('Updated_Gender', Gender_V);
            formData.append('Updated_Age', Age_V);
            formData.append('Updated_Country', Country_V);  
            formData.append('Updated_Last_Update', LastUpdate_V);
            formData.append('Emp_ID', ID_V);
            formData.append('Emp_Old_pic', Old_Pic_V);
            formData.append('Emp_Old_fileInput', Old_fileInput);
             
           
    $.ajax({

      url: "/UpdataUserData",
      type: "POST",
      contentType: "application/json",
      data: formData, 
      processData: false, // Don't process the data
      contentType: false, // Don't set content type

      // data: JSON.stringify({
      //   'Updated_First_Name': FirstName_V,
      //   'Updated_Last_Name': LastName_V,
      //   'Updated_Telephone': Telephone_V,
      //   'Updated_Last_Email': Email_V,
      //   'Updated_Gender': Gender_V,
      //   'Updated_Age': Age_V,
      //   'Updated_Country': Country_V,
      //   'Updated_Last_Update': LastUpdate_V,
      //   'Emp_ID': ID_V,
      //   'Emp_pic' :Pic_V
      // })

    }).done(function (response) {
      // Assuming the server returns the rendered HTML
      document.body.innerHTML = response; // Replace the entire page content
      window.location.href = "/"
    }).fail(function (error) {
      
      console.error("Error:", error);
    }); 

  }
  
};


// ***************************************************************************************************
// ******************  ADD Data **********************************************************************
// ***************************************************************************************************

async function Add_Fun() {

  const now = new Date();

  const year = now.getFullYear(); // e.g., 2023
  const month = now.getMonth() + 1; // Months are zero-indexed (0 = January, 11 = December)
  const day = now.getDate(); // Day of the month (1–31)
  const hours = now.getHours(); // Hours (0–23)
  const minutes = now.getMinutes(); // Minutes (0–59)
  const seconds = now.getSeconds(); // Seconds (0–59)


  // let ID_V = document.querySelector(".IDClass").childNodes[1].textContent.trim()

  let FirstName_V = document.querySelector(".FirstNameClass").value.trim()
  let FirstName_V_L = document.querySelector(".FirstName_errorlabel")

  let LastName_V = document.querySelector(".LastNameClass").value.trim()
  let LastName_V_L = document.querySelector(".LastName_errorlabel")

  let Email_V = document.querySelector(".EmailClass").value.trim()
  let Email_V_L = document.querySelector(".Email_errorlabel")

  let Telephone_V = document.querySelector(".TelephoneClass").value.trim()
  let Telephone_V_L = document.querySelector(".Telephone_errorlabel")

  let Age_V = document.querySelector(".AgeClass").value.trim()
  let Age_V_L = document.querySelector(".Age_errorlabel")
  let Age_V_L_01 = document.querySelector(".Age_errorlabel_01")

  let Country_V = document.querySelector(".CountryClass").value.trim()
  let Country_V_L = document.querySelector(".Country_errorlabel")

  let Gender_V = document.querySelector(".GenderClass").value.trim()
  let Gender_V_L = document.querySelector(".Gender_errorlabel")

  let LastUpdate_V = `${year}-${month}-${day}` + " " + `${hours}:${minutes}`
  let Createddate_V = `${year}-${month}-${day}` + " " + `${hours}:${minutes}`

  FirstName_V_L.style.display = "none"
  LastName_V_L.style.display = "none"
  Email_V_L.style.display = "none"
  Telephone_V_L.style.display = "none"
  Age_V_L.style.display = "none"
  Age_V_L_01.style.display = "none"
  Country_V_L.style.display = "none"
  Gender_V_L.style.display = "none"


  if (FirstName_V == "") {
    FirstName_V_L.style.display = ""
  } else if (LastName_V == "") {
    LastName_V_L.style.display = ""
  } else if (Email_V == "") {
    Email_V_L.style.display = ""
  } else if (Telephone_V == "") {
    Telephone_V_L.style.display = ""
  } else if (Age_V == "") {
    Age_V_L.style.display = ""
  } else if (Age_V < 5 || Age_V > 100) {
    Age_V_L_01.style.display = ""
  } else if (Country_V == "Choose Country here .......") {

    Country_V_L.style.display = ""
  } else if (Gender_V == "Choose here.....") {

    Gender_V_L.style.display = ""
  }
  else {
    
    var formData = new FormData();
    const fileInput = document.getElementById('imgInput');
   
            let file = fileInput.files[0];
           
            if (!file) {
               
              // alert("Please select a file.");   ProfileIcon.webp
             
              formData.append('image','');
    
            } else {
              
               formData.append('image',file);
            }
           
            
            formData.append('New_First_Name', FirstName_V);
            formData.append('New_Last_Name', LastName_V);
            formData.append('New_Telephone', Telephone_V);
            formData.append('New_Last_Email', Email_V);
            formData.append('New_Gender', Gender_V);
            formData.append('New_Age', Age_V);
            formData.append('New_Country', Country_V);
            formData.append('New_Createdate', Createddate_V);
            formData.append('New_Last_Update', LastUpdate_V);
    
    $.ajax({
      url: "/ADDNewUserData",
      type: "POST",
      data: formData, 
      // contentType: "application/json",
      processData: false, // Don't process the data
      contentType: false, // Don't set content type
    //  success: function(response) {
    //     console.log("Success:////", response);
    // },
    // error: function(xhr, status, error) {
    //     console.error("Error:", error);
      // }
      



    //   // data: JSON.stringify({
    //   //   'New_First_Name': FirstName_V,
    //   //   'New_Last_Name': LastName_V,
    //   //   'New_Telephone': Telephone_V,
    //   //   'New_Last_Email': Email_V,
    //   //   'New_Gender': Gender_V,
    //   //   'New_Age': Age_V,
    //   //   'New_Country': Country_V,
    //   //   'New_Createdate': Createddate_V,
    //   //   'New_Last_Update': LastUpdate_V
        
    //   // })



    }).done(function (response) {
      // Assuming the server returns the rendered HTML
      document.body.innerHTML = response; // Replace the entire page content
      window.location.href = "/"
    }).fail(function (error) {
      console.error("Error:", error);
     
   }); 

   }
  
}


// ***************************************************************************************************
// ******************  Search in Data ****************************************************************
// ***************************************************************************************************

function Search_Fun() {

  let Search_V = document.querySelector(".Search_But").value.trim()
  if (Search_V == "") {
    window.location.href = "/"
  } else {
    window.location.href = "/Search_Data?TT=" + Search_V
  }
  // $.ajax({
  //   url: "/Search_Data",
  //   type: "POST",
  //   contentType: "application/json",
  //   context: document.body,
  //   data: JSON.stringify({
  //     'Search_V_01': Search_V,
  //   })

  // }).done(function (response) {
  //   // Assuming the server returns the rendered HTML
  //   document.body.innerHTML = response; // Replace the entire page content
  // }).fail(function (error) {
  //   console.error("Error:", error);
  // });


}

// ***************************************************************************************************
// ******************  Filter By country in Data ****************************************************************
// ***************************************************************************************************

function Filter_Country_Fun() {

  let Filter_by_Country_v = document.querySelector(".CountryClass").value.trim()
  let Filter_Country_Icon_V = document.getElementById("Filter_Country_Icon")

  localStorage.setItem("Filter_by_Country_VV", Filter_by_Country_v)
  localStorage.setItem("Filter_by_Country_IconClass",Filter_Country_Icon_V.getAttribute("class")) 

 

  if (Filter_by_Country_v == "" || Filter_Country_Icon_V.getAttribute("class") =="bi bi-x-square" ) {
    window.location.href = "/"
  } else {
    window.location.href = "/Filter_Data_ByCountry?TT=" + Filter_by_Country_v
    Filter_by_Country_v.value = localStorage.getItem("Filter_by_Country_VV")
  }

  // $.ajax({
  //   url: "/Filter_Data_ByCountry",
  //   type: "POST",
  //   contentType: "application/json",
  //   context: document.body,
  //   data: JSON.stringify({
  //     'Search_V_01': Filter_by_Country_v,
  //   })
  // }).done(function (response) {
  //   // Assuming the server returns the rendered HTML
  //   document.body.innerHTML = response; // Replace the entire page content
    
  // }).fail(function (error) {
  //   console.error("Error:", error);
   
  // }); 
}

// function Upload_Pic_Fun() {

//   let img_code = ""
  
//   if (fileInput.files.length > 0) {
//     const file = fileInput.files[0];
//     const reader = new FileReader();

//     reader.onload = function (e) {
//       img_code = e.target.result ; //   Set the image source to the base64-encoded data URL
//     };
//     reader.readAsDataURL(file); // Read the file as a data URL
//   }

//   console.log(img_code)

//   $.ajax({

//       url: "/upload",
//       type: "POST",
//       contentType: "application/json",
//       context: document.body,
//       data: JSON.stringify({'Img_code_V_01': img_code})

//   }).done(function (response) {
//     // Assuming the server returns the rendered HTML
//     document.body.innerHTML = response; // Replace the entire page content
    
//   }).fail(function (error) {
//     console.error("Error:", error);
   
//   }); 
// }
