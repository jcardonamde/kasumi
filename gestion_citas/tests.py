from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.messages import get_messages
from django.utils import timezone
from django.urls import reverse
from gestion_servicios.models import Servicio
from .models import Cita
from .views import CitaListView, CitaCreateView, CitaUpdateView, CitaDeleteView
from .forms import CitaForm

User = get_user_model()

class CitaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración inicial para las pruebas
        cls.cliente = User.objects.create_user(
            email='cliente@test.com',
            password='testpass123',
            first_name='Cliente',
            last_name='Test',
            tipo_documento='CC',
            numero_documento='12345678'
        )
        
        cls.especialista = User.objects.create_user(
            email='especialista@test.com',
            password='testpass123',
            first_name='Especialista',
            last_name='Test',
            tipo_documento='CC',
            numero_documento='87654321'
        )
        
        # Crear un servicio de prueba
        cls.servicio = Servicio.objects.create(
            nombre='Corte de pelo',
            descripcion='Corte de pelo básico',
            duracion_minutos=30,
            precio=25.00,
            estado='ACT'
        )
        
        # Crear una cita de prueba
        cls.cita = Cita.objects.create(
            cliente=cls.cliente,
            especialista=cls.especialista,
            servicio=cls.servicio,
            fecha_hora=timezone.now(),
            estado='PND',
            creado_por=cls.cliente
        )
    
    def test_creacion_cita(self):
        """Test para verificar la creación de una cita"""
        self.assertEqual(self.cita.cliente, self.cliente)
        self.assertEqual(self.cita.especialista, self.especialista)
        self.assertEqual(self.cita.servicio, self.servicio)
        self.assertEqual(self.cita.estado, 'PND')
        self.assertEqual(self.cita.creado_por, self.cliente)
    
    def test_estados_cita(self):
        """Test para verificar los estados de la cita"""
        # Cambiar el estado de la cita
        self.cita.estado = 'CFM'
        self.cita.save()
        self.assertEqual(self.cita.estado, 'CFM')
        
        # Verificar que el estado no es inválido
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            self.cita.estado = 'INVALIDO'
            self.cita.full_clean()
    
    def test_str_representation(self):
        """Test para verificar la representación en string del modelo"""
        expected_str = f"Cita {self.cita.id} - {self.cliente.get_full_name()}"
        self.assertEqual(str(self.cita), expected_str)
    
    def test_ordering(self):
        """Test para verificar el ordenamiento por fecha_hora"""
        # Crear una segunda cita con fecha posterior
        nueva_cita = Cita.objects.create(
            cliente=self.cliente,
            especialista=self.especialista,
            servicio=self.servicio,
            fecha_hora=timezone.now() + timezone.timedelta(days=1),
            estado='PND',
            creado_por=self.cliente
        )
        
        citas = list(Cita.objects.all())
        self.assertEqual(citas, [self.cita, nueva_cita])


class CitaViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración inicial para las pruebas
        cls.factory = RequestFactory()
        
        # Crear usuario administrador
        cls.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='adminpass123',
            first_name='Admin',
            last_name='Sistema',
            tipo_documento='CC',
            numero_documento='11223344'
        )
        
        # Crear cliente y especialista
        cls.cliente = get_user_model().objects.create_user(
            email='cliente@test.com',
            password='testpass123',
            first_name='Cliente',
            last_name='Test',
            tipo_documento='CC',
            numero_documento='12345678'
        )
        
        # Crear especialista como staff
        cls.especialista = get_user_model().objects.create_user(
            email='especialista@test.com',
            password='testpass123',
            first_name='Especialista',
            last_name='Test',
            tipo_documento='CC',
            numero_documento='87654321',
            is_staff=True  # Hacer que el especialista sea staff
        )
        
        # Crear un servicio de prueba
        cls.servicio = Servicio.objects.create(
            nombre='Corte de pelo',
            descripcion='Corte de pelo básico',
            duracion_minutos=30,
            precio=25.00,
            estado='ACT'
        )
        
        # Crear una cita de prueba
        cls.cita = Cita.objects.create(
            cliente=cls.cliente,
            especialista=cls.especialista,
            servicio=cls.servicio,
            fecha_hora=timezone.now(),
            estado='PND',
            creado_por=cls.admin_user
        )
    
    def setUp(self):
        # Iniciar sesión como administrador para las pruebas
        self.client.login(email='admin@test.com', password='adminpass123')
    
    def test_lista_citas_view(self):
        """Test para verificar la vista de lista de citas"""
        url = reverse('gestion_citas:lista_citas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_citas/lista_citas.html')
        self.assertContains(response, 'Citas')
    
    def test_crear_cita_view_get(self):
        """Test para verificar el formulario de creación de cita (GET)"""
        url = reverse('gestion_citas:crear_cita')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_citas/crear_cita.html')
        self.assertIsInstance(response.context['form'], CitaForm)
    
    def test_crear_cita_view_post(self):
        """Test para verificar la creación de una cita (POST)"""
        from django.utils import timezone
        from datetime import timedelta
        
        url = reverse('gestion_citas:crear_cita')
        fecha_hora = timezone.now() + timedelta(days=2)
        
        # Formatear la fecha y hora en el formato que espera el formulario datetime-local
        fecha_hora_str = fecha_hora.strftime('%Y-%m-%dT%H:%M')
        
        data = {
            'cliente': self.cliente.id,
            'especialista': self.especialista.id,
            'servicio': self.servicio.id,
            'fecha_hora': fecha_hora_str,  # Formato: 'YYYY-MM-DDTHH:MM'
            'estado': 'PND',
        }
        
        # Imprimir datos que se están enviando
        print("\nDatos de prueba para crear cita:", data)
        
        # Realizar la petición sin follow para ver la respuesta real
        response = self.client.post(url, data)
        
        # Imprimir la respuesta para depuración
        print("Respuesta del servidor:")
        print("Status code:", response.status_code)
        
        # Si hay un error en el formulario, mostrarlo
        if response.status_code == 200 and hasattr(response, 'context') and response.context is not None and 'form' in response.context:
            print("Errores del formulario:", response.context['form'].errors)
        
        # Verificar redirección después de crear la cita
        self.assertRedirects(response, reverse('gestion_citas:lista_citas'), 
                           msg_prefix=f"No se redirigió después de crear. Estado: {response.status_code}")
        
        # Verificar que se creó la cita
        self.assertEqual(Cita.objects.count(), 2, 
                        f"No se creó la cita. Estado de respuesta: {response.status_code}")
        
        # Verificar mensaje de éxito
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('creada exitosamente', str(messages[0]))
    
    def test_editar_cita_view_get(self):
        """Test para verificar el formulario de edición de cita (GET)"""
        url = reverse('gestion_citas:editar_cita', args=[self.cita.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_citas/editar_cita.html')
        self.assertIsInstance(response.context['form'], CitaForm)
    
    def test_editar_cita_view_post(self):
        """Test para verificar la actualización de una cita (POST)"""
        from django.utils import timezone
        from datetime import timedelta
        
        url = reverse('gestion_citas:editar_cita', args=[self.cita.id])
        nueva_fecha = timezone.now() + timedelta(days=3)
        
        # Formatear la fecha y hora en el formato que espera el formulario datetime-local
        fecha_hora_str = nueva_fecha.strftime('%Y-%m-%dT%H:%M')
        
        data = {
            'cliente': self.cliente.id,
            'especialista': self.especialista.id,
            'servicio': self.servicio.id,
            'fecha_hora': fecha_hora_str,  # Formato: 'YYYY-MM-DDTHH:MM'
            'estado': 'CFM',  # Cambiar estado a Confirmada
        }
        
        # Imprimir datos que se están enviando
        print("\nDatos de prueba para editar cita:", data)
        
        # Realizar la petición sin follow para ver la respuesta real
        response = self.client.post(url, data)
        
        # Imprimir la respuesta para depuración
        print("Respuesta del servidor:")
        print("Status code:", response.status_code)
        
        # Si hay un error en el formulario, mostrarlo
        if response.status_code == 200 and hasattr(response, 'context') and response.context is not None and 'form' in response.context:
            print("Errores del formulario:", response.context['form'].errors)
        
        # Verificar redirección después de actualizar
        self.assertRedirects(response, reverse('gestion_citas:lista_citas'),
                           msg_prefix=f"No se redirigió después de editar. Estado: {response.status_code}")
        
        # Verificar que la cita se actualizó
        self.cita.refresh_from_db()
        self.assertEqual(self.cita.estado, 'CFM', 
                        f"No se actualizó el estado de la cita. Estado actual: {self.cita.estado}")
        
        # Verificar mensaje de éxito
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('actualizada correctamente', str(messages[0]))
    
    def test_eliminar_cita_view(self):
        """Test para verificar la eliminación de una cita"""
        # Crear una cita para eliminar
        cita_a_eliminar = Cita.objects.create(
            cliente=self.cliente,
            especialista=self.especialista,
            servicio=self.servicio,
            fecha_hora=timezone.now() + timezone.timedelta(days=4),
            estado='PND',
            creado_por=self.admin_user
        )
        
        url = reverse('gestion_citas:eliminar_cita', args=[cita_a_eliminar.id])
        response = self.client.post(url, follow=True)
        
        # Verificar redirección después de eliminar
        self.assertRedirects(response, reverse('gestion_citas:lista_citas'))
        
        # Verificar que la cita fue eliminada
        with self.assertRaises(Cita.DoesNotExist):
            Cita.objects.get(id=cita_a_eliminar.id)
        
        # Verificar mensaje de éxito
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('eliminada exitosamente', str(messages[0]))
