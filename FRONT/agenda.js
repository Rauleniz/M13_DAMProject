document.addEventListener("DOMContentLoaded", function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');

    const calendario = document.getElementById('calendario');
    const modal = document.getElementById("modal");
    const span = document.getElementsByClassName("close")[0];
    const form = document.getElementById("evento-form");
    const eventoFecha = document.getElementById("evento-fecha");

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    function abrirModal(fecha) {
        eventoFecha.value = fecha;
        modal.style.display = "block";
    }

    form.onsubmit = function(event) {
        event.preventDefault();
        const titulo = document.getElementById("evento-titulo").value;
        const descripcion = document.getElementById("evento-descripcion").value;
        const fecha = eventoFecha.value;

        fetch(`http://127.0.0.1:5000/post/agenda/${usuario_id}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                agenda_fecha: fecha,
                agenda_titulo: titulo,
                agenda_descripcion: descripcion
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensaje) {
                alert(data.mensaje);
                modal.style.display = "none";
                actualizarCalendario();
            } else {
                alert("Error al guardar el evento");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("Error al guardar el evento");
        });
    };

    const fechaActual = new Date();
    let mes = fechaActual.getMonth();
    let año = fechaActual.getFullYear();

    function actualizarCalendario() {
        const primerDia = new Date(año, mes, 1);
        const ultimoDia = new Date(año, mes + 1, 0);
        const nombreMes = primerDia.toLocaleString('es-ES', { month: 'long' });
        const diasEnMes = ultimoDia.getDate();
        const primerDiaSemana = primerDia.getDay();

        calendario.innerHTML = '';

        const mesElemento = document.createElement('div');
        mesElemento.id = 'mes';
        mesElemento.textContent = `${nombreMes} ${año}`;
        calendario.appendChild(mesElemento);

        const diasElemento = document.createElement('div');
        diasElemento.id = 'dias';
        const diasSemana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];
        for (let dia of diasSemana) {
            const diaElemento = document.createElement('div');
            diaElemento.classList.add('dia');
            diaElemento.textContent = dia;
            diasElemento.appendChild(diaElemento);
        }
        calendario.appendChild(diasElemento);

        for (let i = 0; i < primerDiaSemana; i++) {
            const diaElemento = document.createElement('div');
            diaElemento.classList.add('dia');
            calendario.appendChild(diaElemento);
        }
        for (let dia = 1; dia <= diasEnMes; dia++) {
            const diaElemento = document.createElement('div');
            diaElemento.classList.add('dia');
            diaElemento.classList.add('dia-numero');
            diaElemento.textContent = dia;

            diaElemento.addEventListener('click', () => {
                const fechaSeleccionada = `${año}-${mes + 1}-${dia}`;
                abrirModal(fechaSeleccionada);
            });

            calendario.appendChild(diaElemento);
        }

        const avanzarElemento = document.createElement('div');
        avanzarElemento.id = 'avanzar';
        const botonAvanzar = document.createElement('button');
        botonAvanzar.textContent = 'Avanzar';
        botonAvanzar.addEventListener('click', () => {
            mes++;
            if (mes === 12) {
                mes = 0;
                año++;
            }
            actualizarCalendario();
        });
        avanzarElemento.appendChild(botonAvanzar);
        calendario.appendChild(avanzarElemento);

        const retrocederElemento = document.createElement('div');
        retrocederElemento.id = 'retroceder';
        const botonRetroceder = document.createElement('button');
        botonRetroceder.textContent = 'Retroceder';
        botonRetroceder.addEventListener('click', () => {
            mes--;
            if (mes === -1) {
                mes = 11;
                año--;
            }
            actualizarCalendario();
        });
        retrocederElemento.appendChild(botonRetroceder);
        calendario.appendChild(retrocederElemento);
    }

    actualizarCalendario();
});
