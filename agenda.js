document.addEventListener("DOMContentLoaded", function() {
    const calendario = document.getElementById('calendario');
    const fechaActual = new Date();
    let mes = fechaActual.getMonth();
    let año = fechaActual.getFullYear();

    function actualizarCalendario() {
        const primerDia = new Date(año, mes, 1);
        const ultimoDia = new Date(año, mes + 1, 0);
        const nombreMes = primerDia.toLocaleString('es-ES', { month: 'long' });
        const diasEnMes = ultimoDia.getDate();
        const primerDiaSemana = primerDia.getDay();

        // Limpiar el calendario
        calendario.innerHTML = '';

        // Mostrar el nombre del mes
        const mesElemento = document.createElement('div');
        mesElemento.id = 'mes';
        mesElemento.textContent = `${nombreMes} ${año}`;
        calendario.appendChild(mesElemento);

        // Mostrar los días de la semana
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

        // Mostrar los días del mes
        for (let i = 0; i < primerDiaSemana; i++) {
            const diaElemento = document.createElement('div');
            diaElemento.classList.add('dia');
            calendario.appendChild(diaElemento);
        }
        for (let dia = 1; dia <= diasEnMes; dia++) {
            const diaElemento = document.createElement('input');
            diaElemento.type = 'text';
            diaElemento.classList.add('dia');
            diaElemento.classList.add('dia-numero'); // Añadir clase para estilos de números del mes
            diaElemento.value = dia; // Mostrar número del día
            calendario.appendChild(diaElemento);
        }

        // Añadir botón para avanzar al siguiente mes
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


        // Añadir botón para retroceder al mes anterior
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
