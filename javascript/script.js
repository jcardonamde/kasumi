// Validación en tiempo real
const loginForm = document.getElementById('userLogin');
const registerForm = document.getElementById('registryForm');

// Verifica el comportamiento del Formulario de Login
if (loginForm) {
  const loginInputs = loginForm.querySelectorAll('input');
  const loginButton = document.getElementById('loginButton');

  // Validación en tiempo real para los inputs de login
  loginInputs.forEach(input => {
    input.addEventListener('input', () => {
      if (input.checkValidity()) {
        input.classList.add('is-valid');
        input.classList.remove('is-invalid');
      } else {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
      }
    });
  });

  // Función para manejar el submit del login
  loginForm.addEventListener('submit', (event) => {
    event.preventDefault();

    // Verificar si todos los campos están completos
    const usuarioInput = document.getElementById('usuario').value.trim();
    const passwordInput = document.getElementById('password').value.trim();
    const tipoUsuario = document.getElementById('tipo_usuario').value;

    if (!usuarioInput || !passwordInput || !tipoUsuario) {
      // Mostrar modal de error si los campos están vacíos
      const errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
      errorModal.show();
    } else {
      localStorage.setItem('usuario', usuarioInput);
      localStorage.setItem('perfil', tipoUsuario);

      window.location.href = 'home.html';
    }
  });
}

// Verifica el comportamiento del Formulario de Registro
if (registerForm) {
  const registerInputs = registerForm.querySelectorAll('input');
  const registerSubmitButton = document.getElementById('submitButton');

  // Validación en tiempo real para los inputs de registro
  registerInputs.forEach(input => {
    input.addEventListener('input', () => {
      if (input.checkValidity()) {
        input.classList.add('is-valid');
        input.classList.remove('is-invalid');
      } else {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
      }
      toggleRegisterSubmitButton();
    });
  });

  // Habilitar/deshabilitar botón de enviar en el formulario de registro
  function toggleRegisterSubmitButton() {
    const allValid = [...registerInputs].every(input => input.checkValidity());
    registerSubmitButton.disabled = !allValid;
  }

  // Manejar el submit del formulario de registro
  registerForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const successRegistryModal = new bootstrap.Modal(document.getElementById('successRegistryModal'));
    successRegistryModal.show();
  });
}

// Mostrar modal de éxito en home.html
document.addEventListener('DOMContentLoaded', () => {
  const successLoginModal = document.getElementById('successLoginModal');

  if (successLoginModal) {
    const modalInstance = new bootstrap.Modal(successLoginModal);
    modalInstance.show();
  }
});

// Redirecciona al usuario hacia la pantalla de Login
function loginSuccess() {
  const successLoginModal = new bootstrap.Modal(document.getElementById('successLoginModal'));
  successLoginModal.show();
}

function goToLoginScreen() {
  window.location.href = 'index.html';
}