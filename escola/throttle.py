from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = "3/day"