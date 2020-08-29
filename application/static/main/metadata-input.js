$(document).ready(function(){
    
    var counter = 1;

    // Add and remove 
    $("#addRow").click(function () {
        var html = '';
        
        
        counter++;

        html += 
        `<div id="inputFormRow">
            <div class="input-group mb-3">
                <input type="text" name="desc" class="form-control m-input" placeholder="Describe the meme" autocomplete="off">
                <div class="input-group-append">'
                <button id="removeRow" type="button" class="btn btn-danger">Remove</button>
            </div>
        </div>`;
        
        $('#newRow').append(html);
    });

    // remove row
    $(document).on('click', '#removeRow', function () {
        counter--;
        $(this).closest('#inputFormRow').remove();
    });


    // $('form').on('submit', function(event){

    //     var inp_data = [];
    //     $('.form-control').each(function(){
    //         inp_data.push($(this).val());
    //         console.log($(this).val());            
    //     });

    //     event.preventDefault();

    //     $.ajax({
    //         type : 'POST',
    //         url : '/process',
    //         data: JSON.stringify(inp_data),
    //         contentType: 'application/json'

    //     }).done(function(data){
    //         if (data.error){
    //             $('#errorAlert').text(data.error).show();
    //         }
    //         else{
    //             $('#errorAlert').text(data.error).hide();
    //         }
    //     });
        
    // });

});


