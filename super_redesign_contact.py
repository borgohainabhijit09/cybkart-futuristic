import re
import os

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_contact_section = """
    <section id="view-contact" class="page-view active" style="padding-top: 120px; padding-bottom: 80px;">
      <div class="container">
        
        <div class="services-editorial-header" style="justify-content: flex-start; text-align: left; border-bottom: none; margin-bottom: 2rem;">
          <div class="services-eh-left" style="max-width: 800px;">
            <div class="services-eyebrow"><span class="pulse-dot-blue"></span>GLOBAL HEADQUARTERS</div>
            <h2 class="editorial-title" style="font-size: 4.5rem; line-height: 1;">Initialize <br><span class="gradient-text">Deployment.</span></h2>
            <p class="editorial-lead" style="margin-top: 1.5rem; max-width: 600px;">Direct access to our growth systems architects. Request a comprehensive audit, competitor teardown, and bespoke digital scaling plan.</p>
          </div>
        </div>

        <div class="contact-redesign-grid">
          
          <!-- Left side: Cinematic Image & Info -->
          <div class="contact-cinematic-card">
            <img src="contact-hq.png" alt="CybKart Global HQ" class="contact-hq-img">
            <div class="contact-hq-overlay"></div>
            
            <div class="contact-hq-content">
              <div class="hq-pulse-badge">
                <span class="pulse-dot-green"></span>
                SYSTEMS ONLINE
              </div>
              
              <div class="contact-details-list">
                <div class="c-detail-item">
                  <div class="c-detail-icon">🏢</div>
                  <div class="c-detail-text">
                    <span class="c-lbl">Global Headquarters</span>
                    <span class="c-val">1309 Coffeen Ave, Sheridan,<br>Wyoming 82801, USA</span>
                  </div>
                </div>
                
                <div class="c-detail-item">
                  <div class="c-detail-icon">📞</div>
                  <div class="c-detail-text">
                    <span class="c-lbl">Direct Line</span>
                    <a href="tel:8446991255" class="c-val link-hover">844-699-1255</a>
                  </div>
                </div>

                <div class="c-detail-item">
                  <div class="c-detail-icon">✉️</div>
                  <div class="c-detail-text">
                    <span class="c-lbl">Electronic Mail</span>
                    <a href="mailto:info@cybkartglobal.com" class="c-val link-hover">info@cybkartglobal.com</a>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right side: Advanced Form -->
          <div class="contact-form-wrapper luxury-glass-card">
            <h3 class="form-title">Architecture Request Form</h3>
            <p class="form-subtitle">All transmissions are end-to-end encrypted. An architect will respond within 15 minutes.</p>
            
            <form id="growth-contact-form" class="luxury-form" onsubmit="event.preventDefault(); alert('CybKart Lead System Engaged: Our architect will contact you shortly.');">
              <div class="form-row">
                <div class="form-group">
                  <label for="usr-name">Full Name</label>
                  <input type="text" id="usr-name" required placeholder="e.g. Sterling Kahn" class="form-input">
                  <span class="input-glow-border"></span>
                </div>
                <div class="form-group">
                  <label for="usr-company">Business Name</label>
                  <input type="text" id="usr-company" required placeholder="e.g. Kahn Enterprises" class="form-input">
                  <span class="input-glow-border"></span>
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="usr-email">Work Email</label>
                  <input type="email" id="usr-email" required placeholder="name@company.com" class="form-input">
                  <span class="input-glow-border"></span>
                </div>
                <div class="form-group">
                  <label for="usr-phone">Direct Phone</label>
                  <input type="tel" id="usr-phone" placeholder="(555) 000-0000" class="form-input">
                  <span class="input-glow-border"></span>
                </div>
              </div>

              <div class="form-group">
                <label for="usr-industry">Target Objective</label>
                <select id="usr-industry" class="form-input">
                  <option value="complete">Complete Digital Overhaul</option>
                  <option value="leadgen">Automated Lead Generation</option>
                  <option value="seo">Local SEO Domination</option>
                  <option value="crm">CRM & Booking Integration</option>
                  <option value="other">Other System Requirement</option>
                </select>
                <span class="input-glow-border"></span>
              </div>

              <div class="form-group">
                <label for="usr-msg">Project Specifications</label>
                <textarea id="usr-msg" rows="4" placeholder="Detail your current bottlenecks, revenue goals, and infrastructure needs..." class="form-input"></textarea>
                <span class="input-glow-border"></span>
              </div>

              <button type="submit" class="btn-primary form-submit-btn" style="width: 100%; justify-content: center; margin-top: 1rem;">
                <span class="btn-txt">Transmit Request <span class="arrow-icon">↗</span></span>
                <span class="btn-slide-bg"></span>
              </button>
            </form>
          </div>

        </div>
      </div>
    </section>
"""

# Find start and end of current contact section
start_marker = '<section id="view-contact"'
end_marker = '    <!-- ========================================\n         ULTRA-PREMIUM CINEMATIC FOOTER'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_contact_section + '\n    ' + content[end_idx:]
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Redesigned contact section injected.")
else:
    print("Could not find contact bounds.")

# Append CSS styles for the redesign
new_css = """
/* ==========================================================================
   CONTACT REDESIGN STYLES
   ========================================================================== */
.contact-redesign-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-top: 3rem;
  align-items: stretch;
}

@media (max-width: 1024px) {
  .contact-redesign-grid {
    grid-template-columns: 1fr;
  }
}

.contact-cinematic-card {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(9, 11, 20, 0.08);
  min-height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.contact-hq-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.contact-hq-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, rgba(9, 11, 20, 0.95) 0%, rgba(9, 11, 20, 0.4) 50%, rgba(9, 11, 20, 0.1) 100%);
  z-index: 2;
}

.contact-hq-content {
  position: relative;
  z-index: 3;
  padding: 3rem;
  color: #fff;
}

.hq-pulse-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 0.5rem 1rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  border: 1px solid rgba(255, 255, 255, 0.2);
  margin-bottom: 2rem;
}

.pulse-dot-green {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #00ff88;
  box-shadow: 0 0 10px #00ff88, 0 0 20px #00ff88;
  animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
}

.contact-details-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.c-detail-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  padding: 1.25rem;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, background 0.3s ease;
}

.c-detail-item:hover {
  transform: translateX(10px);
  background: rgba(255, 255, 255, 0.1);
}

.c-detail-icon {
  font-size: 1.5rem;
  background: rgba(0, 85, 255, 0.2);
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  border: 1px solid rgba(0, 85, 255, 0.3);
}

.c-detail-text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.c-lbl {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255, 255, 255, 0.6);
  font-weight: 600;
}

.c-val {
  font-size: 1.1rem;
  font-weight: 600;
  color: #ffffff;
  line-height: 1.4;
}

.link-hover:hover {
  color: #00bfff;
}

.contact-form-wrapper {
  padding: 3rem;
}

.form-title {
  font-family: var(--font-heading);
  font-size: 2rem;
  font-weight: 800;
  color: #0b0f19;
  margin-bottom: 0.5rem;
}

.form-subtitle {
  color: #64748b;
  font-size: 1rem;
  margin-bottom: 2rem;
}
"""

with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(new_css)
    
print("Appended new CSS.")
