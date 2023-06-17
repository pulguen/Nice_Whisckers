from django.db import models

# Create your models here.
class Barberia(models.Model):
    #is_active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    horario = models.CharField(max_length=255, null=True, blank=True)
    #lat = models.FloatField()
    #lon = models.FloatField()

    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return f"Barberia: {self.nombre}"
    
    def establecer_horario_corrido(self, dia, horario):
        self.barberia_horario[dia] = horario
        print(f"Se ha establecido el horario corrido para el día {dia}.")

    def establecer_horario_cortado(self, dia, intervalo1, intervalo2):
        self.barberia_horario[dia] = [intervalo1, intervalo2]
        print(f"Se ha establecido el horario cortado para el día {dia}.")
        
    def establecer_horariocerrado(self, dia):
        self.barberia_horario[dia] = "cerrado"
        print(f"Se ha establecido que estada cerradodía {dia}.")

    def obtener_horario(self):
        if len(self.horario) == 0:
            return "El horario no ha sido configurado."
        horarios = ""
        for dia, intervalos in self.barberia_horario.items():
            horarios += f"Día {dia}: "
            if intervalos == "corrido":
                horarios += "Horario corrido\n"
            if intervalos == "cortado":
                horarios += f"{intervalos[0]} - {intervalos[1]}\n"
            else:
                horario += f"Cerrado"
        return horarios


    # Barberia.establecer_horario_corrido("09:00 - 18:00")
    # print(mi_barberia.obtener_horario())

    # mi_barberia.establecer_horario_cortado("09:00 - 13:00", "15:00 - 19:00")
    # print(mi_barberia.obtener_horario())  