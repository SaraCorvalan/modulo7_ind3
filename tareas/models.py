from django.db import models
from django.utils import timezone

categorias = (
    ("1", "Trabajo"),
    ("2", "Hogar"),
    ("3", "Estudio"),
    ("4", "Otras categorías"),
)

estados = (
    ("1", "Pendiente"),
    ("2", "En progreso"),
    ("3", "Completada"),
)

class registroTareas(models.Model):
    id_tarea = models.CharField(
        null= False,
        max_length = 3,
        primary_key = True,
        default = '100'
        )               
    titulo_tarea = models.CharField(max_length=50, verbose_name="Título de tarea")
    descripcion_tarea = models.CharField(max_length=150, verbose_name="Descripción de tarea")    
    fecha_vencimiento_tarea = models.DateField(default=timezone.now, verbose_name="Fecha vencimiento tarea (dd-mm-yyyy)")
    categoria_tarea = models.CharField(max_length=1, choices=categorias, default='1', verbose_name="Categoria tarea") 
    estado_tarea = models.CharField(max_length=1, choices=estados, default='1', verbose_name="Estado de tarea")

            
    def __str__(self):
        return "Id: %s, Nombre Tarea: %s, Descripción tarea: %s,  Vencimiento tarea: %s, Categoria: %s, Estado: %s" %(
            self.id_tarea, 
            self.titulo_tarea, 
            self.descripcion_tarea, 
            self.fecha_vencimiento_tarea, 
            self.categoria_tarea, 
            self.estado_tarea)
    


