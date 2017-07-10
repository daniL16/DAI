
function initMap() {
    "use strict";
  var my_rest = {lat: Number(document.getElementById('latitud').value), lng: Number(document.getElementById('longitud').value)};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: my_rest
        });
        var marker = new google.maps.Marker({
          position: my_rest,
          map: map
        });
}
