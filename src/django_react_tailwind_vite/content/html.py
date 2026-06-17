HOME_HTML_CONTENT = """
{% load django_vite %}
{% load static %}
<!doctype html>
<html lang="en" xml:lang="en">
    <head>
        {% vite_hmr_client %}
        {% vite_asset 'frontend/index.tsx' %}
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Home</title>
    </head>
    <body>
        <div id="root">
    </body>
</html>
"""
