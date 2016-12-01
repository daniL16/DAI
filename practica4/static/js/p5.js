
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
	}
	else{
		$('body').css('color','white');
		$('body').css('background','black');
	}
	return false;
});
    
   $('#submenu').hide();
    
  
  $('#rest').hover(function(e) {
       $('#submenu').toggle(300,stop);
     });
	
    
 $.ajax({
                url: "/quiero_filas_desde_la",
                data: { fila: 50},
                type: 'get',                        
                success: function(datos) {
                        Visualiza_filas (datos);  
                },
                failure: function(datos) {
                        alert('esto no vá');
                }
        });
        

    
});

