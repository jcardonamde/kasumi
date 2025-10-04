/**
 * Funcionalidad JavaScript optimizada para el formulario de login
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';
    
    // Validación de formulario
    initFormValidation();
    
    // Funcionalidad simple para el mensaje de "¿Olvidaste tu contraseña?"
    initPasswordHelp();

    // Funcionalidad simple para el mensaje de "Contacta al administrador"
    initContactAdmin();
    
    // Auto-remover mensajes de error del servidor
    initAutoRemoveServerErrors();
});

/**
 * Inicializa la validación del formulario
 */
function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                
                // Mostrar mensaje de error personalizado
                showValidationError('Por favor, completa todos los campos requeridos.');
            } else {
                // Mostrar indicador de carga
                showLoadingState(form);
            }
            
            form.classList.add('was-validated');
        }, false);
    });
}

/**
 * Inicializa la funcionalidad del mensaje de ayuda de contraseña
 */
function initPasswordHelp() {
    const passwordHelp = document.querySelector('.help-message_password');
    if (passwordHelp) {
        passwordHelp.addEventListener('click', function() {
            showPasswordHelpModal();
        });
    }
}

/**
 * Inicializa la funcionalidad del mensaje de ayuda de contraseña
 */
function initContactAdmin() {
    const createAccountHelp = document.querySelector('.help-message_create_user');
    if (createAccountHelp) {
        createAccountHelp.addEventListener('click', function() {
            showContactAdminModal();
        });
    }
}



/**
 * Muestra un modal elegante para ayudar de contraseña
 */
function showPasswordHelpModal() {
    // Crear overlay del modal
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    `;
    
    // Crear contenido del modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        background: white;
        border-radius: 15px;
        padding: 30px;
        max-width: 400px;
        width: 90%;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        transform: translateY(20px);
        transition: transform 0.3s ease;
        position: relative;
    `;
    
    modal.innerHTML = `
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, #D55672, #0075A2);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 15px;
                color: white;
                font-size: 24px;
            ">
                <i class="fas fa-key"></i>
            </div>
            <h3 style="margin: 0; color: #481620; font-size: 22px; font-weight: 600;">
                ¿Olvidaste tu contraseña?
            </h3>
        </div>
        
        <div style="text-align: center; margin-bottom: 25px;">
            <p style="margin: 0 0 20px; color: #6c757d; line-height: 1.5;">
                Para restablecer tu contraseña, contacta al administrador del sistema.
            </p>
            
            <div style="
                background: linear-gradient(135deg, rgba(213, 86, 114, 0.1), rgba(0, 117, 162, 0.1));
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
            ">
                <div style="margin-bottom: 12px;">
                    <i class="fas fa-envelope" style="color: #D55672; margin-right: 8px;"></i>
                    <strong style="color: #481620;">Email:</strong>
                    <span style="color: #0075A2; margin-left: 5px;">admin@kasumi.com</span>
                </div>
                <div>
                    <i class="fas fa-phone" style="color: #D55672; margin-right: 8px;"></i>
                    <strong style="color: #481620;">Teléfono:</strong>
                    <span style="color: #0075A2; margin-left: 5px;">+57 (1) 234-5678</span>
                </div>
            </div>
        </div>
        
        <div style="text-align: center;">
            <button id="closePasswordModal" style="
                background: linear-gradient(135deg, #D55672, #0075A2);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 30px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                box-shadow: 0 4px 15px rgba(213, 86, 114, 0.3);
            " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(213, 86, 114, 0.4)'" 
               onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(213, 86, 114, 0.3)'">
                <i class="fas fa-check" style="margin-right: 8px;"></i>
                Entendido
            </button>
        </div>
    `;
    
    // Agregar modal al overlay
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    // Animación de entrada
    setTimeout(() => {
        overlay.style.opacity = '1';
        modal.style.transform = 'translateY(0)';
    }, 10);
    
    // Función para cerrar el modal
    const closeModal = function() {
        overlay.style.opacity = '0';
        modal.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            if (overlay.parentNode) {
                overlay.remove();
            }
        }, 300);
    };
    
    // Event listeners para cerrar
    document.getElementById('closePasswordModal').addEventListener('click', closeModal);
    overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
            closeModal();
        }
    });
    
    // Cerrar con tecla Escape
    const escapeHandler = function(e) {
        if (e.key === 'Escape') {
            closeModal();
            document.removeEventListener('keydown', escapeHandler);
        }
    };
    document.addEventListener('keydown', escapeHandler);
}

/**
 * Muestra un modal elegante para orientar al usuario en la creación de cuenta
 */
function showContactAdminModal() {
    // Crear overlay del modal
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    `;
    
    // Crear contenido del modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        background: white;
        border-radius: 15px;
        padding: 30px;
        max-width: 400px;
        width: 90%;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        transform: translateY(20px);
        transition: transform 0.3s ease;
        position: relative;
    `;
    
    modal.innerHTML = `
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, #D55672, #0075A2);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 15px;
                color: white;
                font-size: 24px;
            ">
                <i class="fa-solid fa-users"></i>
            </div>
            <h3 style="margin: 0; color: #481620; font-size: 22px; font-weight: 600;">
                Kasumi Soft
            </h3>
        </div>
        
        <div style="text-align: center; margin-bottom: 25px;">
            <p style="margin: 0 0 20px; color: #6c757d; line-height: 1.5;">
                Si requieres acceso al aplicativo, contacta al administrador del sistema.
            </p>
            
            <div style="
                background: linear-gradient(135deg, rgba(213, 86, 114, 0.1), rgba(0, 117, 162, 0.1));
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
            ">
                <div style="margin-bottom: 12px;">
                    <i class="fas fa-envelope" style="color: #D55672; margin-right: 8px;"></i>
                    <strong style="color: #481620;">Email:</strong>
                    <span style="color: #0075A2; margin-left: 5px;">admin@kasumi.com</span>
                </div>
                <div>
                    <i class="fas fa-phone" style="color: #D55672; margin-right: 8px;"></i>
                    <strong style="color: #481620;">Teléfono:</strong>
                    <span style="color: #0075A2; margin-left: 5px;">+57 (1) 234-5678</span>
                </div>
            </div>
        </div>
        
        <div style="text-align: center;">
            <button id="closePasswordModal" style="
                background: linear-gradient(135deg, #D55672, #0075A2);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 30px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                box-shadow: 0 4px 15px rgba(213, 86, 114, 0.3);
            " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(213, 86, 114, 0.4)'" 
               onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(213, 86, 114, 0.3)'">
                <i class="fas fa-check" style="margin-right: 8px;"></i>
                Entendido
            </button>
        </div>
    `;
    
    // Agregar modal al overlay
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    // Animación de entrada
    setTimeout(() => {
        overlay.style.opacity = '1';
        modal.style.transform = 'translateY(0)';
    }, 10);
    
    // Función para cerrar el modal
    const closeModal = function() {
        overlay.style.opacity = '0';
        modal.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            if (overlay.parentNode) {
                overlay.remove();
            }
        }, 300);
    };
    
    // Event listeners para cerrar
    document.getElementById('closePasswordModal').addEventListener('click', closeModal);
    overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
            closeModal();
        }
    });
    
    // Cerrar con tecla Escape
    const escapeHandler = function(e) {
        if (e.key === 'Escape') {
            closeModal();
            document.removeEventListener('keydown', escapeHandler);
        }
    };
    document.addEventListener('keydown', escapeHandler);
}

/**
 * Muestra un mensaje de error de validación
 */
function showValidationError(message) {
    // Remover alertas existentes
    const existingAlert = document.querySelector('.validation-alert');
    if (existingAlert) {
        existingAlert.remove();
    }
    
    // Crear nueva alerta
    const alert = document.createElement('div');
    alert.className = 'alert alert-danger validation-alert';
    alert.innerHTML = `
        <i class="fas fa-exclamation-triangle me-2"></i>
        ${message}
    `;
    
    // Insertar antes del formulario
    const form = document.querySelector('.container-login_form form');
    form.insertBefore(alert, form.firstChild);
    
    // Auto-remover después de 5 segundos
    setTimeout(() => {
        if (alert.parentNode) {
            alert.remove();
        }
    }, 5000);
}

/**
 * Muestra el estado de carga en el formulario
 */
function showLoadingState(form) {
    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
        const originalText = submitButton.innerHTML;
        submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Iniciando sesión...';
        submitButton.disabled = true;
        
        // Restaurar estado original si hay error (esto se maneja en el backend)
        setTimeout(() => {
            submitButton.innerHTML = originalText;
            submitButton.disabled = false;
        }, 10000); // 10 segundos de timeout
    }
}

/**
 * Inicializa la funcionalidad para auto-remover mensajes de error del servidor
 */
function initAutoRemoveServerErrors() {
    // Si ya se procesó por el script inline, no hacer nada
    if (window.errorAutoRemoveProcessed) {
        return;
    }
    
    // Función simple y directa
    const removeServerErrors = function() {
        const serverErrors = document.querySelectorAll('.alert-danger');
        
        if (serverErrors.length === 0) {
            return;
        }
        
        // Marcar como procesado
        window.errorAutoRemoveProcessed = true;
        
        serverErrors.forEach(function(errorAlert) {
            // Verificar si ya tiene el texto informativo
            if (errorAlert.querySelector('small')) {
                return;
            }
            
            // Agregar texto informativo
            const infoText = document.createElement('small');
            infoText.style.cssText = 'display: block; margin-top: 8px; opacity: 0.7; font-style: italic;';
            infoText.textContent = 'Este mensaje se cerrará en 5 segundos';
            errorAlert.appendChild(infoText);
            
            // Auto-remover después de 5 segundos
            setTimeout(function() {
                if (errorAlert && errorAlert.parentNode) {
                    errorAlert.style.transition = 'opacity 0.5s ease';
                    errorAlert.style.opacity = '0';
                    
                    setTimeout(function() {
                        if (errorAlert && errorAlert.parentNode) {
                            errorAlert.remove();
                        }
                    }, 500);
                }
            }, 5000);
        });
    };
    
    // Ejecutar con un pequeño delay
    setTimeout(removeServerErrors, 200);
}

/**
 * Busca mensajes de error por contenido específico (fallback)
 */
function findErrorsByContent() {
    // Buscar elementos que contengan el texto específico del error de Django
    const allElements = document.querySelectorAll('*');
    const errorTexts = [
        'Por favor ingrese un correo y contraseña correctos',
        'Please enter a correct',
        'correos y contraseña correctos'
    ];
    
    allElements.forEach(element => {
        const text = element.textContent || '';
        errorTexts.forEach(errorText => {
            if (text.includes(errorText) && element.children.length === 0) {
                console.log('✅ Encontrado error por contenido:', element);
                
                // Buscar el contenedor padre que sea un alert
                let alertContainer = element;
                while (alertContainer && !alertContainer.classList.contains('alert')) {
                    alertContainer = alertContainer.parentElement;
                    if (!alertContainer || alertContainer === document.body) {
                        alertContainer = element; // Usar el elemento original si no hay contenedor alert
                        break;
                    }
                }
                
                console.log('📦 Contenedor de error:', alertContainer);
                addAutoCloseIndicator(alertContainer);
                
                // Auto-remover después de 5 segundos
                setTimeout(function() {
                    if (alertContainer.parentNode) {
                        alertContainer.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                        alertContainer.style.opacity = '0';
                        alertContainer.style.transform = 'translateY(-10px)';
                        
                        setTimeout(function() {
                            if (alertContainer.parentNode) {
                                alertContainer.remove();
                            }
                        }, 500);
                    }
                }, 5000);
            }
        });
    });
}

/**
 * Agrega un indicador visual de auto-cierre al mensaje de error
 */
function addAutoCloseIndicator(errorAlert) {
    // Crear barra de progreso para mostrar tiempo restante
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: absolute;
        bottom: 0;
        left: 0;
        height: 3px;
        background-color: rgba(255, 255, 255, 0.7);
        width: 100%;
        animation: shrinkProgress 5s linear forwards;
        border-radius: 0 0 4px 4px;
    `;
    
    // Agregar estilos de animación si no existen
    if (!document.getElementById('auto-close-styles')) {
        const style = document.createElement('style');
        style.id = 'auto-close-styles';
        style.textContent = `
            @keyframes shrinkProgress {
                from { width: 100%; }
                to { width: 0%; }
            }
            .alert-danger {
                position: relative;
                overflow: hidden;
            }
        `;
        document.head.appendChild(style);
    }
    
    // Agregar la barra de progreso al alert
    errorAlert.style.position = 'relative';
    errorAlert.style.overflow = 'hidden';
    errorAlert.appendChild(progressBar);
    
    // Agregar texto informativo
    const autoCloseText = document.createElement('small');
    autoCloseText.style.cssText = `
        display: block;
        margin-top: 8px;
        opacity: 0.8;
        font-style: italic;
    `;
    autoCloseText.textContent = 'Este mensaje se cerrará automáticamente en 5 segundos';
    errorAlert.appendChild(autoCloseText);
}
