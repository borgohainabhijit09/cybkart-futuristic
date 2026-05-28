# Append CSS overrides to combined.css

new_css = """
/* ==========================================================================
   USER REQUESTED REDESIGNS (LOGO, BENTO, MEGA MENU)
   ========================================================================== */

/* 1. Complete Logo Font Color White and Constant, with dark pill background */
.luxury-navbar .nav-logo,
.luxury-navbar.scrolled .nav-logo {
  background: #090b14 !important;
  border-color: rgba(255, 255, 255, 0.1) !important;
}

.luxury-navbar .logo-text,
.luxury-navbar.scrolled .logo-text,
.mobile-menu-header .logo-text,
.footer-logo .logo-text {
  color: #ffffff !important;
}

.luxury-navbar .logo-text .thin,
.luxury-navbar.scrolled .logo-text .thin,
.mobile-menu-header .logo-text .thin,
.footer-logo .logo-text .thin {
  color: #ffffff !important;
  font-weight: 400 !important;
}

/* 2. Core Capabilities Pillars Font Colors to White (Darken the Cards) */
.bento-capabilities-section .bento-card {
  background: #090b14 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 30px 60px rgba(9, 11, 20, 0.4) !important;
}

.bento-capabilities-section .bento-card:hover {
  border-color: rgba(0, 140, 255, 0.4) !important;
  box-shadow: 0 40px 80px rgba(0, 140, 255, 0.2) !important;
}

.bento-capabilities-section .bento-title,
.bento-capabilities-section .bento-text {
  color: #ffffff !important;
}

.bento-capabilities-section .bento-text {
  opacity: 0.8;
}

/* Make sure the visual section inside the capability card is also dark */
.bento-capabilities-section .bento-visual {
  background: rgba(255, 255, 255, 0.05) !important;
  border-color: rgba(255, 255, 255, 0.1) !important;
}

/* 3. Redesign the Hover Menu Design for Services (Mega Menu) */
.mega-menu-container {
  background: #090b14 !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 40px 100px rgba(9, 11, 20, 0.5) !important;
  border-radius: 24px !important;
  backdrop-filter: blur(30px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
}

.mega-menu-container .column-eyebrow {
  color: rgba(255, 255, 255, 0.5) !important;
}

.mega-menu-container .column-title {
  color: #ffffff !important;
}

.mega-link-item {
  background: rgba(255, 255, 255, 0.03) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 16px !important;
  padding: 1.25rem !important;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.mega-link-item:hover {
  background: rgba(0, 140, 255, 0.1) !important;
  border-color: rgba(0, 140, 255, 0.3) !important;
  transform: translateX(8px) !important;
}

.mega-link-item .link-title {
  color: #ffffff !important;
  font-weight: 700 !important;
}

.mega-link-item .link-desc {
  color: rgba(255, 255, 255, 0.6) !important;
}

.mega-link-item .link-icon {
  background: rgba(255, 255, 255, 0.1) !important;
  color: #ffffff !important;
}

.mega-featured-card {
  background: linear-gradient(135deg, rgba(0, 85, 255, 0.2), rgba(0, 191, 255, 0.1)) !important;
  border: 1px solid rgba(0, 191, 255, 0.2) !important;
}

.mega-featured-card .featured-title,
.mega-featured-card .featured-text {
  color: #ffffff !important;
}
"""

with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Applied CSS redesigns.")
