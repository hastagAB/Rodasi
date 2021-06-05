var map;
var currentLatLong = {lat: 28.612186529368817, lng: 77.19718186826185}; //New Delhi

var mapImg = document.getElementById('mapImg');
var mapImgZoom = 17;
var mapImgSize = '1400x1200';  

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: currentLatLong,
        zoom: 18,
        mapTypeId: 'satellite'
    });

    map.addListener('click', function(e) {
        map.panTo(e.latLng);
        
        mapImg.src = 'https://maps.googleapis.com/maps/api/staticmap?center='+ e.latLng.lat() +','+ e.latLng.lng() +'&zoom='+ mapImgZoom +'&size='+ mapImgSize +'&maptype=satellite&key=AIzaSyCwXbiOalbQW724Dl5LNIy91xbsLVClnvA'
    });
}

