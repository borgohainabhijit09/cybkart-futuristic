import re

with open('css/combined.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the previous overrides we want to remove
marker = '/* 2. Core Capabilities Pillars Font Colors to White (Darken the Cards) */'
idx = content.find(marker)

if idx != -1:
    content = content[:idx]
    print("Removed dark theme overrides.")

new_light_overrides = """
/* 2. CORE CAPABILITIES - Keep Light Theme (Dark Text) */
.bento-capabilities-section .bento-card {
  background: rgba(255, 255, 255, 0.7) !important;
  border: 1px solid rgba(9, 11, 20, 0.05) !important;
  box-shadow: 0 20px 40px rgba(9, 11, 20, 0.03) !important;
}

.bento-capabilities-section .bento-title,
.bento-capabilities-section .bento-text {
  color: #0b0f19 !important; /* Premium dark text */
}

.bento-capabilities-section .bento-text {
  opacity: 0.7;
}

.bento-capabilities-section .bento-visual {
  background: rgba(255, 255, 255, 0.8) !important;
  border-color: rgba(9, 11, 20, 0.05) !important;
}

/* 3. Redesign the Hover Menu Design for Services (Mega Menu) - LIGHT THEME */
.mega-menu-container {
  background: rgba(255, 255, 255, 0.85) !important;
  border: 1px solid rgba(9, 11, 20, 0.08) !important;
  box-shadow: 0 40px 100px rgba(9, 11, 20, 0.08) !important;
  border-radius: 24px !important;
  backdrop-filter: blur(30px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(180%) !important;
}

.mega-menu-container .column-eyebrow {
  color: rgba(9, 11, 20, 0.5) !important;
}

.mega-menu-container .column-title {
  color: #0b0f19 !important;
}

.mega-link-item {
  background: rgba(255, 255, 255, 0.5) !important;
  border: 1px solid rgba(9, 11, 20, 0.03) !important;
  border-radius: 16px !important;
  padding: 1.25rem !important;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.mega-link-item:hover {
  background: #ffffff !important;
  border-color: rgba(0, 140, 255, 0.2) !important;
  transform: translateX(8px) !important;
  box-shadow: 0 10px 20px rgba(0, 140, 255, 0.05) !important;
}

.mega-link-item .link-title {
  color: #0b0f19 !important;
  font-weight: 700 !important;
}

.mega-link-item .link-desc {
  color: #475569 !important;
}

.mega-link-item .link-icon {
  background: rgba(0, 140, 255, 0.05) !important;
  color: #0055ff !important;
  border: 1px solid rgba(0, 140, 255, 0.1) !important;
}

.mega-featured-card {
  background: linear-gradient(135deg, rgba(0, 85, 255, 0.05), rgba(0, 191, 255, 0.02)) !important;
  border: 1px solid rgba(0, 140, 255, 0.15) !important;
}

.mega-featured-card .featured-title,
.mega-featured-card .featured-text {
  color: #0b0f19 !important;
}
"""

with open('css/combined.css', 'w', encoding='utf-8') as f:
    f.write(content + new_light_overrides)

print("Reverted to light theme and redesigned hover menu.")
