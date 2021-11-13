jQuery(document).ready(function($){
  const kmMat = [km5, km10, km15, km20, km25, km30, km35, km40, km45, km50];
  const tarifa = [300, 350, 400, 450, 500, 600, 700, 800, 900, 1000];
  // console.log(kmMat.length);
  // console.log(tarifa.length);

$('#EnviarUbicacion').on('click', function() {
  var i = 0;
  var j = 0;
  var disponibilidad = false;
  for (var i = 0; i < kmMat.length; i++) {
    if (inscrito(marker, kmMat[i])) {
      disponibilidad = true;
      break;
    }
  }
  if (disponibilidad) {
  if (inscrito(marker, urubo) == true) { j = 0.5; }
  if (inscrito(marker, montero) == true) { j = 1; }
  if (inscrito(marker, laguardia) == true) { j = 0.5; }
  if (inscrito(marker, mapajo) == true) { j = -0.5; }
  if (inscrito(marker, paurito) == true) { j = 0.5; }
  if (inscrito(marker, ppailas) == true) { j = 0.5; }

  var factor = j * 100;

  // var indice = i;
  var precio = tarifa[i] + factor;
  var precio2 = (precio + Math.ceil(precio * .25 / 50) * 50);
  console.log(precio);
  $('#precio').text('Bs. ' + precio); //cambia el codigo de precio
  $('#precioContent').text('Cotización que considera la limpieza de un pozo y una cámara séptica para vivienda'); //cambia el texto de precio
  $('#confirmar').text('Coordinar Servicio'); //cambia el texto de precio
  disponibilidad = true;
 
} else {
  $('#precio').text('Fuera de Rango'); //cambia el codigo de precio
  $('#precioContent').text('Favor contáctanos para obtener una cotización en tu zona'); //cambia el texto de precio
  $('#confirmar').text('Contactarse'); //cambia el texto de precio
  disponibilidad = false;
}
$('#confirmar').on('click', function() {
  console.log(disponibilidad);
  if (disponibilidad) {
  var codigo = precio.toString(10).split('');
  // codigo de cotización ;
  codigo.unshift(parseInt(Math.random() * 10));
  codigo.splice(2, 0, parseInt(Math.random() * 10));
  codigo.splice(4, 0, parseInt(Math.random() * 10));
  codigo.splice(6, 0, parseInt(Math.random() * 10));
  precio2 = (precio2 - precio) / 50;

  codigo = codigo[0] + codigo[1] + codigo[2] + codigo[3] + codigo[4] + codigo[5] + precio2;
  
  var url = `https://wa.me/59163439303?text=Código+de+cotización:+${codigo}%0D%0A
 ¡Hola!,+Quiero+el+servicio+de+limpieza+en+la+siguiente+direccion:%0D%0Ahttps://maps.google.com/maps?q=${marker._latlng.lat}%2C${marker._latlng.lng}&z=17&hl=es`;
} else {
  var url = `https://wa.me/59163439303?text=¡Hola! Deseo una cotización para mi zona`;
}
  
 window.open(url);
  location.reload();
});

});


function inscrito(marker, vs) {
  var x = marker._latlng.lat,
    y = marker._latlng.lng;
  var inside = false;
  for (var i = 0, j = vs.length - 1; i < vs.length; j = i++) {
    var xi = vs[i][0],
      yi = vs[i][1];
    var xj = vs[j][0],
      yj = vs[j][1];
    var intersect = ((yi > y) != (yj > y)) &&
      (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
    if (intersect) inside = !inside;
  }
  return inside;
};

$('#fueraRango').on('click', function() {
  location.reload();
    });



    const modal = document.querySelector('.main-modal');
		const closeButton = document.querySelectorAll('.modal-close');

		modalClose = () => {
			modal.classList.remove('fadeIn');
			modal.classList.add('fadeOut');
			setTimeout(() => {
				modal.style.display = 'none';
			}, 500);
		}

		openModal = () => {
			modal.classList.remove('fadeOut');
			modal.classList.add('fadeIn');
			modal.style.display = 'flex';
		}

		for (let i = 0; i < closeButton.length; i++) {

			const elements = closeButton[i];

			elements.onclick = (e) => modalClose();

			modal.style.display = 'none';

			window.onclick = function (event) {
				if (event.target == modal) modalClose();
			}
		}
    
});
