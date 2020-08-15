document.getElementById("p2").style.color = "blue";

  $("#file-picker").change(function(){

      var input = document.getElementById('file-picker');

      for (var i=0; i<input.files.length; i++)
      {
      //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
          var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()

          if ((ext == 'jpg') || (ext == 'png'))
          {
              $("#msg").text("Files are supported")
          }
          else
          {
              $("#msg").text("Files are NOT supported")
              document.getElementById("file-picker").value ="";
          }
      }
  });


  $("form :input").change(function() {
    $(this).closest('form').data('changed', true);
  });
  $('#mybutton').click(function() {
    if($(this).closest('form').data('changed')) {
       //do something
    }
  });
