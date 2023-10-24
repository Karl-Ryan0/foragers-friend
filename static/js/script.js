// Initialize the map and set its view to a specific location and zoom level
let mymap = L.map('map').setView([51.505, -0.09], 13);

// Add a tile layer (map provider)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(mymap);

let marker = L.marker([51.5, -0.09]).addTo(mymap);

// Add a popup to the marker
marker.bindPopup('This is a test!').openPopup();