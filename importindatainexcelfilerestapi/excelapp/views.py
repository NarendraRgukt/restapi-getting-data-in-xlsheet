import xlwt
import io
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from excelapp import permissions,serializers
from rest_framework.generics import GenericAPIView

class UserRetrievingExcel(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsAdminUser]
    

    def get_serializer_class(self):
        return serializers.UserSerializerExcel
    def get(self,request):
        queryset=get_user_model().objects.all()
        serializer_class=self.get_serializer_class()
        serializer=serializer_class(queryset,many=True)
        #creatting a new workbook and worksheet
        workbook=xlwt.Workbook()
        worksheet=workbook.add_sheet('Data')


        # Write column headers
        headers = list(serializer.data[0].keys())
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        # Write data rows
        for row, data in enumerate(serializer.data, start=1):
            for col, value in enumerate(data.values()):
                worksheet.write(row, col, value)

        # Prepare the response
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)
        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename="data.xls"'
        response.write(output.getvalue())
        return response



class UserUploadingExcel(GenericAPIView):
    serializer_class=serializers.DataSerializer
    
    def post(self, request, *args, **kwargs):
        request_data = request.data

        # Creating the workbook
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('data')
        
        if not request_data:
            # If no data is provided, you may handle it as per your requirement.
            # For now, I'll just return an empty response.
            return HttpResponse(status=204)

        headers = list(request_data[0].keys())

        # Writing column values
        for column, header in enumerate(headers):
            worksheet.write(0, column, header)

        for row, data in enumerate(request_data, start=1):
            for col, value in enumerate(data.values()):
                worksheet.write(row, col, value)

        # Preparing the response
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)
        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename="data.xls"'
        response.write(output.getvalue())
        return response


        

            