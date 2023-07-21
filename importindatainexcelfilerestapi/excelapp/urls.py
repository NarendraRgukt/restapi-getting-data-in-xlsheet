from django.urls import path
from excelapp import views
app_name="excelapp"
urlpatterns = [
    path('excel/import/',views.UserRetrievingExcel.as_view(),name="excel_download"),
    path('excel/export/',views.UserUploadingExcel.as_view(),name="upload")
]
