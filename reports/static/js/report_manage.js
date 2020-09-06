let map;

function loadMap() {
    let container = document.getElementById('map');

    let options = {
        center: new kakao.maps.LatLng(36.76945236756954, 126.93164179306778),
        level: 5
    };
    
    map = new kakao.maps.Map(container, options);
}

function createMarker(latitude, longitude, content) {
    let marker = new kakao.maps.Marker({  
        map: map, 
        position: new kakao.maps.LatLng(latitude, longitude)
    });

    kakao.maps.event.addListener(marker, 'click', function() {
        infowindow = new kakao.maps.InfoWindow({
            content : content,
            removable : true
        });
        
        infowindow.open(map, marker);
    });
}

function setMaximizeImage(url) {
    let maximize_image = document.getElementById('maximize-image');
    maximize_image.src = url;
}