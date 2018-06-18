$(document).ready(function (){
  $(document).on('submit', '#contact_form', function(e){
    e.preventDefault();  
    $('#contact_form button').prop("disabled", true);
    $("#loader").css('display','block');
      $.ajax({
        type:'POST',
        url:'/contact/',
        data: {
          full_name:$('#id_full_name').val(),
          email: $('#id_email').val(),
          message: $('#id_message').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val(),
        },
        dataType: 'json',
        success: function(response){
          
          if (response.status === 'sent'){
              $("#loader").css('display','none');
              $("#contact_alert").addClass('alert-success').fadeIn();
              $("#contact_form")[0].reset();
              $('#contact_form button').prop("disabled", false); 
              $('#contact_form').remove();
          } else if (response.status === 'failed'){
              $("#loader").css('display','none');
              console.log("failed to send message")
              $("#message").text("The message couldn't be sent");
              $("#message").prev().children('i').removeClass('fa-thumbs-o-up').addClass('fa-times-circle');
              $("#contact_alert").addClass('alert-danger').fadeIn();
              $('#contact_form button').prop("disabled", false); 
          } else if (response.status === 'form error' && response.errors ){
            $("#loader").css('display','none');
            console.log(response.errors)
            error_data = response.errors
            $.each(error_data, function(index,value){
              console.log(index + " "+ error_data[index]);
              $("#id_"+index).addClass("is-invalid");
              $("#id_"+index).next('.invalid-feedback').show().html(String(error_data[index]));
              $('#contact_form button').prop("disabled", false); 
              //$(".invalid-feedback").show()
            });
          }
        },
    });
  });

    $("form").on("click", function(){
      console.log("test de is invalid");
      $(".is-invalid").removeClass("is-invalid");
    });
  });