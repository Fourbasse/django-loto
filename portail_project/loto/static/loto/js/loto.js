// Fonction pour récupere le crsftoken
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function(){
  const request=new Request('{% url "test" %}',{method: 'POST',})

  $('#menu').tabs();

  // Partie loto tout court

  $('#loto_sous_menu').tabs();
  $('#euromillion_sous_menu').tabs();

  let csrftoken = getCookie('csrftoken');
  // console.log(csrftoken);
  $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader('Csrf-Token', csrftoken);
        }
    });
  //Loto update
  $('#loto_btn_update').on('click',function(){
    let value=$(this).attr('action');
    console.log('value');
    if ( value == "loto_bdd_update"){
        $.ajax({
          headers: { "X-CSRFToken": csrftoken },
          url: 'loto_update',
          type: "post",
          data: {'x':value},
          success: function(test){
            alert("Bdd mise à jour");
          }
        });
    }
  });
  $('#btn_sim').on('click',function(){
    let $answer = $('#loto_sim');
    let value=$answer.val();
    console.log(value);
    $.ajax({
      headers: { "X-CSRFToken": csrftoken },
      url: 'loto_simulation',
      type: "post",
      data: {'x':value},
      // dataType:"json",
      success: function(test){
        // console.log(test);
        $('#response').empty();
        $('#response').append(test);
      }
    });
  });

  $('#loto_sous_menu a').on('click',function(){
    let value=$(this).attr('href').replace('#','');
    console.log(value);
    $.ajax({
      headers: { "X-CSRFToken": csrftoken },
      url: 'loto_datatable',
      type: "post",
      data:{"id":value},
      success: function(test){
        $('#loto_tbody').empty();
        $.each(test,function(key,value){
          $('#loto_tbody').append('<tr><td>'+key+'</td><td>'+value+'</td></tr>');
        });
        $('#loto_tableau_tirages').DataTable({
          "autoWidth": false,
          "columnDefs":[
            {width: 10},
            {"width":"20px"}
          ]
        });
      }

    });
  });

  // Partie Euromillion
  // Initialisation de la base de donnée
  $('#euromillion_bdd_update').on('click',function(){
    let value=$(this).attr('action');
    console.log(value);
    if ( value == "euromillion_bdd_update"){
        $.ajax({
          headers: { "X-CSRFToken": csrftoken },
          url: 'euromillion_update',
          type: "post",
          data: {'x':value},
          success: function(test){
            alert("Bdd mise à jour");
          }
        });
    }
  });


});
