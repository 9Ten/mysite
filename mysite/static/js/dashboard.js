$( document ).ready(function() {
  function showFilename(){
    var x = document.getElementById("myFile");
    var output_text = "";
    if ('files' in x) {
      if (x.files.length == 0) {
        output_text = "Select a file";
      } else {
        var file = x.files[0];
        if ('name' in file) {
            output_text += "" + file.name + "<br>";
        }
      }
    } 
    else {
      if (x.value == "") {
        output_text += "Select a file";
      } else {
        output_text += "The files property is not supported by your browser!";
        output_text  += "<br>The path of the selected file: " + x.value; 
        // If the browser does not support the files property, it will return the path of the selected file instead. 
      }
    }
    document.getElementById("file").innerHTML = output_text;
  }
});
