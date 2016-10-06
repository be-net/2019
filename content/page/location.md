+++
date = "2016-05-05T21:48:51-07:00"
title = "Location and Contact"
slug = "location"
+++

# Location

The BeNet 2016 meeting will be held at the Université Catholique de Louvain
(Louvain-la-Neuve), in the CORE building.

<div id="mapid" style="width: 100%; height: 400px; border: solid 1px;"></div>

<script src="https://unpkg.com/leaflet@1.0.0-rc.3/dist/leaflet.js"></script>
<script>
var mymap = L.map('mapid', {
    center: [50.6695394, 4.6151262],
    zoom: 16
	});

var mburl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw'

L.tileLayer(mburl, {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
	id: 'mapbox.streets'
}).addTo(mymap);


L.marker([50.6693, 4.6153]).addTo(mymap)
	.bindPopup("<b>CORE</b><br />BeNet2016").openPopup();

var popup = L.popup();
</script>

# Contacts
 
For any question or request please contacti
[Sophie Béreau](<mailto:sophie.bereau@gmail.com>) or
[Jean-Charles Delvenne](<mailto:jean-charles.delvenne@uclouvain.be>)
