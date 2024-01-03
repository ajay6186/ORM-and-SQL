from django.contrib import admin
from django.urls import path
from sql.views import *
urlpatterns = [
    path('select_all/', select_all),
    path('select_all_p/', select_all_p),
    path('select_few_columns_p/', select_few_columns_p),
    path('select_few_columns/', select_few_columns),
    path('select_old_price_and_new_price/', select_old_price_and_new_price),
    path('select_report_with_comment/', select_report_with_comment),
    path('select_distinct/', select_distinct),
    path('alias_sql_alias/', alias_sql_alias),
    path('alias_sql_alias_comprihention/', alias_sql_alias_comprihention),
    path('reporting_with_concatenation/', reporting_with_concatenation),
]
