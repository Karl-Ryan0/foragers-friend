// Initialize the map
let mymap = L.map('map').setView([53.608, -6.191], 13);

let allMarkers = [];

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
        .setContent('Latitude: ' + lat + '<hr>Longitude: ' + lon + '<hr><button type="button" id="popup-button" class="btn btn-primary">Add location</button>')
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

// Update the year dynamically
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('current-year').textContent = new Date().getFullYear();
});

const typeMapping = {
    1: 'Strawberries',
    2: 'Blackberries',
    3: 'Elderberries',
    4: 'Garlic',
    5: 'Nettles'
};

// Fetches a list of locations from the database and updates the map
function fetchLocationsAndUpdateMap(url = '/location-data') {
    fetch(url)
        .then(response => response.json())
        .then(locations => {
            // Clear existing markers
            allMarkers.forEach(marker => mymap.removeLayer(marker));
            allMarkers = [];

            // Add new markers
            locations.forEach(location => {
                // Directly use the type name if available
                let typeName = location.type__name || 'Unknown Type';
                let marker = L.marker([location.latitude, location.longitude])
                              .addTo(mymap)
                              .bindPopup(`<b>${typeName}</b><hr>${location.notes || ''}<hr><button class="btn btn-primary" onclick="toggleFavorite(${location.id})">Add to Favorites</button>`);
                allMarkers.push(marker);
            });
        })
        .catch(error => console.error('Error fetching location data:', error));
}


// Call the function to update the map with initial data
fetchLocationsAndUpdateMap();

// Allows user to mark a location as favorite
function toggleFavorite(locationId) {
    fetch(`/toggle-favorite/${locationId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        console.log('Favorite status toggled', data);
    })
    .catch(error => console.error('Error toggling favorite:', error));
}

function filterMapByType() {
    var selectedType = document.getElementById('typeFilter').value;
    var filterUrl = selectedType ? '/get_filtered_locations?type=' + selectedType : '/location-data';
    

    // Call the function to fetch and update the map with filtered data
    fetchLocationsAndUpdateMap(filterUrl);
}

