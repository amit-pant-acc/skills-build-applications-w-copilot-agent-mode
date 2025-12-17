from rest_framework import routers
from .views import (
    TeamViewSet,
    UserViewSet,
    ActivityViewSet,
    WorkoutViewSet,
    LeaderboardEntryViewSet,
)

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)

urlpatterns = router.urls
