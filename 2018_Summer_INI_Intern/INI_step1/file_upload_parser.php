<?php
$fileName = $_FILES["file1"]["name"]; 
$fileTmpLoc = $_FILES["file1"]["tmp_name"]; 
$fileType = $_FILES["file1"]["type"]; 
$fileSize = $_FILES["file1"]["size"]; 
$fileErrorMsg = $_FILES["file1"]["error"]; 

$userName = $_GET["user_name"];
$fileDes = "/var/www/html/wp-content/uploads/$userName";
$uploadfile = "$fileDes/$fileName";

if (!$fileTmpLoc) { 
    echo "ERROR: Please browse for a file before clicking the upload button.";
    exit();
}


if(!is_dir($fileDes)){
 mkdir($fileDes);
 echo "make fileDes <br /> ";

  if(move_uploaded_file($fileTmpLoc, "$fileDes/$fileName" )){
   echo "$fileName upload is complete1 <br /> " ;
  }

  else {
   echo "move_uploaded_file function failed1" ;
  }

}

else {
 echo "fileDes already exists <br />";
 if( file_exists($uploadfile)) {
  echo "fileName already exists <br />";
  echo "Change your file name <br />";
  exit();
 }
 else {
  echo "you can upload new file <br />"; 
  if(move_uploaded_file($fileTmpLoc, "$fileDes/$fileName")){
   echo "$fileName upload is complete2 <br /> ";
  }
  else{
   echo "move_uploaded_file function failed2 <br /> ";
  }
 }
}



?>






















