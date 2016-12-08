var map;


function initMap() {
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
    
  }

}


