from datetime import datetime
import pytz

# Get the hour of Bogota
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
# Print with format dd/mm/YYYY HH:MM:SS
print("Bogota: ",bogota_date.strftime("%d/%m/%Y %H:%M:%S"))


# Get the hour of Bogota
mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
# Print with format dd/mm/YYYY HH:MM:SS
print("Mexico city: ",mexico_date.strftime("%d/%m/%Y %H:%M:%S"))


# Get the hour of Bogota
caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
# Print with format dd/mm/YYYY HH:MM:SS
print("Caracas: ",caracas_date.strftime("%d/%m/%Y %H:%M:%S"))
