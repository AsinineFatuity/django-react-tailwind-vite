HOME_HTML_CONTENT = """
{% load static %}
<!doctype html>
<html lang="en" xml:lang="en">
    <head>
        {% vite_hmr_client %}
        {% vite_asset 'frontend/index.tsx' %}
        <title>Home</title>
    </head>
    
    <body>
        <div id="root">
    </body>
</html>
"""
