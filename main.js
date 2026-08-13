/* ==========================================================================
   TRENZAS - Observatorio de los Derechos de los Pueblos Étnicos

   Dos comportamientos, nada más:
     1. Aparición de bloques al entrar en pantalla (IntersectionObserver).
     2. Cierre del aviso de borrador.

   No se usa ningún listener de scroll. IntersectionObserver hace el trabajo
   fuera del hilo de renderizado y no dispara en cada cuadro.
   ========================================================================== */

(function () {
  'use strict';

  var prefiereMenosMovimiento = window.matchMedia(
    '(prefers-reduced-motion: reduce)'
  );

  /* ---- 1. Aparición al entrar en pantalla ------------------------------ */

  function activarAparicion() {
    var bloques = document.querySelectorAll('.reveal');
    if (!bloques.length) return;

    // Sin soporte o con movimiento reducido: todo visible de entrada.
    if (prefiereMenosMovimiento.matches || !('IntersectionObserver' in window)) {
      bloques.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }

    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        entrada.target.classList.add('is-visible');
        observador.unobserve(entrada.target);
      });
    }, {
      rootMargin: '0px 0px -8% 0px',
      threshold: 0.12
    });

    bloques.forEach(function (el) { observador.observe(el); });
  }

  /* ---- 2. Aviso de borrador -------------------------------------------- */

  function activarAviso() {
    var boton = document.querySelector('[data-close-notice]');
    var aviso = document.getElementById('aviso-borrador');
    if (!boton || !aviso) return;

    boton.addEventListener('click', function () {
      aviso.hidden = true;
      document.body.style.paddingBottom = '0';
    });
  }

  /* ---- Arranque --------------------------------------------------------- */

  function iniciar() {
    activarAparicion();
    activarAviso();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', iniciar, { once: true });
  } else {
    iniciar();
  }
})();
