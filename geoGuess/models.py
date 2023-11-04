from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Link to the user who created the challenge
    image = models.ImageField(upload_to='challenges/')          # Store the uploaded image
    longitude = models.FloatField()                             # Store the answer coordinates
    latitude = models.FloatField()                              # Store the answer coordinates
    timestamp = models.DateTimeField(auto_now_add=True)         # Automatically set when the challenge is created
    approve_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Challenge {self.pk} by {self.user.username}"

    class Meta:
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

class DailyChallenge(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)  # Links to the challenge
    timestamp = models.DateTimeField(auto_now_add=True)                 # Automatically set when the daily challenge is created 
    def __str__(self):
        return f"Daily Challenge {self.pk} from {self.timestamp}"

class Guess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)                              # Store the score / 1000         
    distanceFromAnswer = models.FloatField(default=0)                   # Store in meters
    longitude = models.FloatField(default=0)                            # Store the guessed coordinates
    latitude = models.FloatField(default=0)                             # Store the  coordinates

    def __str__(self):
        return f"Guess {self.pk} by {self.user.username}"
    
