from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('select_all/', select_all),
    path('select_few_columns/', select_few_columns),
    path('select_all_p/', select_all_p),
    path('select_few_columns_p/', select_few_columns_p),
    path('select_old_price_and_new_price_p/', select_old_price_and_new_price_p),
    path('select_old_price_and_new_price/', select_old_price_and_new_price),
    path('select_report_with_comment_p/', select_report_with_comment_p),
    path('select_distinct_p/', select_distinct_p),
    path('select_distinct_p_list/', select_distinct_p_list),
    path('select_distinct_p_list/', select_distinct_p_list),
    path('alias_sql_alias_p/', alias_sql_alias_p),
    path('reporting_with_Concatenation_p/', reporting_with_Concatenation_p),
    path('reporting_with_concatenation_customer_location_p/', reporting_with_concatenation_customer_location_p),
    path('reporting_with_concatenation_customer_location_New_p/', reporting_with_concatenation_customer_location_New_p),
    path('reporting_with_Concatenation_p/',reporting_with_Concatenation_p),
    path('report_formatting_without_concatention_p/',report_formatting_without_concatention_p),
    path('report_formatting_add_two_coloumn_in_one_coloumn_p/',report_formatting_add_two_coloumn_in_one_coloumn_p),
    path('round_amount_one_decimal/',round_amount_one_decimal),
    path('round_amounformattiong_53/',round_amounformattiong_53),
    path('order_by_company_name/',order_by_company_name),
    path('order_by_customer_id_asc_order_id_desc/',order_by_customer_id_asc_order_id_desc),
    path('order_by_customer_id_asc_order_id_asc/',order_by_customer_id_asc_order_id_asc),
    path('where_sales_manager_details/',where_sales_manager_details),
    path('where_owner_details/',where_owner_details),
    path('where_specific_order_id/',where_specific_order_id),
    path('where_searching_product/',where_searching_product),
    path('where_searching_for_customer_id/',where_searching_for_customer_id),
    path('where_product_above/',where_product_above),
    path('where_product_less/',where_product_less),
    path('where_product_whose_price_are_40_above/',where_product_whose_price_are_40_above),
    path('where_product_whose_price_are_40_above/',where_product_whose_price_are_40_above),
    path('where_product_with_range/',where_product_with_range),
    path('where_product_rostocking/',where_product_rostocking),
    path('order_amount_of_10540_or_above/',order_amount_of_10540_or_above),
    path('where_not_mr/',where_not_mr),
    path(' where_not_sales_representative/', where_not_sales_representative),
    path('where_price_between_two_figure/', where_price_between_two_figure),
    path('where_price_not_between_two_figure/', where_price_not_between_two_figure),
    path('where_two_between/',where_two_between),

]
