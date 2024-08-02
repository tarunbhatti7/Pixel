from django.urls import path
from .views import Upload,Select_comps,Post_view_ist,Post_view_sec,Post_view_thir,Upload_view_ist,Upload_view_sec,Upload_view_thir,Show_view_ist,Show_view_sec,Show_view_thir,Post_view_four,Show_view_four

app_name = 'Base_App'
urlpatterns=[
    path('detail_ist/PRoWaDr!2udrAdis_ciwowLjafIpeXldrOtHIhAx/',Post_view_ist,name='detail_ist'),
    path('detail_ist/',Show_view_ist,name='show_ist'),
    path('upload_ist/',Upload_view_ist,name='upload_ist'),
    path('detail_sec/PRoWaDr!2udrAdis_ciwowLjafIpeXldrOtHIhAx/',Post_view_sec,name='detail_sec'),
    path('detail_sec/',Show_view_sec,name='show_sec'),
    path('upload_sec/',Upload_view_sec,name='upload_sec'),
    path('detail_thir/PRoWaDr!2udrAdis_ciwowLjafIpeXldrOtHIhAx/',Post_view_thir,name='detail_thir'),
    path('detail_thir/',Show_view_thir,name='show_thir'),
    path('detail_four/PRoWaDr!2udrAdis_ciwowLjafIpeXldrOtHIhAx/',Post_view_four,name='detail_thir'),
    path('detail_four/',Show_view_four,name='show_thir'),
    path('select_comps/',Select_comps,name='select_comps'),
    path('upload/',Upload,name='upload'),
    path('upload_thir/',Upload_view_thir,name='upload_thir'),
    path('upload_four/',Upload_view_thir,name='upload_four'),
]