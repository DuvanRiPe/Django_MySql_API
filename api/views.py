from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json

#en las vistas podemos trabajar con funciones y con clases en ste caso usaremos clases
 
class CompanyView(View):

    # este metodo solo se ejecuta cuando realizamos una peticion, csrf es como falcificacion de una petifcion y django toma  esta medida de seguiradad.
    @method_decorator(csrf_exempt)#para decir que la peticion es correcta y no falsa
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get(self, request, id=0):
        if id > 0:
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]
                datos={"message":"Success","companies":company}
            else:
                datos={"message":"Companies not found..."}
            return JsonResponse(datos)
        else:
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
        jd=json.loads(request.body)
        Company.objects.create(name=jd['name'],website=jd['website'], foundation=jd['foundation'])
        datos={"message":"Success"}
        return JsonResponse(datos)
    def put(self, request, id):
        jd=json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company= Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            datos={"message":"Success"}
        else:
            datos={"message":"Companies not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos={"message":"Success"}
        else:
            datos={"message":"Companies not found..."}
        return JsonResponse(datos)
