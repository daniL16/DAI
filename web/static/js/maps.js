
function initMap() {
    "use strict";
  var my_rest = {lat: parseFloat(document.getElementById('latitud').value), lng: parseFloat(document.getElementById('longitud').value)};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: my_rest
        });
        var marker = new google.maps.Marker({
          position: my_rest,
          map: map
        });
}
