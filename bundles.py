from djanjinja.loader import Bundle

from templatetags.static_asset import static_asset as sm_static_asset
from templatetags.static_combo import static_combo_css as sm_static_combo_css
from templatetags.static_combo import static_combo_js as sm_static_combo_js

static_management = Bundle()

@static_management.ctxfunction
def static_asset(ctx, file_name):
    """djanjinja bundle wrapper for static_asset template tag"""
    return sm_static_asset(file_name)
   
@static_management.ctxfunction
def static_combo_css(ctx, file_name, media=None):
    return sm_static_combo_css(file_name, media=None)
    
@static_management.ctxfunction
def static_combo_js(ctx, file_name):
    return sm_static_combo_js(file_name)