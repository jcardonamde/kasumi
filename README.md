# 🌸 Kasumi - Sistema de Gestión

> **Sistema web profesional desarrollado con Django para la gestión integral de usuarios, roles y servicios**

[![Django](https://img.shields.io/badge/Django-5.0.14-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 👥 **Equipo de Desarrollo**

- 👨‍💻 **Daniel Alejandro Vargas Uzuriaga**
- 👩‍💻 **Daniela López Chica** 
- 👨‍💻 **Jonathan Cardona Calderon**
- 👩‍💻 **Luz Eleidis Baldovino González**

**Programa:** Tecnólogo en Análisis y Desarrollo de Software  
**Ficha Técnica:** 2977435  
**Institución:** SENA

![Logo SENA](https://docs.google.com/drawings/d/e/2PACX-1vRHtXZUAI_yYltgXtZnIChIn1CDQyMCtZJLQ8R-5TiVO_IjaDVPsQnYlPEotP63Jz_I06loshw4yA1X/pub?w=50&h=50)

---

## 🚀 **Descripción del Proyecto**

Kasumi es un **sistema web profesional** desarrollado con **Django 5.0** que proporciona una plataforma completa para la gestión de usuarios, roles, permisos y servicios. El sistema implementa las mejores prácticas de desarrollo web, con una arquitectura modular, seguridad robusta y una interfaz moderna y responsive.

## ✨ **Características Principales**

### 🔐 **Sistema de Autenticación Completo**
- ✅ Login seguro con sistema de sesiones de Django
- ✅ Logout con confirmación
- ✅ Cambio de contraseña para usuarios
- ✅ Mensajes de error auto-removibles (7 segundos)
- ✅ Modales elegantes para recuperación de contraseña
- ✅ Protección de rutas con decoradores `@login_required`
- ✅ Validación de permisos por rol

### 👥 **Gestión Completa de Usuarios**
- ✅ CRUD completo de usuarios (Crear, Leer, Actualizar, Eliminar)
- ✅ Modelo de usuario personalizado con campos adicionales:
  - Tipo y número de documento
  - Teléfono, dirección, ciudad
  - Fecha de nacimiento
- ✅ Lista de usuarios con búsqueda y filtros
- ✅ Vista de detalles de usuario
- ✅ Perfil de usuario ("Mi Perfil")
- ✅ Validación de formularios con mensajes claros
- ✅ Prevención de auto-eliminación

### 🎭 **Sistema de Roles y Permisos**
- ✅ CRUD completo de roles
- ✅ Asignación múltiple de roles a usuarios
- ✅ Permisos granulares configurables:
  - Ver, crear, editar, eliminar usuarios
  - Ver reportes
  - Ver configuración
- ✅ Historial de asignaciones (quién y cuándo)
- ✅ Vista de usuarios por rol
- ✅ Estados activo/inactivo

### 🎨 **Diseño y UX Profesional**
- ✅ Interfaz moderna con Bootstrap 5.3.3
- ✅ Diseño responsive para todos los dispositivos
- ✅ Animaciones suaves y transiciones CSS
- ✅ Paleta de colores corporativa: Rosa (#D55672) y Azul (#0075A2)
- ✅ Iconografía con Font Awesome 6
- ✅ Breadcrumbs para navegación
- ✅ Mensajes toast auto-removibles

### ⚙️ **Panel de Administración Django**
- ✅ Django Admin completamente configurado
- ✅ Gestión visual de usuarios, roles y asignaciones
- ✅ Filtros y búsquedas avanzadas
- ✅ Historial de acciones (solo lectura)
- ✅ Auditoría automática
- ✅ Interfaz organizada con fieldsets

## 🛠 **Tecnologías Utilizadas**

### **Backend**
- **Django 5.0.14** - Framework web de Python
- **Python 3.13** - Lenguaje de programación
- **SQLite** - Base de datos (desarrollo)
- **Django Auth** - Sistema de autenticación
- **Django Messages** - Sistema de mensajes

### **Frontend**
- **HTML5** - Estructura semántica
- **CSS3** - Estilos y animaciones
- **JavaScript ES6** - Interactividad y validaciones
- **Bootstrap 5.3.3** - Framework CSS responsive
- **Font Awesome 6** - Iconografía profesional

### **Arquitectura y Patrones**
- **MVT (Model-View-Template)** - Patrón de Django
- **Apps modulares** - Separación de responsabilidades
- **Class-Based Views (CBV)** - Vistas reutilizables
- **Templates heredados** - DRY (Don't Repeat Yourself)
- **Mixins** - LoginRequiredMixin, UserPassesTestMixin
- **Signals** - Para auditoría y eventos

## 📁 **Estructura del Proyecto**

```
kasumi/
├── 📂 kasumi_project/              # Configuración principal del proyecto
│   ├── settings.py                 # Configuración de Django
│   ├── urls.py                     # URLs principales
│   ├── wsgi.py                     # Configuración WSGI
│   └── asgi.py                     # Configuración ASGI
│
├── 📂 accounts/                    # App de autenticación y usuarios
│   ├── models.py                   # Modelo Usuario personalizado
│   ├── views.py                    # Vistas de login, logout, perfil
│   ├── forms.py                    # Formularios de usuario
│   ├── urls.py                     # URLs de autenticación
│   ├── admin.py                    # Configuración Django Admin
│   └── migrations/                 # Migraciones de BD
│
├── 📂 core/                        # App principal
│   ├── views.py                    # Vista del home
│   ├── urls.py                     # URLs principales
│   └── migrations/
│
├── 📂 gestion_usuarios/            # App de gestión de usuarios y roles
│   ├── models.py                   # Modelos: Rol, UsuarioRol, HistorialUsuario
│   ├── views.py                    # Vistas CRUD de usuarios y roles
│   ├── forms.py                    # Formularios de gestión
│   ├── urls.py                     # URLs de gestión
│   ├── admin.py                    # Configuración Django Admin
│   └── migrations/                 # Migraciones de BD
│
├── 📂 templates/                   # Plantillas HTML
│   ├── base.html                   # Template base con navbar y footer
│   ├── base_login.html             # Template para páginas de auth
│   ├── 📂 accounts/                # Templates de autenticación
│   │   ├── login.html              # Página de login
│   │   ├── perfil.html             # Mi Perfil
│   │   └── cambiar_password.html  # Cambio de contraseña
│   ├── 📂 core/                    # Templates principales
│   │   └── home.html               # Dashboard principal
│   └── 📂 gestion_usuarios/        # Templates de gestión
│       ├── 📂 usuarios/            # CRUD de usuarios
│       │   ├── lista_usuarios.html
│       │   ├── crear_usuario.html
│       │   ├── editar_usuario.html
│       │   ├── detalle_usuario.html
│       │   └── eliminar_usuario.html
│       └── 📂 roles/               # CRUD de roles
│           ├── lista_roles.html
│           ├── crear_rol.html
│           ├── editar_rol.html
│           ├── detalle_rol.html
│           └── asignar_rol.html
│
├── 📂 static/                      # Archivos estáticos
│   ├── 📂 css/                     # Estilos CSS
│   │   ├── styles.css              # Estilos globales
│   │   ├── login.css               # Estilos de login
│   │   └── home.css                # Estilos del home
│   ├── 📂 js/                      # JavaScript
│   │   └── login.js                # Funcionalidad de login
│   └── 📂 imgs/                    # Imágenes y logos
│       └── logo_kasumi.png
│
├── 📂 docs/                        # Documentación del proyecto
│   ├── ACTIVACION_MODULO_ROLES.md
│   ├── CONFIGURACION_DJANGO_ADMIN.md
│   └── INSTRUCCIONES_GESTION_USUARIOS.md
│
├── 📄 .gitignore                   # Archivos ignorados por Git
├── 📄 requirements.txt             # Dependencias Python
├── 📄 manage.py                    # Script de gestión Django
├── 📄 README.md                    # Este archivo
└── 📄 db.sqlite3                   # Base de datos (no en Git)
```

## 🚀 **Instalación y Configuración**

### **Prerrequisitos**
- **Python 3.8 o superior** (recomendado 3.13)
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)

### **Pasos de Instalación**

#### 1. **Clonar el repositorio**
```bash
git clone https://github.com/jcardonamde/kasumi.git
cd kasumi
```

#### 2. **Crear entorno virtual**
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

#### 3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

**Dependencias incluidas:**
- Django 5.0.14
- Pillow (para manejo de imágenes)
- Otros paquetes necesarios

#### 4. **Configurar base de datos**
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

#### 5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

**Datos solicitados:**
- Email (usado como username)
- Contraseña
- Confirmación de contraseña

#### 6. **Recolectar archivos estáticos (opcional en desarrollo)**
```bash
python manage.py collectstatic
```

#### 7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

#### 8. **Acceder a la aplicación**
- **Aplicación principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/
- **Login:** http://127.0.0.1:8000/accounts/login/

---

### **Panel de Administración Django**

1. Ir a: http://127.0.0.1:8000/admin/
2. Login con credenciales de superusuario
3. Gestionar:
   - Usuarios
   - Roles
   - Asignaciones de roles
   - Historial de acciones

## 📱 **Funcionalidades Implementadas**

### ✅ **Módulos Completados**

#### **Autenticación y Sesiones**
- [x] Sistema de login con Django Auth
- [x] Logout con confirmación
- [x] Cambio de contraseña
- [x] Protección de rutas con `@login_required`
- [x] Validación de permisos por rol
- [x] Sesiones seguras del lado del servidor

#### **Gestión de Usuarios**
- [x] CRUD completo de usuarios
- [x] Modelo de usuario personalizado
- [x] Lista con búsqueda y paginación
- [x] Vista de detalles completa
- [x] Perfil de usuario ("Mi Perfil")
- [x] Validación de formularios
- [x] Prevención de auto-eliminación

#### **Gestión de Roles y Permisos**
- [x] CRUD completo de roles
- [x] Asignación múltiple de roles
- [x] Permisos granulares configurables
- [x] Historial de asignaciones
- [x] Vista de usuarios por rol
- [x] Estados activo/inactivo

#### **Interfaz de Usuario**
- [x] Diseño responsive con Bootstrap 5
- [x] Navbar con menú desplegable
- [x] Breadcrumbs de navegación
- [x] Mensajes toast auto-removibles (7s)
- [x] Modales elegantes
- [x] Iconografía con Font Awesome
- [x] Animaciones CSS suaves

#### **Panel de Administración**
- [x] Django Admin configurado
- [x] Filtros y búsquedas avanzadas
- [x] Gestión visual de modelos
- [x] Historial de acciones (auditoría)
- [x] Fieldsets organizados

#### **Documentación**
- [x] README completo
- [x] Documentación de módulos
- [x] Guías de uso
- [x] Estructura del proyecto documentada

### 🔄 **En Desarrollo**
- [ ] Gestión de servicios
- [ ] Gestión de citas y agenda
- [ ] Gestión de clientes
- [ ] Reportes y estadísticas
- [ ] Dashboard con métricas
- [ ] API REST
- [ ] Notificaciones en tiempo real

### 🎯 **Próximas Funcionalidades**
- [ ] Módulo de servicios (spa, belleza, etc.)
- [ ] Calendario de citas
- [ ] Gestión de especialistas
- [ ] Sistema de reportes
- [ ] Exportación de datos (PDF, Excel)
- [ ] Notificaciones por email
- [ ] Logs de auditoría avanzados

## 🔒 **Seguridad**

### **Buenas Prácticas Implementadas**
- ✅ Contraseñas hasheadas con PBKDF2
- ✅ Protección CSRF en formularios
- ✅ Validación de permisos en vistas
- ✅ Sesiones seguras del lado del servidor
- ✅ SQL injection prevention (ORM de Django)
- ✅ XSS protection con escape automático de templates
- ✅ `.gitignore` configurado para archivos sensibles

### **Recomendaciones para Producción**
- [ ] Cambiar `SECRET_KEY` en producción
- [ ] Configurar `DEBUG = False`
- [ ] Usar base de datos PostgreSQL o MySQL
- [ ] Configurar HTTPS
- [ ] Implementar rate limiting
- [ ] Configurar ALLOWED_HOSTS
- [ ] Usar variables de entorno para configuración sensible

---

## 🧪 **Testing**

### **Comandos de Testing**
```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests de una app específica
python manage.py test accounts
python manage.py test gestion_usuarios

# Ejecutar con cobertura
coverage run --source='.' manage.py test
coverage report
```

### **Tests Implementados**
- [ ] Tests unitarios de modelos
- [ ] Tests de vistas
- [ ] Tests de formularios
- [ ] Tests de permisos
- [ ] Tests de integración

---

### **Documentación Externa**
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Font Awesome Icons](https://fontawesome.com/icons)

---

## 📞 **Contacto y Soporte**

### **Equipo de Desarrollo**
Para consultas sobre el proyecto, contactar a cualquier miembro del equipo.

---

<div align="center">

**© 2025 Kasumi - Sistema de Gestión**

**Desarrollado por D2JL Inc ®**

*Proyecto académico - SENA Ficha 2977435*

</div>
