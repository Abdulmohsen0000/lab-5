{% extends 'tax_app/base.html' %}

{% block title %}Tax Result - Tax Calculator{% endblock %}

{% block content %}
<div class="card">
    <h2 style="font-size: 1.4rem; letter-spacing: 2px; text-transform: uppercase; color: #888; margin-bottom: 40px;">
        Tax Calculation Result
    </h2>

    <div style="display: grid; gap: 20px; text-align: left; margin-bottom: 40px;">
        <div style="display: flex; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid #eee;">
            <span style="color: #555;">Original Price</span>
            <strong style="font-size: 1.1rem;">${{ price }}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid #eee;">
            <span style="color: #555;">Tax ({{ tax_rate_percent }}%)</span>
            <strong style="font-size: 1.1rem; color: #c0392b;">+${{ tax_amount }}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 20px; background: #1a1a2e; color: white; border-radius: 2px;">
            <span style="font-size: 1.1rem; letter-spacing: 1px;">TOTAL PRICE</span>
            <strong style="font-size: 1.4rem;">${{ total_price }}</strong>
        </div>
    </div>

    <a href="/" style="color: #1a1a2e; text-decoration: none; font-size: 0.9rem; letter-spacing: 1px; border-bottom: 1px solid #1a1a2e; padding-bottom: 2px;">
        &larr; Back to Home
    </a>
</div>
{% endblock %}
