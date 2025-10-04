# 🌸 Kasumi - Sistema de Gestión

> **Sistema web desarrollado con Django para la gestión integral de servicios y usuarios**

## 👥 **Equipo de Desarrollo**

- 👨‍💻 **Daniel Alejandro Vargas Uzuriaga**
- 👩‍💻 **Daniela López Chica** 
- 👨‍💻 **Jonathan Cardona Calderon**
- 👩‍💻 **Luz Eleidis Baldovino González**

**Programa:** Tecnólogo en Análisis y Desarrollo de Software  
**Ficha Técnica:** 2977434  
**Institución:** SENA

![Logo SENA](https://docs.google.com/drawings/d/e/2PACX-1vRHtXZUAI_yYltgXtZnIChIn1CDQyMCtZJLQ8R-5TiVO_IjaDVPsQnYlPEotP63Jz_I06loshw4yA1X/pub?w=50&h=50)

---

## 🚀 **Descripción del Proyecto**

Kasumi es un sistema web moderno desarrollado con **Django** que proporciona una plataforma integral para la gestión de servicios, usuarios y administración. El sistema cuenta con una interfaz elegante y responsive, optimizada tanto para dispositivos de escritorio como móviles.

## ✨ **Características Principales**

### 🔐 **Sistema de Autenticación**
- Login seguro con validación de credenciales
- Mensajes de error auto-removibles (5 segundos)
- Modales elegantes para recuperación de contraseña
- Interfaz de contacto con administrador

### 🎨 **Diseño y UX**
- Interfaz moderna con degradados personalizados
- Diseño responsive para todos los dispositivos
- Animaciones suaves y transiciones CSS
- Paleta de colores: Rosa (#D55672) y Azul (#0075A2)

### 👥 **Gestión de Usuarios**
- Sistema de roles y permisos
- Perfil de usuario personalizable
- Gestión administrativa de cuentas

## 🛠 **Tecnologías Utilizadas**

### **Backend**
- **Django 4.x** - Framework web de Python
- **SQLite** - Base de datos (desarrollo)
- **Python 3.x** - Lenguaje de programación

### **Frontend**
- **HTML5** - Estructura semántica
- **CSS3** - Estilos y animaciones
- **JavaScript ES6** - Interactividad
- **Bootstrap 5** - Framework CSS
- **Font Awesome** - Iconografía

### **Arquitectura**
- **MVT (Model-View-Template)** - Patrón de Django
- **Apps modulares** - Separación de funcionalidades
- **Templates heredados** - Reutilización de código

## 📁 **Estructura del Proyecto**

```
kasumi/
├── kasumi_project/          # Configuración principal
├── accounts/                # Autenticación y usuarios
├── core/                    # Funcionalidades principales
├── gestion_usuarios/        # Gestión de usuarios
├── templates/               # Plantillas HTML
│   ├── base.html           # Template base
│   ├── base_login.html     # Template para login
│   └── accounts/           # Templates de autenticación
├── static/                  # Archivos estáticos
│   ├── css/                # Estilos CSS
│   ├── js/                 # JavaScript
│   ├── imgs/               # Imágenes
│   └── styles/             # Estilos específicos
├── requirements.txt         # Dependencias Python
└── manage.py               # Comando de Django
```

## 🚀 **Instalación y Configuración**

### **Prerrequisitos**
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### **Pasos de Instalación**

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/jcardonamde/kasumi.git
   cd kasumi
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📱 **Funcionalidades Implementadas**

### ✅ **Completadas**
- [x] Sistema de autenticación completo
- [x] Interfaz de login responsive
- [x] Modales interactivos para ayuda
- [x] Auto-remove de mensajes de error
- [x] Gestión básica de usuarios
- [x] Templates base optimizados
- [x] Estilos CSS personalizados

### 🔄 **En Desarrollo**
- [ ] Dashboard principal
- [ ] Gestión avanzada de servicios
- [ ] Reportes y estadísticas
- [ ] API REST
- [ ] Notificaciones en tiempo real

## 🎨 **Capturas de Pantalla**

### Login Screen
![Login](static/imgs/login-screenshot.png)

### Dashboard
![Dashboard](static/imgs/dashboard-screenshot.png)

## 🤝 **Contribución**

Este proyecto es parte del programa académico del SENA. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 **Contacto**

Para soporte técnico o consultas sobre el proyecto:

- **Email:** admin@kasumi.com
- **Teléfono:** +57 (1) 234-5678

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

**© 2025 Kasumi - Sistema de Gestión | Desarrollado por D2JL Inc ®**
