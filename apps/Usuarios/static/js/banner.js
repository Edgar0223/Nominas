function animateAndRedirect(event, url) {
    event.preventDefault();
    const body = document.body;
    body.classList.add('zoom-in');
    setTimeout(() => {
        window.location.href = url;
    }, 600); // Espera 0.6 segundos antes de redirigir
}