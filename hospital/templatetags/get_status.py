from django import template

register = template.Library()


def get_statu(h_status):
    if h_status == '已结算':
        return False
    else:
        return True

register.filter('get_statu', get_statu)








