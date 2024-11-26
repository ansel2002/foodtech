from django.shortcuts import render

# Mock data to simulate dynamic content (replace with actual database queries)
def home(request):
    return render(request, 'home.html')  # This remains unchanged if 'home.html' is static.

def dashboard(request):
    # Mock data for the dashboard
    activities = [
        {"name": "Tennis", "image_url": "tennis_image.jpg"},
        {"name": "Hiking", "image_url": "hiking_image.jpg"},
        {"name": "Running", "image_url": "running_image.jpg"},
        {"name": "Cycling", "image_url": "cycling_image.jpg"},
        {"name": "Yoga", "image_url": "yoga_image.jpg"},
    ]

    schedule = [
        {
            "date": "26",
            "weekday": "Monday",
            "activity": "Swimming",
            "participants": [{"image": "user1.jpg"}, {"image": "user2.jpg"}],
        },
        {
            "date": "27",
            "weekday": "Tuesday",
            "activity": "Yoga",
            "participants": [{"image": "user3.jpg"}],
        },
        {
            "date": "28",
            "weekday": "Wednesday",
            "activity": "Running",
            "participants": [{"image": "user4.jpg"}, {"image": "user5.jpg"}],
        },
    ]

    personal_bests = [
        {"name": "Longest Run", "value": "10 km", "image_url": "longest_run.jpg"},
        {"name": "Fastest Swim", "value": "2 min", "image_url": "fastest_swim.jpg"},
        {"name": "Most Calories Burned", "value": "500 cal", "image_url": "calories_burned.jpg"},
    ]

    user = {
        "name": "John Doe",
        "profile_picture": "profile_pic.jpg",
    }

    active_calories_percentage = 75  # Example percentage

    context = {
        "activities": activities,
        "schedule": schedule,
        "personal_bests": personal_bests,
        "user": user,
        "active_calories_percentage": active_calories_percentage,
    }

    return render(request, 'dashboard/base.html', context)



def profile(request):
    # Mock data for the profile page (replace with actual user profile data)
    user_profile = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "bio": "Food enthusiast and sustainability advocate.",
        "profile_picture": "profile_pic.jpg",  # Update with a real static or media path
    }

    context = {"user_profile": user_profile}
    return render(request, 'dashboard/profile.html', context)


def schedule(request):
    # Mock data for schedule activities (replace with real data)
    schedule_data = [
        {"date": "2024-11-27", "activity": "Visit recycling center"},
        {"date": "2024-11-28", "activity": "Community awareness program"},
        {"date": "2024-11-29", "activity": "Organize leftover food collection"},
    ]

    context = {"schedule_data": schedule_data}
    return render(request, 'dashboard/schedule.html', context)


def settings(request):
    # Mock settings options (replace with real settings data)
    settings_data = {
        "email_notifications": True,
        "sms_alerts": False,
        "account_privacy": "Public",
    }

    context = {"settings_data": settings_data}
    return render(request, 'dashboard/settings.html', context)


from .models import FoodWasteReport, FoodRecoveryEffort, UserProfile


def dashboard_view(request):
    user = request.user
    food_waste_reports = FoodWasteReport.objects.filter(user=user)
    food_recovery_efforts = FoodRecoveryEffort.objects.filter(user=user)
    active_engagement_percentage = (user.userprofile.total_food_donated / max(1, user.userprofile.total_food_wasted)) * 100
    
    context = {
        'user': user,
        'food_waste_reports': food_waste_reports,
        'food_recovery_efforts': food_recovery_efforts,
        'active_engagement_percentage': active_engagement_percentage,
        'page': 'home',
    }
    return render(request, 'dashboard.html', context)


def food_waste_reports(request):
    # Your logic for displaying the reports
    return render(request, 'food_waste_reports.html')
def food_recovery(request):
    # Logic for food recovery page
    return render(request, 'food_recovery.html')