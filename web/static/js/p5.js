
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


    function paginador(page){
    var pagina_actual=page;

 $.ajax({
                url: "/quiero_filas_desde_la",
                data: { fila: pagina_actual*10},
                type: 'get',                        
                success: function(datos) {
                        Visualiza_filas (datos);  
                },
                failure: function(datos) {
                        alert('esto no vá');
                }
        });
}



});


function Visualiza_datos (datos) {
    console.log(lista_articulos);
    var $contendor_principal = $('#resultado_busqueda') ;
}
   
$('#page2').on('click', function(e){
   paginador(2);
});