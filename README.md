# EventAPI
Event management API using Django Rest Framework with role-based access, event creation, and ticket purchasing functionality.

**Step 1: Set Up the Django Project**

  **1. Install Required Packages:**
  
        After cloning project move to EventAPI
        cd EventAPI
        
        Install required packages
        pip install -r requirements.txt

**2. Setup database credentials:**

       Inside EventAPI in settings.py file change database credentials
        
        # settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'eventapi_db',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
**3. Migrate Database: Run migrations to set up the database:**

        python manage.py migrate

**4. Run the Server:**
 
    python manage.py runserver

**5. Test with Postman or Curl**

1. Register User: POST /api/register/

2. Create Event (Admin only): POST /api/events/

3. View Events: GET /api/events/

4. Purchase Tickets: POST /api/events/{event_id}/purchase/

**6. SQL Query**
  
   - In models.py file get_top_events is raw sql query to fetch top 3 events by tickets sold
