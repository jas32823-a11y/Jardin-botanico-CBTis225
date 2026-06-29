const parametros = new URLSearchParams(window.location.search);

const id = Number(parametros.get("id"));

const planta = plantas.find((p) => p.id === id);

if (planta) {
  document.getElementById("nombre").textContent = planta.comun;

  document.getElementById("cientifico").textContent = planta.cientifico;

  document.getElementById("origen").textContent = planta.origen;

  document.getElementById("ubicacion").textContent = planta.ubicacion;

  document.getElementById("descripcion").textContent = planta.descripcion;

  document.getElementById("imagen").src = planta.imagen;

  const lista = document.getElementById("usos");

  planta.usos.forEach((uso) => {
    const li = document.createElement("li");

    li.textContent = uso;

    lista.appendChild(li);
  });
} else {
  document.body.innerHTML = "<h1>Planta no encontrada</h1>";
}
