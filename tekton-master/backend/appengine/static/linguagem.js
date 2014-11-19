
$(document).ready(function() {
    var $linguagemForm = $('#linguagem-form');
    $linguagemForm.hide();
    $('#mostrar-form-btn').click(function () {
        $linguagemForm.slideToggle();
    });

    var $linguagemInput = $('#linguagemInput');
    var $ajaxGif = $('#ajax-gif');

    var $linguagemDiv = $('#linguagemDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    var $helpLinguagemSpan = $('#help-linguagem');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha = function adicionarLinha(linguagem) {
        var linha = '<tr id="tr' + linguagem.id + '"> <td>' +
            '<td>' + linguagem.id + '</td>' +
            '<td>' + linguagem.creation + '</td>' +
            '<td>' + linguagem.descricao + '</td>' +
            '<td><button id="bt' + linguagem.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.append(linha);

        var $linhaHtml = $('#tr' +  linguagem.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();

        $('#bt' + linguagem.id).click(function() {
           $linhaHtml.fadeOut();
            $.post('/linguagems/rest/delete', {'linguagem_id': linguagem.id}).success(function() {
               $linhaHtml.remove();
            }).error(function () {
                alert('Remocao nao funfou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/linguagems/rest').success(function (linguagems) {
        for (var i = 0; i < linguagems.length; i+=1){
            adicionarLinha(linguagems[i]);
        }
    });

    $salvarBtn.click(function() {
        var linguagem = {descricao: $linguagemInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();

        var promessa = $.post('/linguagems/rest/save', linguagem);


        promessa.success(function (linguagem_do_servidor) {
            adicionarLinha(linguagem_do_servidor);
        });

        promessa.error(function(erros) {
           if (erros.responseJSON != null && erros.responseJSON.descricao != null) {
               $linguagemDiv.addClass('has-erros');
               $helpLinguagemSpan.text(erros.responseJSON.descricao);
           }
        });

        promessa.always(function(){
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        });

    });


});