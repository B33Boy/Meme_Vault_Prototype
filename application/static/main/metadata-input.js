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

});


