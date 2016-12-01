
	var chart;
	$(document).ready(function() {
		chart = new Highcharts.Chart({
			chart: {
				renderTo: 'graficaLineal'
			},
			title: {
				text: 'Porcentaje de Visitas por Paises'
			},
			subtitle: {
				text: 'Jarroba.com'
			},
			plotArea: {
				shadow: null,
				borderWidth: null,
				backgroundColor: null
			},
			tooltip: {
				formatter: function() {
					return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
				}
			},
			plotOptions: {
				pie: {
					allowPointSelect: true,
					cursor: 'pointer',
					dataLabels: {
						enabled: true,
						color: '#000000',
						connectorColor: '#000000',
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
						}
					}
				}
			},
		    series: [{
				type: 'pie',
				name: 'Browser share',
				data: [
						['España',35.38],
						['México',21.0],
						['Colombia',9.45],
						['Perú',5.74],
						['Argentina',5.14],
						['Chile',4.89],
						['Venezuela',3.04],
						['Ecuador',2.53],
						['Bolivia',1.66],
						['Rep. Dominicana',1.12],
						['Guatemala',1.08],
						['Costa Rica',1.07],
						['Estados Unidos',1.03],
						['+81 paises',6.87]
					]
			}]
		});
	});			
