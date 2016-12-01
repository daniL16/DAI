var map;
var directionsDisplay;


function initMap(name, lati, longi) {
directionsDisplay = new google.maps.DirectionsRenderer();
   map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 41.850033, lng: -87.6500523},
    zoom: 10
  });
    
    if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    }); 
    


  var p = {lat: 41.850033, lng:  -87.6500523};
  var marker = new google.maps.Marker({
        position: p,
        map: map,
        title: name
    });

  var directionsService = new google.maps.DirectionsService();

  var request = {
    origin:map.getCenter(),
    destination:p,
    travelMode: google.maps.TravelMode.DRIVING
  };
  directionsService.route(request, function(result, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(result);
    }
  });
    }
}


