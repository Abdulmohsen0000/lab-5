{% extends 'tax_app/base.html' %}

{% block title %}Tax Rate - Tax Calculator{% endblock %}

{% block content %}
<div class="card">
    <p style="color: #888; letter-spacing: 2px; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 20px;">
        Current Tax Rate
    </p>
    <h1 style="font-size: 5rem; color: #1a1a2e; font-weight: bold; letter-spacing: -2px;">
        {{ tax_rate_percent }}%
    </h1>
    <p style="color: #aaa; margin-top: 20px; font-size: 0.95rem;">
        Applied to all price calculations on this site.
    </p>
</div>
{% endblock %}
