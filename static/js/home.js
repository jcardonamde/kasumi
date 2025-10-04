// Función para cargar el mensaje de bienvenida
function loadWelcomeMessage() {
    const usuario = localStorage.getItem('usuario');
    const perfil = localStorage.getItem('perfil');

    if (usuario && perfil) {
        const welcomeMessage = `¡Hola, ${usuario}! Has iniciado sesión como ${perfil}.`;
        document.getElementById('welcomeMessage').textContent = welcomeMessage;

        const profileName = `${perfil}`;
        document.getElementById('nombrePerfil').textContent = profileName;
    } else {
        // Si no hay datos en localStorage, redirigir al login
        window.location.href = 'index.html';
    }
}

// Función para cerrar sesión
function logout() {
    // Elimina los datos del localStorage
    localStorage.removeItem('usuario');
    localStorage.removeItem('perfil');

    // Redirige al login
    window.location.href = 'index.html';
}

// Asignar eventos y cargar el mensaje al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    loadWelcomeMessage();

    // Asignar evento al botón de cerrar sesión
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', logout);
    }
});
