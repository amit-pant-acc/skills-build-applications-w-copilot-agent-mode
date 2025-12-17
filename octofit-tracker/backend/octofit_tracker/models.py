from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField()
    calories = models.PositiveIntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.user.email}) on {self.date}"


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=200)
    exercises = models.JSONField(default=list)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.user.email}) on {self.date}"


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f"{self.user.email}: {self.score}"
