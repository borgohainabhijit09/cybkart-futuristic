import os

new_portfolio_items = """
            <!-- Project 9: Fitness (Large Span) -->
            <div class="bento-project-card bento-large">
              <img src="portfolio-fitness.png" alt="Elite Fitness Center" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">ELITE FITNESS</span>
                  <span class="meta-year">2026</span>
                </div>
                <h3 class="bento-title">IronCore Athletics</h3>
                <p class="bento-desc">An aggressive, high-conversion membership funnel designed to capture trial sign-ups and personal training leads for a premium gym.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">+150%</span>
                    <span class="stat-lbl">Trial Signups</span>
                  </div>
                  <div class="stat-box">
                    <span class="stat-val">3x</span>
                    <span class="stat-lbl">Member Retention</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 10: E-commerce (Standard) -->
            <div class="bento-project-card">
              <img src="portfolio-ecommerce.png" alt="Luxury E-commerce" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">LUXURY BOUTIQUE</span>
                </div>
                <h3 class="bento-title">Aura Fashion</h3>
                <p class="bento-desc">Sleek, minimalist e-commerce storefront with seamless checkout integration.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">+80%</span>
                    <span class="stat-lbl">Sales Conversion</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>
            
            <!-- Project 11: SaaS (Standard) -->
            <div class="bento-project-card">
              <img src="portfolio-saas.png" alt="Tech Startup SaaS" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">TECH STARTUP</span>
                </div>
                <h3 class="bento-title">Nova Analytics</h3>
                <p class="bento-desc">Futuristic landing page for a SaaS platform designed to drive enterprise demo requests.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">4.5x</span>
                    <span class="stat-lbl">Demo Requests</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 12: Logistics (Large Span, Reverse) -->
            <div class="bento-project-card bento-large reverse-content">
              <img src="portfolio-logistics.png" alt="Global Logistics" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">GLOBAL TRANSPORT</span>
                  <span class="meta-year">2025</span>
                </div>
                <h3 class="bento-title">Velocity Freight</h3>
                <p class="bento-desc">A highly professional, corporate web presence integrating live shipment tracking and automated quote generation.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">+110%</span>
                    <span class="stat-lbl">B2B Leads</span>
                  </div>
                  <div class="stat-box">
                    <span class="stat-val">Sub-300ms</span>
                    <span class="stat-lbl">API Latency</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>
"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert this right before the closing div of the bento grid
# To be safe, we can search for the end of the last bento project card (which was Project 8)
marker = '          </div>\n        </div>\n      </div>'
idx = content.find(marker)

if idx != -1:
    content = content[:idx] + new_portfolio_items + content[idx:]
    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added 4 more items to portfolio grid.")
else:
    print("Could not find insertion point.")
