$(document).ready(function(){
    if($("#MeusLevantamentos").length){
    var estaLogado = localStorage.getItem("esta_logado");
    if(estaLogado == 'false'){
        $('#modal1').modal({
            complete: function(){
                $('.tap-target').tapTarget('open');
            }
        }).modal('open');
        localStorage.setItem("esta_logado", 'true');
    }
    }
    $('.tooltipped').tooltip({delay: 50, html: true});
    $(".modal").modal();
    
})

$(document).ready(function() {
    $('select').material_select();
    $('select').on('contentChanged', function() {
        // re-initialize (update)
        $(this).material_select();
      });
  });
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: 'yyyy-mm-dd'
});

function submitform()
{
    document.forms["levantamento-edit"].submit();
}

function quantidadeObrigatoriaAcumulada(elem){
    var e = document.getElementById("id_quantidadeAcumulada");
    var itemSelecionado = e.options[e.selectedIndex].text;
    if(itemSelecionado != "---------"){
        $("#id_tipoAcumulo").prop("required", true);
    }else{
        $("#id_tipoAcumulo").prop("required", false);
    }

}

function quantidadeObrigatoriaTipo(elem){
    var e = document.getElementById("id_tipoAcumulo");
    var itemSelecionado = e.options[e.selectedIndex].text;
    if(itemSelecionado != "---------"){
        $("#id_quantidadeAcumulada").prop("required", true);
    }else{
        $("#id_quantidadeAcumulada").prop("required", false);
    }

}


// Submit post on submit
$('#formAtividade').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

function insere_atividade(val, text) {
    $('#id_atividade').append(
        $('<option></option>').val(val).html(text)
    ).trigger('contentChanged');
}

var json1;
// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $("#loader").show();
        $.ajax({
            url : "/tipologia/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(), descricao : $('#id_descricao').val(), botao_cadastrar : '3'  }, // data sent with the post request
            // handle a successful response
            success : function(json) {
            if(json.resposta == '0'){
                $('#loader').hide();
                $('#erro_atividade').show(); // remove the value from the input
                }
            else{
                $('#formularioAtividade').modal('close');
                insere_atividade(json.resposta, json.nome_atividade);
                $('#loader').hide();
                Materialize.toast('Atividade criada com sucesso!', 4000);
                $('#id_descricao').val('');
                $('#erro_atividade').hide();

            }
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $("#loader").hide();
                $('#results').html("<div class='alert-box alert radius' data-alert>Opss! Nós encontramos um erro!: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
};


function botaoSalvar(){
    $("#valor_botao").val("1");
    $('#tipologia-form').submit();
}

function botaoSim(){
    $("#valor_botao").val("0");
    $('#tipologia-form').submit();
}


