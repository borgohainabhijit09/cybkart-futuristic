import os
import glob
import re

html_files = glob.glob("*.html")

seo_data = {
    "index.html": {
        "title": "CybKart Global | AI-Powered Digital Growth Platform",
        "description": "CybKart Global builds ultra-premium websites, custom AI automations, systems integration, and high-conversion lead gen workflows for modern high-end businesses.",
        "url": "https://cybkartglobal.com/"
    },
    "services.html": {
        "title": "Our Services | CybKart Global Growth Infrastructure",
        "description": "Explore CybKart Global's elite digital services: High-converting local sites, Local SEO & Google Maps domination, and Automated Booking & Lead systems.",
        "url": "https://cybkartglobal.com/services.html"
    },
    "portfolio.html": {
        "title": "Portfolio | CybKart Global Web & AI Projects",
        "description": "View CybKart Global's portfolio of premium websites built for local home services, generating massive ROI, phone calls, and local search dominance.",
        "url": "https://cybkartglobal.com/portfolio.html"
    },
    "pricing.html": {
        "title": "Pricing & Packages | CybKart Global",
        "description": "View transparent pricing for CybKart Global's digital growth packages: Starter, Growth, Pro, and Elite tiers designed for scaling local service businesses.",
        "url": "https://cybkartglobal.com/pricing.html"
    },
    "contact.html": {
        "title": "Contact Us | CybKart Global Strategy & Briefing",
        "description": "Contact CybKart Global's lead growth systems architects. Request a comprehensive audit, competitor teardown, and bespoke digital scaling plan.",
        "url": "https://cybkartglobal.com/contact.html"
    },
    "industries.html": {
        "title": "Industries We Serve | CybKart Global",
        "description": "CybKart Global engineers digital dominance for HVAC, Auto Detailing, Roofing, Pest Control, Plumbing, and other premium local service industries.",
        "url": "https://cybkartglobal.com/industries.html"
    },
    "toolkit.html": {
        "title": "Tech Stack & Toolkit | CybKart Global",
        "description": "Discover the bleeding-edge technology stack CybKart Global uses to build lightning-fast websites and AI-driven growth systems.",
        "url": "https://cybkartglobal.com/toolkit.html"
    }
}

schema_markup = """
  <!-- Local Business Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "CybKart Global",
    "image": "https://cybkartglobal.com/logo.png",
    "@id": "",
    "url": "https://cybkartglobal.com",
    "telephone": "8446991255",
    "email": "info@cybkartglobal.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "1309 Coffeen Ave",
      "addressLocality": "Sheridan",
      "addressRegion": "WY",
      "postalCode": "82801",
      "addressCountry": "US"
    },
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "opens": "09:00",
      "closes": "18:00"
    },
    "sameAs": [
      "https://twitter.com/cybkartglobal",
      "https://www.linkedin.com/company/cybkartglobal"
    ]
  }
  </script>
"""

for file in html_files:
    if file not in seo_data:
        continue
        
    data = seo_data[file]
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of <head> tag
    head_end_idx = content.find('</head>')
    if head_end_idx == -1:
        continue
        
    head_content = content[:head_end_idx]
    body_content = content[head_end_idx:]
    
    # Remove existing <title>, <meta name="description">, canonical, og:, twitter:, and schema
    head_content = re.sub(r'<title>.*?</title>', '', head_content, flags=re.IGNORECASE | re.DOTALL)
    head_content = re.sub(r'<meta\s+name=["\']description["\'][^>]*>', '', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>', '', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'<meta\s+property=["\']og:.*?["\'][^>]*>', '', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'<meta\s+name=["\']twitter:.*?["\'][^>]*>', '', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'<!-- Local Business Schema -->\s*<script type="application/ld\+json">.*?</script>', '', head_content, flags=re.IGNORECASE | re.DOTALL)
    
    # Clean up empty lines
    head_content = re.sub(r'\n\s*\n', '\n', head_content)

    new_seo = f"""
  <title>{data['title']}</title>
  <meta name="description" content="{data['description']}">
  
  <!-- Canonical URL -->
  <link rel="canonical" href="{data['url']}" />
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{data['url']}" />
  <meta property="og:title" content="{data['title']}" />
  <meta property="og:description" content="{data['description']}" />
  <meta property="og:image" content="https://cybkartglobal.com/contact-hq.png" />
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="{data['url']}" />
  <meta name="twitter:title" content="{data['title']}" />
  <meta name="twitter:description" content="{data['description']}" />
  <meta name="twitter:image" content="https://cybkartglobal.com/contact-hq.png" />
  {schema_markup}
"""
    
    # Insert new SEO right after the <head> tag
    head_start_idx = head_content.find('<head>') + 6
    final_head = head_content[:head_start_idx] + new_seo + head_content[head_start_idx:]
    
    # Combine back
    final_content = final_head + body_content
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(final_content)

print("Applied full SEO implementation to all HTML files.")
