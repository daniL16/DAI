$(document).ready(function(){
    $("#submenu_rest").hide();
     $("#submenu_users").hide();
    $("#rest").hover(function(e){
        $("#submenu_rest").toggle(300,stop);
    });
     $("#users").hover(function(e){
        $("#submenu_users").toggle(300,stop);
    });
});


function aumentarFuente() {
  	var fuente = $('body').css('font-size');
    var act = parseFloat(fuente, 10);
	$('body').css('font-size', act+0.5);
	return false;
  }
 
  function disminuirFuente(){
  	var fuente = $('body').css('font-size');
        var act = parseFloat(fuente, 10);
	$('body').css('font-size', act-0.5);
	return false;
  }
  
  function cambiarColor(){
	if ($('body').css('color') == 'rgb(255, 255, 255)'){
  		$('body').css('color','black');
		$('body').css('background','white');
        $('footer').css('color','black');
		$('footer').css('background','white');
	}
	else{
		$('body').css('color','white');
		$('body').css('background','black');
        $('footer').css('color','white');
		$('footer').css('background','black');
	}
	return false;
}