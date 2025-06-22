INDEX_HTML_CONTENT = """
{% load static %}
<!doctype html>
<html lang="en" xml:lang="en">
    <head>
        <title>Home</title>
    </head>
    
    <body>
        <div id="root">
        <script defer="defer" type="text/javascript" src="{% static 'index-bundle.js' %}"></script>
    </body>
</html>
"""

HOME_HTML_CONTENT = """
{% load static %}
<!doctype html>
<html lang="en" xml:lang="en">
    <head>
        <title>Home</title>
    </head>
    
    <body>
        <div id="root">
        <script type="text/javascript" src="{% static 'index-bundle.js' %}"></script>
    </body>
</html>
"""
