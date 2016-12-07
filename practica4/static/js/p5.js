
$(document).ready(function(){
  $(".aumentarFuente").click(function(){
  	var fuente = $('body').css('font-size');
    var act = parseFloat(fuente, 10);
	$('body').css('font-size', act+0.5);
	return false;
  });
 
  $(".disminuirFuente").click(function(){
  	var fuente = $('body').css('font-size');
        var act = parseFloat(fuente, 10);
	$('body').css('font-size', act-0.5);
	return false;
  });
  
  $(".cambiarColor").click(function(){
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
});
    
   $('#submenu').hide();
    
  
  $('#rest').hover(function(e) {
       $('#submenu').toggle(300,stop);
     });
	
    

        

    
});

