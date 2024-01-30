# Fluent Python ex.2-4
# Cartesian product using list comprehension
from keyword import kwlist

DOMAINS = ["dev", "io"]

# Build list of Python keywords with each suffix in DOMAINS list:
site_domains = [f"{kw}.{domain}" for kw in kwlist for domain in DOMAINS]

print(site_domains)
