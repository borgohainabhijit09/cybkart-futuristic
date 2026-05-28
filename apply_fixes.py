import os
import glob
import re

# 1. Update HTML files to include favicon
html_files = glob.glob("*.html")
favicon_tag = '  <link rel="icon" href="logo.png" type="image/png">\n'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if '<link rel="icon"' not in content:
        # Insert after <title> tag
        title_idx = content.find('</title>')
        if title_idx != -1:
            insertion_pt = title_idx + 8 # length of </title>
            content = content[:insertion_pt] + '\n' + favicon_tag + content[insertion_pt:]
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)

# 2. Append CSS overrides to fix Loader Mobile Size and Navbar Logo Color
css_overrides = """
/* ==========================================================================
   USER REQUESTED FIXES (LOADER SIZE, LOGO COLOR CONSTANCY)
   ========================================================================== */

/* Reduce Loader Font Size on Mobile */
@media (max-width: 768px) {
  .pl-word-cybkart,
  .pl-word-global {
    font-size: clamp(1.5rem, 6vw, 2.5rem) !important;
  }
}

/* Make Navbar Logo Text Color Constant and Visible on Light Theme */
.luxury-navbar .logo-text,
.luxury-navbar.scrolled .logo-text,
.mobile-menu-header .logo-text,
.footer-logo .logo-text {
  color: #0b0f19 !important;
}

.luxury-navbar .logo-text .thin,
.luxury-navbar.scrolled .logo-text .thin,
.mobile-menu-header .logo-text .thin,
.footer-logo .logo-text .thin {
  color: #0055ff !important;
  font-weight: 500 !important;
}
"""

with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(css_overrides)

print("Applied HTML favicon updates and CSS overrides.")
