// Initialize the map
let mymap = L.map('map').setView([53.608, -6.191], 13);

// Add a tile layer (map provider)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(mymap);

// Attempt to get the user's current position
mymap.locate({setView: true, maxZoom: 16, watch: false, enableHighAccuracy: true});

// Event when location is found
mymap.on('locationfound', function(e) {
    // Add a marker to the user's location
    L.marker(e.latlng).addTo(mymap)
        .bindPopup("You are here!");
});

// Event when location is not found (or access is denied)
mymap.on('locationerror', function(e) {
    // Set a default view if we can't get the user's location
    mymap.setView([53.608, -6.191], 13);
});

// Add an event listener to the map to capture coordinates when a user clicks
mymap.on('click', function (e) {
    let lat = e.latlng.lat.toFixed(3);
    let lon = e.latlng.lng.toFixed(3);

    // Create a popup with coordinates
    L.popup()
        .setLatLng(e.latlng)
        .setContent('Latitude: ' + lat + '<br>Longitude: ' + lon + '<br><button type="button" id="popup-button" class="btn btn-primary">Add location</button>')
        .openOn(mymap);

    // Attach a click event to the popup button
    let popupButton = document.querySelector('#popup-button');
    popupButton.addEventListener('click', function () {
        // Redirect to the 'add_item' page when the button is clicked
        window.location.href = `/add_item/?latitude=${lat}&longitude=${lon}`;
    });

    // Populate the latitude and longitude fields in the form with the selected coordinates
    document.querySelector('#id_latitude').value = lat;
    document.querySelector('#id_longitude').value = lon;
    console.log('Latitude: ' + lat + ', Longitude: ' + lon);
});

const urlParams = new URLSearchParams(window.location.search);
document.querySelector('#id_latitude').value = urlParams.get('latitude');
document.querySelector('#id_longitude').value = urlParams.get('longitude');



