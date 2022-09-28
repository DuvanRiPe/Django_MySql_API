from django.http.response import JsonResponse
from django.views import View
from .models import Company

#en las vistas podemos trabajar con funciones y con clases en ste caso usaremos clases
 
class CompanyView(View):

    def get(self, request):
        #con companies=Company.objects.all()obtengo los datos de mi tabla, estos estan en el modelo Company, sin embargo django no serializa esto a un json asi que hay que hacerlo de la siguiente manera:
        companies= list(Company.objects.values())
        #creo una condicional que me diga si devielve un valor diferente de 0 que sala un mensaje de succes y me guasrde la informacion en la variable datos y si no pues sale un mensaje de no encontrado.
        if len(companies)>0:
            datos={"message":"Success","companies":companies}
        else:
            datos={"message":"Companies not found..."}
        #como trabajaremos con una api lo que deve devolver es un archivo json y para eso usamos JsonResponse(datos) donde datos es la variable que me esta guardadon el mesnjae con la informacion de mi tabla
        return JsonResponse(datos)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass
