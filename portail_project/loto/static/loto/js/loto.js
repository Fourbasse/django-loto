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
  $('#loto_sous_menu').tabs();

  let csrftoken = getCookie('csrftoken');
  // console.log(csrftoken);
  $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader('Csrf-Token', csrftoken);
        }
    });

  $('#btn').on('click',function(){
    let $answer = $('#answer');
    let value=$('#btn').attr('action');
    if ( value == "bdd_update"){
      // let request=new Request('test/',{method: 'POST',body:data})
      // fetch(request)
      //   .then(response => response.json())
      //   .then(result => {console.log(result);})
    $.ajax({
      headers: { "X-CSRFToken": csrftoken },
      url: '',
      type: "post",
      data: {'x':value},
      success: function(test){
        $('body').empty();
        $('body').append(test);
      }
    });
  }
  });
  $('#btn_sim').on('click',function(){
    let $answer = $('#id_sim');
    let value=$answer.val();
    console.log(value);
    $.ajax({
      headers: { "X-CSRFToken": csrftoken },
      url: 'simulation',
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
        $('#loto_tableau_tirages').DataTable();
      }

    });
  });

});
