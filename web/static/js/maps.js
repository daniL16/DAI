var map;

function initMap() {
   var latitud = document.getElementById('latitud').value;
   var longitud = document.getElementById('longitud').value;
   map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
  });
}
