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