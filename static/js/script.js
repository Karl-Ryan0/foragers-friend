// Initialize the map
let mymap = L.map('map').setView([53.608, -6.191], 13);

// Add a tile layer (map provider)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(mymap);

// Add an event listener to the map to capture coordinates when a user clicks
mymap.on('click', function (e) {
    let lat = e.latlng.lat.toFixed(3);
    let lon = e.latlng.lng.toFixed(3);

    // Create a popup with coordinates
    L.popup()
        .setLatLng(e.latlng)
        .setContent('Latitude: ' + lat + '<br>Longitude: ' + lon + '<br><button type="button" id="popup-button">Add location</button>')
        .openOn(mymap);

    // Attach a click event to the popup button
    let popupButton = document.querySelector('#popup-button');
    popupButton.addEventListener('click', function () {
        // Redirect to the 'add_item' page when the button is clicked
        window.location.href = '/add_item/';
    });

    // Populate the latitude and longitude fields in the form with the selected coordinates
    document.querySelector('#id_latitude').value = lat;
    document.querySelector('#id_longitude').value = lon;
    console.log('Latitude: ' + lat + ', Longitude: ' + lon);
});


