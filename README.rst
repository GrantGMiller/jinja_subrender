Jinja Tools
===========

A tool to help you logically separate how things are rendered in your project.
For example, you may want to have smaller templates rendered within larger templates.

Register the Blueprint
======================
To enable the features of the package, you must register the flask blueprint.

::

    from flask import Flask
    import jinja_subrender

    app = Flask()
    app.register_blueprint(jinja_subrender.bp)

Sub-Render Example
==================

You may have a jinja-template that displays a collection of items, called 'all_items.jinja'.
You may also have a jinja-templte for how each item should be rendered, called 'item.jinja'.

In this case your 'all_items.jinja' template could look something like:

::

    {% extends "main.jinja" %}

    {% block content %}

    {% for item in items %}
        <div>
            {{ item | Render('item.jinja') }}
        </div>
    {% endfor %}

    {% endblock %}

The 'item.jinja' template could look something like:

::

    <div>
        {{ obj['name'] }}
        <img src="{{ obj['src'] }}"/>
    </div>

Note: Render() always passes the item as 'obj', but you can rename within the jinja template, like so:

::

    {% set item = obj %}
    <div>
        {{ item['name'] }}
        <img src="{{ item['src'] }}"/>
    </div>

Passing multiple arguments
==========================

You can also pass multiple arguments by passing them as a tuple in the super-template.
For example, 'all_items.jinja' could look like:

::

    {% set total = items | length %}
    {% for item in items %}
        <div>
            {{ (item, total) | Render('item.jinja') }}
        </div>
    {% endfor %}

You can then access the second argument in the sub-template by breaking it apart with 'set'

::

    {% set item, total = obj %}
    <div>
        {{ item['name'] }}
        <img src="{{ item['src'] }}"/>
        total = {{ total }}
    </div>