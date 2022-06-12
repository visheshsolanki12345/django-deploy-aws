from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
# Create your views here.

@api_view(["GET"])
def get_data(request):
    obj = Student.objects.all()
    serializer = StudentSerializer(obj, many=True)
    context = {"data": serializer.data, "status": 200}
    return Response(context)

