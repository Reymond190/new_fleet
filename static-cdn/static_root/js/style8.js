
$(document).ready(function(){
$("#b1").hide();
$("#c1").hide();
$("#v1").hide();
$("#vt1").hide();
$("#vg1").hide();
$("#c").click(function(){
$("#c1").show();
$("#b1").hide();
$("#v1").hide();
$("#vt1").hide();
$("#vg1").hide();
$("#check1").click(function () {
    $(".ch1").prop('checked', $(this).prop('checked'));
});
});
$("#b").click(function(){
$("#b1").show();
$("#c1").hide();
$("#v1").hide();
$("#vt1").hide();
$("#vg1").hide();
$("#check2").click(function () {
    $(".ch2").prop('checked', $(this).prop('checked'));
});
});
$("#vt").click(function(){
$("#vt1").show();
$("#b1").hide();
$("#c1").hide();
$("#v1").hide();
$("#vg1").hide();
$("#check3").click(function () {
    $(".ch3").prop('checked', $(this).prop('checked'));
});
});
$("#v").click(function(){
$("#v1").show();
$("#b1").hide();
$("#c1").hide();
$("#vt1").hide();
$("#vg1").hide();
$("#check4").click(function () {
    $(".ch4").prop('checked', $(this).prop('checked'));
});
});
$("#vg").click(function(){
$("#vg1").show();
$("#v1").hide();
$("#b1").hide();
$("#c1").hide();
$("#vt1").hide();
});
});
function myFunction() {
var input, filter, table, tr, td, i, txtValue;
input = document.getElementById("myInput");
filter = input.value.toUpperCase();
table = document.getElementById("myTable");
tr = table.getElementsByTagName("tr");
for (i = 0; i < tr.length; i++) {
td = tr[i].getElementsByTagName("td")[0];
if (td) {
txtValue = td.textContent || td.innerText;
if (txtValue.toUpperCase().indexOf(filter) > -1) {
tr[i].style.display = "";
} else {
tr[i].style.display = "none";
}
}
}}
function myFunction() {
  window.print();
  }
  function myText(){
  $('#sample').removeClass('sample');
$('#sample').show();
 $('#sample').removeClass('col-md-6');
  $('#map').hide();
}
 function myText1(){
  $('#sample').show();
  $('#sample').addClass('sample');
  $('#map').show();
    $('#map').removeClass('d');

}
function myText2(){
$('#map').show();
 $('#map').removeClass('col-md-6');
   $('#map').addClass('d');
  $('#sample').hide();
}
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
