# Instrucciones - Módulo de Gestión de Usuarios

## Cambios Implementados

### 1. Home Mejorado
- **Diseño moderno y atractivo** con tarjetas interactivas
- **Menú principal** con 6 módulos visibles:
  - Gestión de Roles
  - Gestión de Usuarios (✅ Funcional)
  - Gestión de Servicios (En desarrollo)
  - Gestión de Especialistas (En desarrollo)
  - Gestión de Agenda (En desarrollo)
  - Gestión de Clientes (En desarrollo)
- **Sección desplegable** con opciones adicionales:
  - Gestión de Citas
  - Reportes
  - Configuraciones

### 2. Módulo de Gestión de Usuarios - COMPLETAMENTE FUNCIONAL

#### Características Implementadas:
- ✅ **Listar usuarios** con búsqueda y paginación
- ✅ **Crear usuarios** con formulario completo
- ✅ **Editar usuarios** con todos los campos
- ✅ **Eliminar usuarios** con confirmación
- ✅ **Ver detalles** de usuario
- ✅ **Cambiar contraseña**
- ✅ **Asignar/Quitar roles**

#### Campos del Formulario de Usuario:
- Tipo de documento (TI, CC, CE, PAS)
- Número de documento
- Nombres
- Apellidos
- Teléfono
- Dirección
- Ciudad
- Fecha de nacimiento
- Email (usado para login)
- Contraseña
- Estado (Activo/Inactivo)
- Tipo de usuario (Administrador/Usuario)

### 3. Módulo de Gestión de Roles - COMPLETAMENTE FUNCIONAL

#### Características Implementadas:
- ✅ **Listar roles** con búsqueda
- ✅ **Crear roles** con permisos específicos
- ✅ **Editar roles**
- ✅ **Eliminar roles** (con validación de uso)
- ✅ **Asignar roles a usuarios**

### 4. Navegación Mejorada
- **Navbar con dropdown** que incluye todas las opciones del menú
- **Breadcrumbs** en todas las páginas para mejor navegación
- **Diseño responsive** que funciona en móviles y tablets

## Cómo Usar el Sistema

### Acceder al Sistema
1. Ejecutar el servidor: `python manage.py runserver`
2. Abrir navegador en: `http://localhost:8000`
3. Iniciar sesión con un usuario administrador

### Crear un Nuevo Usuario
1. Ir a **Inicio** > **Gestión de Usuarios**
2. Click en **"Nuevo Usuario"**
3. Llenar el formulario con todos los datos:
   - Seleccionar tipo de documento
   - Ingresar número de documento (único)
   - Nombres y apellidos
   - Datos de contacto (email, teléfono, dirección, ciudad)
   - Fecha de nacimiento (opcional)
   - Email (será el username para login)
   - Contraseña (mínimo 8 caracteres)
   - Marcar si es administrador
4. Click en **"Crear"**

### Editar un Usuario
1. En la lista de usuarios, click en el ícono de **editar** (lápiz)
2. Modificar los campos necesarios
3. Para cambiar la contraseña, llenar los campos de contraseña (dejar en blanco para no cambiar)
4. Click en **"Actualizar"**

### Asignar un Rol a un Usuario
1. Ir a los detalles del usuario
2. En la sección "Roles Asignados", click en **"Asignar Rol"**
3. Seleccionar el rol deseado
4. Click en **"Asignar Rol"**

### Crear un Nuevo Rol
1. Ir a **Inicio** > **Gestión de Roles**
2. Click en **"Nuevo Rol"**
3. Ingresar nombre y descripción
4. Seleccionar los permisos que tendrá el rol
5. Click en **"Crear"**

## Estructura de Archivos Creados/Modificados

### Formularios
- `gestion_usuarios/forms.py` - Agregado `UsuarioForm`

### Vistas
- `gestion_usuarios/views.py` - Agregadas:
  - `CrearUsuarioView`
  - `EditarUsuarioView`
  - `EliminarUsuarioView`

### URLs
- `gestion_usuarios/urls.py` - Agregadas rutas para crear, editar y eliminar usuarios

### Templates Creados
```
templates/gestion_usuarios/
├── usuarios/
│   ├── lista_usuarios.html
│   ├── form_usuario.html
│   ├── detalle_usuario.html
│   ├── eliminar_usuario.html
│   └── cambiar_contrasena.html
└── roles/
    ├── lista_roles.html
    ├── form_rol.html
    ├── eliminar_rol.html
    ├── asignar_rol.html
    └── quitar_rol.html
```

### Templates Modificados
- `templates/core/home.html` - Rediseñado completamente con nuevo menú
- `templates/base.html` - Agregado menú desplegable en navbar

## Base de Datos

Todos los datos se almacenan en `db.sqlite3`:
- Tabla `accounts_usuario` - Usuarios del sistema
- Tabla `gestion_usuarios_rol` - Roles
- Tabla `gestion_usuarios_usuariorol` - Relación usuarios-roles
- Tabla `gestion_usuarios_historialusuario` - Historial de acciones

## Validaciones Implementadas

### Formulario de Usuario:
- ✅ Email único (no puede haber dos usuarios con el mismo email)
- ✅ Número de documento único
- ✅ Contraseña mínimo 8 caracteres
- ✅ Confirmación de contraseña debe coincidir
- ✅ Email válido
- ✅ Campos requeridos marcados

### Seguridad:
- ✅ Solo administradores pueden gestionar usuarios
- ✅ Un usuario no puede eliminarse a sí mismo
- ✅ Las contraseñas se almacenan hasheadas
- ✅ Validación de permisos en todas las vistas

## Notas Técnicas

- Framework: Django 4.x
- Base de datos: SQLite3
- Frontend: Bootstrap 5.3.3
- Iconos: Font Awesome 6.4.0
- Autenticación: Django Auth con modelo de usuario personalizado
- Modelo de usuario: `accounts.Usuario` (usa email como username)
