import os
import re

new_portfolio_items = """
            <!-- Project 5: Landscaping (Standard) -->
            <div class="bento-project-card">
              <img src="portfolio-landscaping.png" alt="Luxury Landscaping" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">LUXURY OUTDOORS</span>
                </div>
                <h3 class="bento-title">Verdant Hardscapes</h3>
                <p class="bento-desc">Premium outdoor design portfolio generating high-ticket leads organically.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">+210%</span>
                    <span class="stat-lbl">Inquiries</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 6: HVAC (Standard) -->
            <div class="bento-project-card">
              <img src="portfolio-hvac.png" alt="Commercial HVAC" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">COMMERCIAL HVAC</span>
                </div>
                <h3 class="bento-title">AeroTech Climate</h3>
                <p class="bento-desc">High-speed emergency booking funnel designed for rapid dispatch.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">3x</span>
                    <span class="stat-lbl">Conversions</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>
            
            <!-- Project 7: Real Estate (Large Span) -->
            <div class="bento-project-card bento-large">
              <img src="portfolio-realestate.png" alt="Luxury Real Estate" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">PREMIUM REAL ESTATE</span>
                  <span class="meta-year">2026</span>
                </div>
                <h3 class="bento-title">Vanguard Properties</h3>
                <p class="bento-desc">An immersive property listing platform featuring seamless video integration, dynamic sorting, and automated agent routing for high-net-worth buyers.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">#1</span>
                    <span class="stat-lbl">Market Search</span>
                  </div>
                  <div class="stat-box">
                    <span class="stat-val">+120%</span>
                    <span class="stat-lbl">Showing Requests</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>

            <!-- Project 8: Law Firm (Large Span, Reverse) -->
            <div class="bento-project-card bento-large reverse-content">
              <img src="portfolio-lawfirm.png" alt="Corporate Law Firm" class="bento-bg-img">
              <div class="bento-overlay-gradient"></div>
              
              <div class="bento-content">
                <div class="bento-meta">
                  <span class="meta-tag">CORPORATE LEGAL</span>
                  <span class="meta-year">2025</span>
                </div>
                <h3 class="bento-title">Sterling & Associates</h3>
                <p class="bento-desc">A highly authoritative, trust-building web presence engineered to rank for competitive corporate litigation terms and secure retained clients.</p>
                
                <div class="bento-stats">
                  <div class="stat-box">
                    <span class="stat-val">4.5x</span>
                    <span class="stat-lbl">Organic Traffic</span>
                  </div>
                  <div class="stat-box">
                    <span class="stat-val">+60%</span>
                    <span class="stat-lbl">Retainers</span>
                  </div>
                </div>
                <a href="contact.html" class="bento-btn">View Case Study ↗</a>
              </div>
            </div>
"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert this right before `</div> <!-- End of .portfolio-bento-grid -->`
# Let's find the closing div of portfolio-bento-grid
marker = '          </div>\n        </div>\n      </div>'
idx = content.find(marker)

if idx != -1:
    content = content[:idx] + new_portfolio_items + content[idx:]
    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added new items to portfolio grid.")
else:
    print("Could not find insertion point.")
