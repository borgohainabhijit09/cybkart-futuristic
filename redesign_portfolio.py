import os

new_portfolio_html = """
    <!-- ========================================
         VIEW 5: PORTFOLIO (CINEMATIC CASE STUDIES) - REDESIGNED
         ======================================== -->
    <section id="view-portfolio" class="page-view active">
      
      <!-- Portfolio Hero -->
      <div class="portfolio-hero">
        <div class="mesh-bg-overlay-light"></div>
        <div class="container section-padding" style="position: relative; z-index: 2; text-align: center;">
          <div class="services-eyebrow"><span class="pulse-dot-blue"></span>SELECTED WORKS</div>
          <h1 class="services-massive-title">Digital <span class="gradient-text">Masterpieces.</span></h1>
          <p class="services-lead-text">A carefully selected showcase of high-end business transformations. Where ultra-premium aesthetic design meets explosive organic conversion.</p>
        </div>
      </div>

      <!-- Portfolio Bento Grid -->
      <div class="portfolio-bento-section">
        <div class="container">
          <div class="portfolio-bento-grid">
            
            <!-- Project 1: Detailing (Large Span) -->
            <div class="bento-project-card bento-large">
              <img src="portfolio-detailing.png" alt="Apex Detail Lab" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">ELITE AUTO DETAILING</span>
                  <span class="meta-year">2026</span>
                </div>
                <h3 class="bento-title">Apex Detail Lab</h3>
                <p class="bento-desc">Immersive visual scheduling funnel integrated with automated text-back systems to capture high-ticket ceramic coating clients on autopilot.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">3.1x</span>
                    <span class="stat-lbl">Bookings</span>
                  </div>
                  <div class="stat-box">
                    <span class="stat-val">10s</span>
                    <span class="stat-lbl">Text Response</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 2: Roofing (Standard) -->
            <div class="bento-project-card">
              <img src="portfolio-roofing.png" alt="Climate Control Co" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">ROOFING & EXTERIORS</span>
                </div>
                <h3 class="bento-title">Skyline Roofing</h3>
                <p class="bento-desc">Complete web overhaul resulting in a massive influx of local emergency booking requests.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">+140%</span>
                    <span class="stat-lbl">Phone Calls</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 3: Dental (Standard) -->
            <div class="bento-project-card">
              <img src="portfolio-dentist.png" alt="Premium Dental Clinic" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">COSMETIC DENTISTRY</span>
                </div>
                <h3 class="bento-title">Lumina Dental</h3>
                <p class="bento-desc">Sleek, minimalist booking engine targeting high-end cosmetic patients.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">#1</span>
                    <span class="stat-lbl">Maps Rank</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 4: Restaurant (Large Span) -->
            <div class="bento-project-card bento-large reverse-content">
              <img src="portfolio-restaurant.png" alt="Luxury Restaurant" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">LUXURY DINING</span>
                  <span class="meta-year">2025</span>
                </div>
                <h3 class="bento-title">Maison Rouge</h3>
                <p class="bento-desc">A moody, highly visual experience that captures the essence of fine dining while integrating a frictionless table reservation CRM.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">Sub-200ms</span>
                    <span class="stat-lbl">Load Speed</span>
                  </div>
                  <div class="stat-box">
                    <span class="stat-val">+85%</span>
                    <span class="stat-lbl">Reservations</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

          </div>
        </div>
      </div>
      
      <!-- Call to Action Banner -->
      <div class="portfolio-cta-banner">
        <div class="container" style="text-align: center;">
          <h2 style="font-family: var(--font-heading); font-size: 2.5rem; font-weight: 800; color: #0b0f19; margin-bottom: 1rem;">Ready to build yours?</h2>
          <p style="color: #475569; font-size: 1.1rem; margin-bottom: 2rem;">Join the ranks of local service leaders dominating their markets.</p>
          <a href="pricing.html" class="btn-primary">View Pricing Architecture ↗ <span class="btn-slide-bg"></span></a>
        </div>
      </div>

    </section>
"""

new_css = """
/* ==========================================================================
   REDESIGNED PORTFOLIO PAGE STYLES (LIGHT LUXURY BENTO)
   ========================================================================== */

#view-portfolio {
  background: transparent;
}

.portfolio-hero {
  position: relative;
  padding: 10rem 0 4rem 0;
}

.mesh-bg-overlay-light {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: 
    radial-gradient(circle at 50% 0%, rgba(0, 85, 255, 0.05) 0%, transparent 60%);
  opacity: 1;
}

.portfolio-bento-section {
  padding-bottom: 8rem;
}

.portfolio-bento-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

@media (max-width: 991px) {
  .portfolio-bento-grid {
    grid-template-columns: 1fr;
  }
}

.bento-project-card {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  min-height: 450px;
  background: #000;
  display: flex;
  align-items: flex-end;
  border: 1px solid rgba(9, 11, 20, 0.08);
  box-shadow: 0 20px 40px rgba(9, 11, 20, 0.05);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
}

.bento-large {
  grid-column: span 2;
  min-height: 550px;
}

@media (max-width: 991px) {
  .bento-large {
    grid-column: span 1;
  }
}

.bento-project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 30px 60px rgba(0, 85, 255, 0.15);
  border-color: rgba(0, 85, 255, 0.3);
}

.bento-bg-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}

.bento-project-card:hover .bento-bg-img {
  transform: scale(1.05);
}

.bento-overlay-gradient {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);
  transition: opacity 0.4s ease;
}

.bento-content {
  position: relative;
  z-index: 2;
  padding: 3rem;
  width: 100%;
  color: #ffffff;
  display: flex;
  flex-direction: column;
}

.bento-large.reverse-content .bento-content {
  align-items: flex-end;
  text-align: right;
}

.bento-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.meta-tag {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  padding: 0.4rem 1rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.meta-year {
  font-size: 0.85rem;
  font-weight: 600;
  opacity: 0.7;
}

.bento-title {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.8rem;
}

.bento-desc {
  font-size: 1.05rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.7);
  max-width: 500px;
  margin-bottom: 2rem;
}

.bento-stats {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.bento-large.reverse-content .bento-stats {
  justify-content: flex-end;
}

.stat-box {
  display: flex;
  flex-direction: column;
}

.stat-val {
  font-family: var(--font-heading);
  font-size: 1.8rem;
  font-weight: 800;
  color: #00bfff;
}

.stat-lbl {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.7;
}

.bento-btn {
  align-self: flex-start;
  display: inline-flex;
  align-items: center;
  padding: 0.8rem 1.8rem;
  background: #ffffff;
  color: #0b0f19;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.95rem;
  border-radius: 100px;
  text-decoration: none;
  transition: all 0.3s ease;
}

.bento-large.reverse-content .bento-btn {
  align-self: flex-end;
}

.bento-btn:hover {
  background: #0055ff;
  color: #ffffff;
  box-shadow: 0 10px 20px rgba(0, 85, 255, 0.3);
}

.portfolio-cta-banner {
  background: rgba(255, 255, 255, 0.6);
  border-top: 1px solid rgba(9, 11, 20, 0.05);
  border-bottom: 1px solid rgba(9, 11, 20, 0.05);
  padding: 6rem 0;
}
"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Remove the old portfolio section content
start_tag = '<section id="view-portfolio" class="page-view editorial-portfolio-section">'
end_tag = '</section>'
start_idx = content.find(start_tag)
end_idx = content.find(end_tag, start_idx) + len(end_tag)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_portfolio_html + content[end_idx:]
    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced portfolio.html content.")
else:
    print("Could not find section boundaries in portfolio.html")

# Append new CSS to combined.css
with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(new_css)
print("Appended new CSS to combined.css")
