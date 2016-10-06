from django.contrib import admin
from django.contrib.admin.sites import AdminSite


AdminSite.site_header = "Certificado Digital Vale"
AdminSite.site_title = "Certificado Digital Vale"

admin.site.disable_action('delete_selected')
