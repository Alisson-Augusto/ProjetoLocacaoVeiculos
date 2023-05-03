const busca_agencia = document.getElementById("buscar-agencia");
const dropdown = document.getElementById("dropdown-sugestoes-agencias");


function buscar_agencias(busca) {
  // Realiza a requisição GET
  fetch("/agencias?busca="+busca)
  .then(response => {
      if (response.ok) {
          response.json().then(json => {
            console.log(json);
            dropdown.innerHTML = "";
            for(let i=0; i < json.length; i++) {
              const {localizacao, id} = json[i];
              html = `<li><a class="dropdown-item text-wrap" href="/agencias/${id}">${localizacao}</a></li>`;
              dropdown.innerHTML += html;
            }

            if(json.length > 0) {
              dropdown.classList.add("show");
            }
          });
      } else {
          throw new Error('Erro na requisição');
      }
  })
}


busca_agencia.addEventListener("input", () => {
  const busca = busca_agencia.value;
  dropdown.classList.remove("show");
  if(busca.length < 3) return;

  console.log(buscar_agencias(busca));
})

console.log("Olá mundo!")