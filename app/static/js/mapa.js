jQuery(document).ready(function($){
  marker = null;
  var map = L.map('map').setView([-17.784071, -63.180522], 11);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  L.control.scale().addTo(map);

  $('.leaflet-container').css('cursor','crosshair'); //Cursor de cruz Mapa
  map.scrollWheelZoom.disable();


  // Agrega boton de posicion
  
  L.control.custom({
      position: 'topright',
      content: '<button class="absolute top-2 right-2 bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">' +
      '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">' +
          '<path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />' +
      '</svg>' +
      '</button>',
      style: {
        margin: '20px',
        padding: '5px 0 0 0',
        cursor: 'pointer',
      },
      events: {
        click: function(data) {
          $('#map').prepend("<div id='loading' class='absolute flex items-center justify-center bg-opacity-50 bg-black w-full h-full' style='z-index:10000;'>"+            
              "<div class='animate-spin rounded-full h-32 w-32 border-b-2 border-white'>" + 
            "</div>" +
          "</div>");

          map.findAccuratePosition({
            maxWait: 7000,
            desiredAccuracy: 25
          });
        },
      }
    })
    .addTo(map);

  // funciones de mapa
  function onAccuratePositionError(e) {
    // addStatus(e.message, 'error');
  }

  function onAccuratePositionProgress(e) {
    var message = 'En Progreso … (Presición: ' + e.accuracy + ')';
    // addStatus(message, 'progressing');
  }

  function onAccuratePositionFound(e) {
    var message = 'Ubicación encontrada (Presición: ' + e.accuracy + ')';
    // addStatus(message, 'done');
    map.setView(e.latlng, 16);
    $('body #loading').remove(); //Elimina un elemento de DOM
    marker = L.marker(e.latlng).addTo(map);
    
    if ($('#EnviarUbicacion').prop('disabled')) {
      $('#EnviarUbicacion').prop('disabled', false); //Desactiva boton
      $('#EnviarUbicacion').removeClass('cursor-not-allowed opacity-50');
    }
    console.log(marker._latlng.lat);
    console.log(marker._latlng.lng);
  }

  function addStatus(message, className) {
    var ubic = document.getElementById('status');
    ubic.innerHTML = (message);
    ubic.className = className;
  }

  function onMapClick(e) {
    if (marker != null) {
      map.removeLayer(marker);
    }
    if ($('#EnviarUbicacion').prop('disabled')) {
      $('#EnviarUbicacion').prop('disabled', false); //Desactiva boton
      $('#EnviarUbicacion').removeClass('cursor-not-allowed opacity-50');
    }
    marker = L.marker(e.latlng).addTo(map);
    console.log(marker._latlng.lat);
    console.log(marker._latlng.lng);
  }

  map.on('accuratepositionprogress', onAccuratePositionProgress);
  map.on('accuratepositionfound', onAccuratePositionFound);
  map.on('accuratepositionerror', onAccuratePositionError);
  map.on('click', onMapClick);

  });