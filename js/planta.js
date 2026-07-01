const parametros = new URLSearchParams(window.location.search);

const id = Number(parametros.get("id"));

const planta = plantas.find((p) => p.id === id);

if (planta) {
  document.getElementById("imagen").src = planta.imagen;
  const imagen = document.getElementById("imagen");

  imagen.src = planta.imagen;
  imagen.alt = planta.cientifico;
  const lista = document.getElementById("usos");
} else {
  document.body.innerHTML = "<h1>Planta no encontrada</h1>";
}
