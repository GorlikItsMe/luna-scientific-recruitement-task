from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import HydroponicSystem, Measurement
from django.utils import timezone


class TestHydroponicSystemViewSet(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='user', password='passwd')
        self.client = APIClient()
        self.client.login(username='user', password='passwd')

        self.user2 = User.objects.create_user(username='user2', password='passwd2')
        self.client2 = APIClient()
        self.client2.login(username='user2', password='passwd2')

    def tearDown(self) -> None:
        Measurement.objects.all().delete()
        HydroponicSystem.objects.all().delete()

    def test_create_hydroponic_system(self):
        r = self.client.post('/api/v1/hydroponicsystem/', {
            'name': 'Test System',
            'description': 'Test Description'
        })
        self.assertEqual(r.status_code, 201)
        data = r.data
        self.assertEqual(data['name'], 'Test System')
        self.assertEqual(data['description'], 'Test Description')

    def test_list_hydroponic_systems(self):
        r = self.client.get('/api/v1/hydroponicsystem/')
        self.assertEqual(r.status_code, 200)
        data = r.data['results']
        self.assertEqual(len(data), 0)

        self.client.post('/api/v1/hydroponicsystem/', {
            'name': 'Test System',
            'description': 'Test Description'
        })

        r = self.client.get('/api/v1/hydroponicsystem/')
        data = r.data['results']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test System')
        self.assertEqual(data[0]['description'], 'Test Description')

    def test_list_hydroponic_systems_unauthenticated(self):
        self.client.logout()
        r = self.client.get('/api/v1/hydroponicsystem/')
        self.assertEqual(r.status_code, 401)

    def test_can_see_only_own_systems(self):
        self.client.post('/api/v1/hydroponicsystem/', {
            'name': 'Test System',
            'description': 'Test Description'
        })

        self.client2.post('/api/v1/hydroponicsystem/', {
            'name': 'Test System 2',
            'description': 'Test Description 2'
        })

        r = self.client.get('/api/v1/hydroponicsystem/')
        data = r.data['results']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test System')

        r = self.client2.get('/api/v1/hydroponicsystem/')
        data = r.data['results']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test System 2')

    def test_last_10_measurements(self):
        system = HydroponicSystem.objects.create(
            name='Test System',
            description='Test Description',
            owner=self.user
        )
        now = timezone.now()
        for n in range(25):
            dt = now - timezone.timedelta(minutes=1)
            Measurement.objects.create(
                hydroponic_system=system,
                ph=float(n),
                water_temp=25.0,
                tds=1000.0,
                created_at=dt
            )

        r = self.client.get(f'/api/v1/hydroponicsystem/{system.id}/')
        data = r.data
        self.assertEqual(len(data['last_10_measurements']), 10)
        # check ordering
        self.assertEqual(data['last_10_measurements'][0]['ph'], 24.0)

    def test_create_mesurements(self):
        system = HydroponicSystem.objects.create(
            name='Test System',
            description='Test Description',
            owner=self.user
        )
        r = self.client.post('/api/v1/measurement/', {
            'hydroponic_system': system.id,
            'ph': 5.0,
            'water_temp': 25.0,
            'tds': 1000.0
        })
        self.assertEqual(r.status_code, 201)
        data = r.data
        self.assertEqual(data['ph'], 5.0)
        self.assertEqual(data['water_temp'], 25.0)
        self.assertEqual(data['tds'], 1000.0)

    def test_cant_add_measurement_to_not_owned_system(self):
        system = HydroponicSystem.objects.create(
            name='Test System',
            description='Test Description',
            owner=self.user2
        )
        r = self.client.post('/api/v1/measurement/', {
            'hydroponic_system': system.id,
            'ph': 5.0,
            'water_temp': 25.0,
            'tds': 1000.0
        })
        self.assertEqual(r.status_code, 400)

    def test_can_see_only_own_measurements(self):
        system = HydroponicSystem.objects.create(
            name='Test System',
            description='Test Description',
            owner=self.user
        )
        Measurement.objects.create(
            hydroponic_system=system,
            ph=5.0,
            water_temp=25.0,
            tds=1000.0
        )

        system2 = HydroponicSystem.objects.create(
            name='Test System 2',
            description='Test Description 2',
            owner=self.user2
        )
        Measurement.objects.create(
            hydroponic_system=system2,
            ph=5.0,
            water_temp=25.0,
            tds=1000.0
        )

        r = self.client.get('/api/v1/measurement/')
        data = r.data['results']
        self.assertEqual(len(data), 1)

        r = self.client2.get('/api/v1/measurement/')
        data = r.data['results']
        self.assertEqual(len(data), 1)
