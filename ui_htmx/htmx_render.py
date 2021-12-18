from django.template import Template, RequestContext

def htmx_render_page(request, template, context, rendered_overlay=""):

    if "HTTP_HX_REQUEST" not in request.META:
        wrapper = f"""{{% extends "ui_htmx/wrapper.html" %}}"""
    else:
        wrapper = f"""{{% extends "ui_htmx/wrapper_in_body.html" %}}"""

    return Template(f"""
        {wrapper}
        {{% block page %}}
            {{% include "{template}" %}}
        {{% endblock %}}
        {{% block overlay %}}
        {rendered_overlay}
        {{% endblock %}}
        """).render(RequestContext(request, context))


def htmx_render_overlay(request, template, context):
    return Template(f"""{{% include "{template}" %}}""").render(RequestContext(request, context))
