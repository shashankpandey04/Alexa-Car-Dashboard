import os

css_overrides = """
/* Custom Jaipur Luxury Aesthetic Overrides */
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
    color: #2B1B0E !important;
    background-color: #F5E6C8;
}

h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6, .navbar-brand {
    font-family: 'Cinzel', serif !important;
    font-weight: 600 !important;
    letter-spacing: 1px;
}

h1 { font-weight: 700 !important; }

.btn-primary {
    background: #C89B3C !important;
    border-color: #C89B3C !important;
    color: #fff !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 10px rgba(200, 155, 60, 0.3);
}

.btn-primary:hover {
    background: #b38830 !important;
    border-color: #b38830 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(200, 155, 60, 0.4);
}

.car-wrap {
    box-shadow: 0 10px 30px -5px rgba(43, 27, 14, 0.15);
    border-radius: 12px !important;
    overflow: hidden;
    transition: all 0.3s ease;
    background-color: #fff;
    border: 1px solid rgba(200, 155, 60, 0.2);
}

.car-wrap:hover {
    box-shadow: 0 15px 40px -5px rgba(43, 27, 14, 0.25);
    transform: translateY(-5px);
}

.navbar-brand span {
    color: #C89B3C !important;
}

.ftco-section {
    background-color: #F5E6C8 !important;
}

.bg-light {
    background-color: #F5E6C8 !important;
}
"""

with open('static/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_overrides)

print("CSS Overrides appended to style.css")
