/// <reference path="../../typings/globals/jquery/index.d.ts" />
$(function() {
   $('[data-toggle="tooltip"]').tooltip();
   $('[data-toggle="popover"]').popover();

   $("#botao-enviar").click(function() {
      let validacao = validaCadastro()

      if (validacao) {
         $(this).attr("data-dismiss","modal");
      }
      else {
         alert("Formulário inválido!")
      }
   })

   $('.page-item.page-item-change').click(function(){
        let childAnchor = $(this).children()[0]
        if($(childAnchor).is('a')){
            let search = $(childAnchor).attr('href')
            let path = window.location.href
            path = path.substring(path.indexOf('produto/') + ('produto/'.length))
            if(path.length===0){
                return
            }
            let atributos = path.split('&')
            let contain = false
            path = ''

            function check(item) {
                if(!item.includes('?')) item = `&${item}`
                if(item.includes(search.substring(1, search.indexOf('=')))){
                    contain = true
                    item = item.substring(0,item.indexOf('=')) + search.substring(search.indexOf('='))
                }
                path = path + item
            }
            atributos.forEach(check)

            if(!contain)path = path + search.replace('?', '&')


            $(childAnchor).attr("href", path)
        }
   })

   $(".far.fa-thumbs-up").click(function() {
      let display = $(this).parent().parent()

      let displayChildren = display.children()


      if($($(displayChildren[1]).children()[0]).hasClass("far")){
         $($(displayChildren[1]).children()[0]).removeClass("far")
         $($(displayChildren[1]).children()[0]).addClass("fas")
         let count = parseInt($(displayChildren[0]).data("like"), 10)
         $(displayChildren[0]).text(`${count + 1}`)
         $(displayChildren[0]).data('like', count + 1)
      }

      else if($($(displayChildren[1]).children()[0]).hasClass("fas")){
         $($(displayChildren[1]).children()[0]).removeClass("fas")
         $($(displayChildren[1]).children()[0]).addClass("far")
         let count = parseInt($(displayChildren[0]).data("like"), 10)
         $(displayChildren[0]).text(`${count - 1}`)
         $(displayChildren[0]).data('like', count - 1)
      }


      if($($(displayChildren[2]).children()[0]).hasClass("fas")){
         $($(displayChildren[2]).children()[0]).removeClass("fas")
         $($(displayChildren[2]).children()[0]).addClass("far")
         let count = parseInt($(displayChildren[3]).data("dislike"), 10)
         $(displayChildren[3]).text(`${count - 1}`)
         $(displayChildren[3]).data('dislike', count - 1)
      }
   })

   // 1. Inverter os valores de data-like e data-dislike.

   $(".far.fa-thumbs-down").click(function() {
      let display = $(this).parent().parent()

      let displayChildren = display.children()


      if($($(displayChildren[2]).children()[0]).hasClass("far")){
         $($(displayChildren[2]).children()[0]).removeClass("far")
         $($(displayChildren[2]).children()[0]).addClass("fas")
         let count = parseInt($(displayChildren[3]).data("dislike"), 10)
         $(displayChildren[3]).text(`${count + 1}`)
         $(displayChildren[3]).data('dislike', count + 1)
        
      }

      else if($($(displayChildren[2]).children()[0]).hasClass("fas")){
         $($(displayChildren[2]).children()[0]).removeClass("fas")
         $($(displayChildren[2]).children()[0]).addClass("far")
         let count = parseInt($(displayChildren[3]).data("dislike"), 10)
         $(displayChildren[3]).text(`${count - 1}`)
         $(displayChildren[3]).data('dislike', count - 1)
      }


      if($($(displayChildren[1]).children()[0]).hasClass("fas")){
         $($(displayChildren[1]).children()[0]).removeClass("fas")
         $($(displayChildren[1]).children()[0]).addClass("far")
         let count = parseInt($(displayChildren[0]).data("like"), 10)
         $(displayChildren[0]).text(`${count - 1}`)
         $(displayChildren[0]).data('like', count - 1)
      }
   })
})

function validaCadastro() {
   let resposta = true;
   let campo = $("#Nome");

   let bool = campo.val() != '';
   setValidation(campo, bool);
   if(!bool) resposta = false;

   campo = $("#Cep");
   bool = campo.val().replace(/-/g, '').length == 8;
   setValidation(campo, bool);
   if(!bool) resposta = false;

   campo = $("#Telefone");
   bool = campo.val() != '';
   setValidation(campo, bool);
   if(!bool) resposta = false;

   campo = $("#Numero");
   bool = campo.val() != '';
   setValidation(campo, bool);
   if(!bool) resposta = false;




   let botoes = $("input.sabores:checked")
   if (botoes.length === 0) {
      $("#salgados").addClass("is-invalid")
      $("#doces").addClass("is-invalid")
      $("#veganos").addClass("is-invalid")
      $("#sabores-feedback").addClass("d-block")
      resposta = false
   }
   else {
      $("#salgados").removeClass("is-invalid")
      $("#doces").removeClass("is-invalid")
      $("#veganos").removeClass("is-invalid")
      $("#sabores-feedback").removeClass("d-block")
   }


   botoes = $("input[name='intolerancia']:checked")
   if (botoes.length === 0) {
      $("input[name='intolerancia']").addClass("is-invalid")
      $("#intolerancia-feedback").addClass("d-block")
      resposta = false
   }
   else {
      $("input[name='intolerancia']").removeClass("is-invalid")
      $("#intolerancia-feedback").removeClass("d-block")
   }


   campo = $("#Unidade")
   if(campo.val() === '') {
      campo.css("border-color", "red");
      resposta = false;
   }
   else {
      campo.css("border-color", "green");
   }

   campo = $("#Email");
   bool = campo.val() != '';
   setValidation(campo, bool);
   if(!bool) resposta = false;

   campo = $("#Senha");
   bool = campo.val().length >= 8;
   setValidation(campo, bool);
   if(!bool) resposta = false;


   return resposta;
}


   function setValidation(item, bool){
      if(bool){
         item.removeClass("is-invalid");
         item.addClass("is-valid");
         return
      }
      item.addClass("is-invalid");
      item.removeClass("is-valid");
      resposta = false;
   }