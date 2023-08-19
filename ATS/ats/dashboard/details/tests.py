from django.test import TestCase
from .models import caditate_signup, Candidate, Cse, Civil, Mechanical, Eee, Ece, UploadedFile, profiles

class ModelTestCase(TestCase):
    def test_caditate_signup_model(self):
        caditate = caditate_signup.objects.create(
            firstname='John',
            lastname='Doe',
            username='johndoe',
            password='password123'
        )
        self.assertEqual(caditate.firstname, 'John')
        self.assertEqual(caditate.lastname, 'Doe')
        self.assertEqual(caditate.username, 'johndoe')
        self.assertEqual(caditate.password, 'password123')

    def test_candidate_model(self):
        candidate = Candidate.objects.create(
            first_name='John',
            last_name='Doe',
            branch='CSE',
            skills='Python, Django',
            jr_number='JR123',
            phone_number='1234567890',
            email_address='john@example.com',
            current_company='ABC Corp',
            total_experience=2.5,
            ctc=500000,
            expected_ctc=600000,
            offers_in_hand=1,
            notice_period=30,
            current_location='New York',
            source='Referral',
            screening_status='Passed',
            screened_by='Jane'
        )
        self.assertEqual(candidate.first_name, 'John')
        self.assertEqual(candidate.last_name, 'Doe')
        self.assertEqual(candidate.branch, 'CSE')
        self.assertEqual(candidate.skills, 'Python, Django')
        # ... continue checking other fields

    def test_cse_model(self):
        cse = Cse.objects.create(
            first_name='Jane',
            last_name='Smith',
            branch='CSE',
            skills='JavaScript, HTML, CSS',
            jr_number='JR456',
            phone_number='9876543210',
            email_address='jane@example.com',
            current_company='XYZ Corp',
            total_experience=3.5,
            ctc=600000,
            expected_ctc=700000,
            offers_in_hand=2,
            notice_period=45,
            current_location='San Francisco',
            source='Job Board',
            screening_status='Pending',
            screened_by='John'
        )
        self.assertEqual(cse.first_name, 'Jane')
        self.assertEqual(cse.last_name, 'Smith')
        self.assertEqual(cse.branch, 'CSE')
        self.assertEqual(cse.skills, 'JavaScript, HTML, CSS')
        # ... continue checking other fields

    # Write similar test methods for other models

class ProfileModelTestCase(TestCase):
    def test_profiles_model(self):
        profile = profiles.objects.create(
            firstname='John',
            lastname='Doe',
            username='johndoe',
            password='password123'
        )
        self.assertEqual(profile.firstname, 'John')
        self.assertEqual(profile.lastname, 'Doe')
        self.assertEqual(profile.username, 'johndoe')
        self.assertEqual(profile.password, 'password123')

    # Write similar test methods for other models

class FileModelTestCase(TestCase):
    def test_uploaded_file_model(self):
        # Assuming you have a file named 'test_file.txt' in your test directory
        test_file_path = 'path/to/test_file.txt'
        uploaded_file = UploadedFile.objects.create(file=test_file_path)
        self.assertEqual(uploaded_file.get_file_url(), '/media/uploads/test_file.txt')

    # Write similar test methods for other models

class ModelTestCase(TestCase):
    def test_caditate_signup_model(self):
        caditate = caditate_signup.objects.create(
            firstname='John',
            lastname='Doe',
            username='johndoe',
            password='password123'
        )
        self.assertEqual(caditate.firstname, 'John')
        self.assertEqual(caditate.lastname, 'Doe')
        self.assertEqual(caditate.username, 'johndoe')
        self.assertEqual(caditate.password, 'password123')

    def test_candidate_model(self):
        candidate = Candidate.objects.create(
            first_name='John',
            last_name='Doe',
            branch='CSE',
            skills='Python, Django',
            jr_number='JR123',
            phone_number='1234567890',
            email_address='john@example.com',
            current_company='ABC Corp',
            total_experience=2.5,
            ctc=500000,
            expected_ctc=600000,
            offers_in_hand=1,
            notice_period=30,
            current_location='New York',
            source='Referral',
            screening_status='Passed',
            screened_by='Jane'
        )
        self.assertEqual(candidate.first_name, 'John')
        self.assertEqual(candidate.last_name, 'Doe')
        self.assertEqual(candidate.branch, 'CSE')
        self.assertEqual(candidate.skills, 'Python, Django')
        # ... continue checking other fields

    def test_cse_model(self):
        cse = Cse.objects.create(
            first_name='Jane',
            last_name='Smith',
            branch='CSE',
            skills='JavaScript, HTML, CSS',
            jr_number='JR456',
            phone_number='9876543210',
            email_address='jane@example.com',
            current_company='XYZ Corp',
            total_experience=3.5,
            ctc=600000,
            expected_ctc=700000,
            offers_in_hand=2,
            notice_period=45,
            current_location='San Francisco',
            source='Job Board',
            screening_status='Pending',
            screened_by='John'
        )
        self.assertEqual(cse.first_name, 'Jane')
        self.assertEqual(cse.last_name, 'Smith')
        self.assertEqual(cse.branch, 'CSE')
        self.assertEqual(cse.skills, 'JavaScript, HTML, CSS')
        # ... continue checking other fields

    def test_civil_model(self):
        civil = Civil.objects.create(
            first_name='Emily',
            last_name='Johnson',
            branch='Civil',
            skills='AutoCAD, Structural Engineering',
            jr_number='JR789',
            phone_number='9876543210',
            email_address='emily@example.com',
            current_company='PQR Corp',
            total_experience=4.5,
            ctc=800000,
            expected_ctc=900000,
            offers_in_hand=0,
            notice_period=60,
            current_location='Chicago',
            source='LinkedIn',
            screening_status='Rejected',
            screened_by='Jessica'
        )
        self.assertEqual(civil.first_name, 'Emily')
        self.assertEqual(civil.last_name, 'Johnson')
        self.assertEqual(civil.branch, 'Civil')
        self.assertEqual(civil.skills, 'AutoCAD, Structural Engineering')
        # ... continue checking other fields

    # Write similar test methods for other models

class ProfileModelTestCase(TestCase):
    def test_profiles_model(self):
        profile = profiles.objects.create(
            firstname='John',
            lastname='Doe',
            username='johndoe',
            password='password123'
        )
        self.assertEqual(profile.firstname, 'John')
        self.assertEqual(profile.lastname, 'Doe')
        self.assertEqual(profile.username, 'johndoe')
        self.assertEqual(profile.password, 'password123')

    # Write similar test methods for other models

class FileModelTestCase(TestCase):
    def test_uploaded_file_model(self):
        # Assuming you have a file named 'test_file.txt' in your test directory
        test_file_path = 'path/to/test_file.txt'
        uploaded_file = UploadedFile.objects.create(file=test_file_path)
        self.assertEqual(uploaded_file.get_file_url(), '/media/uploads/test_file.txt')

    # Write similar test methods for other models
