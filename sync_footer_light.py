import os
import re

# 1. Update CSS to Light Theme
with open('css/combined.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Locate the redesigned block
start_marker = "/* ==========================================================================\n   REDESIGNED SERVICES PAGE STYLES (DARK LUXURY)\n   ========================================================================== */"
if start_marker in css_content:
    idx = css_content.find(start_marker)
    # We will just replace everything after this marker with a light theme version
    css_to_keep = css_content[:idx]
    
    light_theme_css = """
/* ==========================================================================
   REDESIGNED SERVICES PAGE STYLES (LIGHT LUXURY)
   ========================================================================== */

#view-services {
  background: transparent;
  color: #0b0f19;
  padding-bottom: 6rem;
}

.services-hero-container {
  position: relative;
  padding: 10rem 0 6rem 0;
  overflow: hidden;
  border-bottom: 1px solid rgba(9, 11, 20, 0.05);
}

.mesh-bg-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: 
    radial-gradient(circle at 50% -20%, rgba(0, 85, 255, 0.08) 0%, transparent 60%),
    linear-gradient(rgba(9, 11, 20, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(9, 11, 20, 0.02) 1px, transparent 1px);
  background-size: 100% 100%, 40px 40px, 40px 40px;
  opacity: 1;
}

.services-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #0055ff;
  background: rgba(0, 85, 255, 0.05);
  padding: 0.5rem 1.2rem;
  border-radius: 100px;
  border: 1px solid rgba(0, 85, 255, 0.15);
  margin-bottom: 1.5rem;
}

.pulse-dot-blue {
  width: 6px;
  height: 6px;
  background: #0055ff;
  border-radius: 50%;
  box-shadow: 0 0 10px #0055ff;
  animation: pulse-active-light 2s infinite;
}

@keyframes pulse-active-light {
  0% { box-shadow: 0 0 0 0 rgba(0, 85, 255, 0.4); }
  70% { box-shadow: 0 0 0 6px rgba(0, 85, 255, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 85, 255, 0); }
}

.services-massive-title {
  font-family: var(--font-heading);
  font-size: clamp(3.5rem, 8vw, 5.5rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: #0b0f19;
  margin-bottom: 1.5rem;
}

.services-lead-text {
  font-size: 1.25rem;
  color: #475569;
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Alternate Service Blocks */
.service-block-alternate {
  padding: 6rem 0;
  border-bottom: 1px solid rgba(9, 11, 20, 0.05);
}

.service-flex-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 5rem;
}

.service-block-alternate.reverse-layout .service-flex-row {
  flex-direction: row-reverse;
}

@media (max-width: 991px) {
  .service-flex-row, .service-block-alternate.reverse-layout .service-flex-row {
    flex-direction: column;
    gap: 3rem;
  }
}

.service-text-col {
  flex: 1;
}

.service-image-col {
  flex: 1.1;
  position: relative;
}

.service-num {
  font-family: var(--font-heading);
  font-size: 5rem;
  font-weight: 800;
  color: rgba(9, 11, 20, 0.04);
  line-height: 1;
  display: block;
  margin-bottom: -1.5rem;
  z-index: 0;
  position: relative;
}

.service-block-title {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  font-weight: 800;
  color: #0b0f19;
  margin-bottom: 1rem;
  position: relative;
  z-index: 1;
}

.service-block-desc {
  font-size: 1.1rem;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 2.5rem;
}

.service-feature-list {
  list-style: none;
  padding: 0;
  margin: 0 0 2.5rem 0;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.service-feature-list li {
  display: flex;
  align-items: flex-start;
  gap: 1.2rem;
}

.feat-icon-box {
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(9, 11, 20, 0.06);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
  box-shadow: 0 10px 20px rgba(9, 11, 20, 0.03);
}

.feat-text h4 {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 700;
  color: #0b0f19;
  margin-bottom: 0.3rem;
}

.feat-text p {
  font-size: 0.9rem;
  color: #64748b;
  line-height: 1.5;
}

.btn-service-action {
  display: inline-flex;
  align-items: center;
  padding: 0.9rem 2rem;
  background: linear-gradient(135deg, #0055ff, #00bfff);
  color: #ffffff;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1rem;
  border-radius: 100px;
  text-decoration: none;
  box-shadow: 0 10px 30px rgba(0, 85, 255, 0.2);
  transition: all 0.3s ease;
}

.btn-service-action:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px rgba(0, 85, 255, 0.3);
}

.service-img-glass-wrapper {
  position: relative;
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(9, 11, 20, 0.05);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 30px 60px rgba(9, 11, 20, 0.05);
}

.service-img-glass-wrapper::before {
  content: '';
  position: absolute;
  top: -2px; left: -2px; right: -2px; bottom: -2px;
  background: linear-gradient(135deg, rgba(0, 85, 255, 0.3), transparent, rgba(255, 255, 255, 0.8));
  border-radius: 26px;
  z-index: -1;
  opacity: 0.5;
}

.service-mockup-img {
  width: 100%;
  border-radius: 16px;
  display: block;
}

.glass-floating-badge {
  position: absolute;
  bottom: -20px;
  left: -20px;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(9, 11, 20, 0.05);
  padding: 1rem 1.5rem;
  border-radius: 100px;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  box-shadow: 0 20px 40px rgba(9, 11, 20, 0.06);
  animation: float 6s ease-in-out infinite;
}

.glass-floating-badge.right-badge {
  left: auto;
  right: -20px;
  bottom: 40px;
  animation: float 7s ease-in-out infinite reverse;
}

.badge-icon {
  font-size: 1.2rem;
}

.badge-text {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.95rem;
  color: #0b0f19;
}

/* Timeline */
.cybkart-method-section {
  padding: 8rem 0;
  background: linear-gradient(180deg, #fafafc, #f1f5f9);
}

.method-header {
  text-align: center;
  margin-bottom: 5rem;
}

.method-title {
  font-family: var(--font-heading);
  font-size: 3rem;
  font-weight: 800;
  color: #0b0f19;
  margin-bottom: 1rem;
}

.method-lead {
  font-size: 1.15rem;
  color: #475569;
}

.method-timeline {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.method-step {
  position: relative;
  display: flex;
  gap: 2.5rem;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(9, 11, 20, 0.05);
  padding: 2.5rem;
  border-radius: 24px;
  transition: all 0.4s ease;
  box-shadow: 0 10px 30px rgba(9, 11, 20, 0.02);
}

.method-step:hover {
  background: #ffffff;
  border-color: rgba(0, 85, 255, 0.2);
  transform: translateX(10px);
  box-shadow: 0 15px 40px rgba(9, 11, 20, 0.05);
}

.step-dot {
  position: absolute;
  left: -40px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  background: #0055ff;
  border-radius: 50%;
  box-shadow: 0 0 15px rgba(0, 85, 255, 0.3);
}

.step-line {
  position: absolute;
  left: -33px;
  top: -2rem;
  bottom: -2rem;
  width: 2px;
  background: rgba(9, 11, 20, 0.08);
  z-index: -1;
}

.method-step:first-child .step-line { top: 50%; }
.method-step:last-child .step-line { bottom: 50%; }

.step-content {
  flex: 1;
}

.step-num {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 800;
  color: #0b0f19;
  margin-bottom: 0.5rem;
}

.step-content p {
  color: #64748b;
  line-height: 1.6;
  font-size: 0.95rem;
}

/* Light Table Styles */
.dark-table-wrap {
  background: rgba(255, 255, 255, 0.6) !important;
  border: 1px solid rgba(9, 11, 20, 0.05) !important;
  box-shadow: 0 30px 60px rgba(9, 11, 20, 0.02);
}

.dark-table th {
  color: #0b0f19 !important;
}

.dark-table .feat-column {
  color: #0b0f19 !important;
}

.dark-table .cyb-column {
  background: rgba(0, 85, 255, 0.02) !important;
  color: #0055ff !important;
}

.dark-table .legacy-column {
  color: #64748b !important;
}

.dark-table th, .dark-table td {
  border-bottom: 1px solid rgba(9, 11, 20, 0.04) !important;
}

.services-comparison-section {
  padding-top: 6rem;
  padding-bottom: 6rem;
}
"""
    
    with open('css/combined.css', 'w', encoding='utf-8') as f:
        f.write(css_to_keep + light_theme_css)
    print("Reverted combined.css back to Light Theme.")


# 2. Sync Footers across all HTML files
# First, extract footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

footer_match = re.search(r'(<footer id="global-footer">.*?</footer>)', index_html, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    
    # Files to update
    files_to_sync = ['services.html', 'portfolio.html', 'pricing.html', 'contact.html', 'industries.html', 'toolkit.html']
    
    for file in files_to_sync:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace footer in the file
            content = re.sub(r'<footer id="global-footer">.*?</footer>', footer_html, content, flags=re.DOTALL)
            
            # Also, fix the inline styles on the comparative section header inside services.html that forced white text
            if file == 'services.html':
                content = content.replace('<h3 style="color:#fff !important;">', '<h3>')
                content = content.replace('<p style="color:rgba(255,255,255,0.6) !important;">', '<p>')
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Synced footer for {file}")
else:
    print("Could not find footer in index.html")
