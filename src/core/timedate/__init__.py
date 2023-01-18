from datetime import datetime, timezone

class TimeDate:
    def __init__(self):
        pass

    def getTime(self,format):
        if format == "UTC":
            now = datetime.now(timezone.utc)
            currentTime = now.strftime("%H:%M")

            return currentTime
        elif format == "local":
            now = datetime.now()
            currentTime = now.strftime("%H:%M")

            return currentTime

    def getDay(self,format):
        if format == "UTC":
            now = datetime.now(timezone.utc)
            currentDay = now.strftime("%a")

            return currentDay
        elif format == "local":
            now = datetime.now()
            currentDay = now.strftime("%a")

            return currentDay

        return day
        

