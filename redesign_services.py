import os

new_services_html = """
    <!-- ========================================
         VIEW 2: SERVICES (MODULAR SOLUTIONS) - REDESIGNED
         ======================================== -->
    <section id="view-services" class="page-view active">
      <div class="services-hero-container">
        <div class="mesh-bg-overlay"></div>
        <div class="container section-padding" style="position: relative; z-index: 2; text-align: center;">
          <div class="services-eyebrow"><span class="pulse-dot-blue"></span>CORE CAPABILITIES</div>
          <h1 class="services-massive-title">Systems & <span class="gradient-text">Operations.</span></h1>
          <p class="services-lead-text">We construct high-frequency digital weapons engineered to help local trade businesses capture every lead, rank #1 in local search, and automate customer scheduling.</p>
        </div>
      </div>

      <!-- Core Service 1: Web Architecture -->
      <div class="service-block-alternate">
        <div class="container service-flex-row">
          <div class="service-image-col">
            <div class="service-img-glass-wrapper">
              <img src="web-mockup.png" alt="Premium Web Design Mockup" class="service-mockup-img">
              <div class="glass-floating-badge">
                <span class="badge-icon">⚡</span>
                <span class="badge-text">&lt; 300ms Load Time</span>
              </div>
            </div>
          </div>
          <div class="service-text-col">
            <span class="service-num">01</span>
            <h2 class="service-block-title">Premium Web Architecture</h2>
            <p class="service-block-desc">Ultra-premium websites engineered specifically for local home services. Designed to load instantly, display flawlessly on mobile devices, and convert visitors into scheduled service appointments.</p>
            
            <ul class="service-feature-list">
              <li>
                <div class="feat-icon-box">📱</div>
                <div class="feat-text">
                  <h4>Mobile-First Fluid Layouts</h4>
                  <p>Designs that look and perform like native apps on smartphones.</p>
                </div>
              </li>
              <li>
                <div class="feat-icon-box">🚀</div>
                <div class="feat-text">
                  <h4>Edge-Network Performance</h4>
                  <p>Google PageSpeed scores consistently exceeding 95+.</p>
                </div>
              </li>
              <li>
                <div class="feat-icon-box">🗺️</div>
                <div class="feat-text">
                  <h4>Geo-Optimized Landing Pages</h4>
                  <p>Programmatic pages targeting specific cities and suburbs.</p>
                </div>
              </li>
            </ul>
            <a href="portfolio.html" class="btn-service-action">View Live Builds ↗</a>
          </div>
        </div>
      </div>

      <!-- Core Service 2: SEO & Local Dominance -->
      <div class="service-block-alternate reverse-layout">
        <div class="container service-flex-row">
          <div class="service-text-col">
            <span class="service-num">02</span>
            <h2 class="service-block-title">SEO & Local Dominance</h2>
            <p class="service-block-desc">Hyper-targeted geographic search strategies and Google Business Profile optimization designed to rank your company in the local 3-pack for high-intent emergency keywords.</p>
            
            <ul class="service-feature-list">
              <li>
                <div class="feat-icon-box">📍</div>
                <div class="feat-text">
                  <h4>Google Maps 3-Pack Rankings</h4>
                  <p>Strategic local citations to secure top placement in local search.</p>
                </div>
              </li>
              <li>
                <div class="feat-icon-box">⭐</div>
                <div class="feat-text">
                  <h4>Automated Review Systems</h4>
                  <p>SMS funnels that capture 5-star reviews immediately after jobs.</p>
                </div>
              </li>
              <li>
                <div class="feat-icon-box">📊</div>
                <div class="feat-text">
                  <h4>Live Rank Tracking</h4>
                  <p>Real-time dashboards monitoring your keyword positions.</p>
                </div>
              </li>
            </ul>
            <a href="contact.html" class="btn-service-action">Audit Your Rankings ↗</a>
          </div>
          <div class="service-image-col">
            <div class="service-img-glass-wrapper">
              <img src="seo-dashboard.png" alt="SEO Dashboard Mockup" class="service-mockup-img">
              <div class="glass-floating-badge right-badge">
                <span class="badge-icon">#1</span>
                <span class="badge-text">Maps Dominance</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Core Service 3: Lead Operations -->
      <div class="service-block-alternate">
        <div class="container service-flex-row">
          <div class="service-image-col">
            <div class="service-img-glass-wrapper">
              <img src="automation-flow.png" alt="Automation Flow Visual" class="service-mockup-img">
              <div class="glass-floating-badge">
                <span class="badge-icon">⚙️</span>
                <span class="badge-text">&lt; 10s Response Time</span>
              </div>
            </div>
          </div>
          <div class="service-text-col">
            <span class="service-num">03</span>
            <h2 class="service-block-title">AI & Lead Operations</h2>
            <p class="service-block-desc">Instant missed-call text-back systems, interactive scheduling calendars, and direct dispatch integrations (Jobber/ServiceTitan/Housecall Pro) to secure leads instantly.</p>
            
            <ul class="service-feature-list">
              <li>
                <div class="feat-icon-box">💬</div>
                <div class="feat-text">
                  <h4>Missed-Call Text Back</h4>
                  <p>Automatic SMS responder that replies to missed leads in under 10 seconds.</p>
                </div>
              </li>
              <li>
                <div class="feat-icon-box">📅</div>
                <div class="feat-text">
                  <h4>Automated Booking Engines</h4>
                  <p>Direct scheduling widgets synced with your live dispatch calendar.</p>
                </div>
              </li>
              <li>
                <div class="feat-icon-box">🤖</div>
                <div class="feat-text">
                  <h4>AI Chatbot Assistants</h4>
                  <p>24/7 intelligent agents that qualify leads while you sleep.</p>
                </div>
              </li>
            </ul>
            <a href="contact.html" class="btn-service-action">Automate My Leads ↗</a>
          </div>
        </div>
      </div>

      <!-- The CybKart Method Section -->
      <div class="cybkart-method-section">
        <div class="container">
          <div class="method-header">
            <span class="services-eyebrow"><span class="pulse-dot-blue"></span>PIPELINE</span>
            <h2 class="method-title">The CybKart Method.</h2>
            <p class="method-lead">A surgical 4-step deployment process guaranteeing zero downtime.</p>
          </div>
          
          <div class="method-timeline">
            <div class="method-step">
              <div class="step-line"></div>
              <div class="step-dot"></div>
              <div class="step-content">
                <h3 class="step-num">01. Blueprint</h3>
                <p>We audit your current digital footprint and engineer a custom growth blueprint targeting specific revenue bottlenecks.</p>
              </div>
            </div>
            <div class="method-step">
              <div class="step-line"></div>
              <div class="step-dot"></div>
              <div class="step-content">
                <h3 class="step-num">02. Construct</h3>
                <p>Our developers build your new platform on a private staging environment. We code, write copy, and configure SEO.</p>
              </div>
            </div>
            <div class="method-step">
              <div class="step-line"></div>
              <div class="step-dot"></div>
              <div class="step-content">
                <h3 class="step-num">03. Integrate</h3>
                <p>We connect the system to your existing CRM (Jobber, ServiceTitan) and deploy the AI communication workflows.</p>
              </div>
            </div>
            <div class="method-step">
              <div class="step-line"></div>
              <div class="step-dot"></div>
              <div class="step-content">
                <h3 class="step-num">04. Ignite</h3>
                <p>The system goes live. We monitor traffic flows, initiate local SEO campaigns, and provide ongoing technical overwatch.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Comparative Metrics Grid (Dark Mode Adjusted) -->
      <div class="services-comparison-section">
        <div class="container">
          <div class="comp-header">
            <h3 style="color:#fff !important;">Standard Templates vs. CybKart Systems</h3>
            <p style="color:rgba(255,255,255,0.6) !important;">Why local service leaders choose advanced custom architecture over simple visual themes.</p>
          </div>
          <div class="comparison-table-wrap dark-table-wrap">
            <table class="comp-table dark-table">
              <thead>
                <tr>
                  <th class="feat-column">System Parameter</th>
                  <th class="cyb-column">CybKart Custom Systems</th>
                  <th class="legacy-column">Standard Template (WordPress/Wix)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="feat-column">Page Load Performance</td>
                  <td class="cyb-column"><span class="check-icon">✓</span> Sub-300ms edge delivery (95+ score)</td>
                  <td class="legacy-column"><span class="cross-icon">✗</span> 3.4s - 6.2s load delay (40-60 score)</td>
                </tr>
                <tr>
                  <td class="feat-column">Unanswered Call Recovery</td>
                  <td class="cyb-column"><span class="check-icon">✓</span> Automated SMS text-back in &lt;10s</td>
                  <td class="legacy-column"><span class="cross-icon">✗</span> Missed lead (customer calls competitor)</td>
                </tr>
                <tr>
                  <td class="feat-column">Local SEO & Maps Sync</td>
                  <td class="cyb-column"><span class="check-icon">✓</span> Automated local review collection + GBP API</td>
                  <td class="legacy-column"><span class="cross-icon">✗</span> Manual review requests with high friction</td>
                </tr>
                <tr>
                  <td class="feat-column">Multi-City Landing Pages</td>
                  <td class="cyb-column"><span class="check-icon">✓</span> Programmatic city-suburb templates</td>
                  <td class="legacy-column"><span class="cross-icon">✗</span> Heavy manual pages that slow down database</td>
                </tr>
                <tr>
                  <td class="feat-column">Booking Friction</td>
                  <td class="cyb-column"><span class="check-icon">✓</span> Direct API integration with Jobber / ServiceTitan</td>
                  <td class="legacy-column"><span class="cross-icon">✗</span> Standard static form requiring manual callback</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
"""

new_css = """
/* ==========================================================================
   REDESIGNED SERVICES PAGE STYLES (DARK LUXURY)
   ========================================================================== */

#view-services {
  background: #090b14;
  color: #ffffff;
  padding-bottom: 6rem;
}

.services-hero-container {
  position: relative;
  padding: 10rem 0 6rem 0;
  overflow: hidden;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.mesh-bg-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: 
    radial-gradient(circle at 50% -20%, rgba(0, 85, 255, 0.15) 0%, transparent 60%),
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 100% 100%, 40px 40px, 40px 40px;
  opacity: 0.8;
}

.services-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #00bfff;
  background: rgba(0, 140, 255, 0.1);
  padding: 0.5rem 1.2rem;
  border-radius: 100px;
  border: 1px solid rgba(0, 140, 255, 0.2);
  margin-bottom: 1.5rem;
}

.pulse-dot-blue {
  width: 6px;
  height: 6px;
  background: #00bfff;
  border-radius: 50%;
  box-shadow: 0 0 10px #00bfff;
  animation: pulse-active 2s infinite;
}

.services-massive-title {
  font-family: var(--font-heading);
  font-size: clamp(3.5rem, 8vw, 5.5rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: #ffffff;
  margin-bottom: 1.5rem;
}

.services-lead-text {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.7);
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Alternate Service Blocks */
.service-block-alternate {
  padding: 6rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.03);
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
  color: rgba(255, 255, 255, 0.04);
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
  color: #ffffff;
  margin-bottom: 1rem;
  position: relative;
  z-index: 1;
}

.service-block-desc {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.6);
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
  background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01));
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.feat-text h4 {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.3rem;
}

.feat-text p {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
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
  box-shadow: 0 10px 30px rgba(0, 85, 255, 0.3);
  transition: all 0.3s ease;
}

.btn-service-action:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px rgba(0, 85, 255, 0.4);
}

.service-img-glass-wrapper {
  position: relative;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 40px 100px rgba(0, 0, 0, 0.5);
}

.service-img-glass-wrapper::before {
  content: '';
  position: absolute;
  top: -2px; left: -2px; right: -2px; bottom: -2px;
  background: linear-gradient(135deg, rgba(0, 140, 255, 0.5), transparent, rgba(255, 255, 255, 0.1));
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
  background: rgba(9, 11, 20, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 1rem 1.5rem;
  border-radius: 100px;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
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
  color: #ffffff;
}

/* Timeline */
.cybkart-method-section {
  padding: 8rem 0;
  background: linear-gradient(180deg, #090b14, #05060a);
}

.method-header {
  text-align: center;
  margin-bottom: 5rem;
}

.method-title {
  font-family: var(--font-heading);
  font-size: 3rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 1rem;
}

.method-lead {
  font-size: 1.15rem;
  color: rgba(255, 255, 255, 0.6);
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
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  padding: 2.5rem;
  border-radius: 24px;
  transition: all 0.4s ease;
}

.method-step:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(0, 140, 255, 0.3);
  transform: translateX(10px);
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
  box-shadow: 0 0 15px rgba(0, 85, 255, 0.6);
}

.step-line {
  position: absolute;
  left: -33px;
  top: -2rem;
  bottom: -2rem;
  width: 2px;
  background: rgba(255, 255, 255, 0.1);
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
  color: #ffffff;
  margin-bottom: 0.5rem;
}

.step-content p {
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.6;
  font-size: 0.95rem;
}

/* Dark Table Styles */
.dark-table-wrap {
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.dark-table th {
  color: #ffffff !important;
}

.dark-table .feat-column {
  color: #ffffff !important;
}

.dark-table .cyb-column {
  background: rgba(0, 140, 255, 0.05) !important;
  color: #00bfff !important;
}

.dark-table .legacy-column {
  color: rgba(255, 255, 255, 0.4) !important;
}

.dark-table th, .dark-table td {
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
}

.services-comparison-section {
  padding-bottom: 6rem;
}
"""

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Remove the old section content
start_tag = '<section id="view-services" class="page-view active">'
end_tag = '</section>'
start_idx = content.find(start_tag)
end_idx = content.find(end_tag, start_idx) + len(end_tag)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_services_html + content[end_idx:]
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced services.html content.")
else:
    print("Could not find section boundaries in services.html")

# Append new CSS to combined.css
with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(new_css)
print("Appended new CSS to combined.css")
