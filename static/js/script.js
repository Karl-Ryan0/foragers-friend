// Initialize the map
var mymap = L.map('map').setView([53.608, -6.191], 13);

// Add a tile layer (map provider)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(mymap);

// Add an event listener to the map to capture coordinates when a user clicks
mymap.on('click', function (e) {
    var lat = e.latlng.lat;
    var lon = e.latlng.lng;
    // Populate the latitude and longitude fields in the form with the selected coordinates
    document.querySelector('#id_latitude').value = lat;
    document.querySelector('#id_longitude').value = lon;
    console.log('Latitude: ' + lat + ', Longitude: ' + lon);
});