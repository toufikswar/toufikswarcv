$(document).ready(function(){
  $("#ibm,#bnp,#ccl,#mastercard").on("shown.bs.collapse", function(event){
    $(this).next().children("a").children("i").addClass('fa-minus-circle').removeClass('fa-plus-circle');
  });
  $("#ibm,#bnp,#ccl,#mastercard").on("hidden.bs.collapse", function(event){
    $(this).next().children("a").children("i").addClass('fa-plus-circle').removeClass('fa-minus-circle');
  });
});