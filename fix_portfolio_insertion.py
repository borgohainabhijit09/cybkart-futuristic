import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We need to locate the mega-menu block where the accidental items were inserted
# and delete them.
# The accidental items started with "<!-- Project 5: Landscaping (Standard) -->" 
# and ended right before the closing </nav> tag.

# Find the start of Project 5
proj5_start = content.find('            <!-- Project 5:')
if proj5_start != -1:
    # Find the closing </nav> tag, which is shortly after these items
    nav_end = content.find('    </nav>', proj5_start)
    if nav_end != -1:
        # We want to keep everything up to proj5_start
        # And we need to make sure the mega-menu still closes properly
        # The mega-menu structure originally had:
        #           </div>
        #         </div>
        #       </div>
        #     </nav>
        
        # We will just replace everything from proj5_start up to nav_end
        # with the correct closing tags for the mega menu.
        correct_closing = '          </div>\n        </div>\n      </div>\n'
        content = content[:proj5_start] + correct_closing + content[nav_end:]
        print("Removed accidental items from the navbar.")

# 2. Now insert Projects 5-12 at the CORRECT location.
projects_5_to_12 = """
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

# The correct insertion point is right after Project 4.
# We will look for "<!-- Project 4:" and then find the closing </div> of that project card.
proj4_start = content.find('<!-- Project 4: Restaurant')
if proj4_start != -1:
    # We need to find the end of this project's div.
    # We know the HTML structure:
    #                 <a href="contact.html" class="bento-btn">View Case Study ↗</a>
    #               </div>
    #             </div>
    
    insert_marker = '                <a href="contact.html" class="bento-btn">View Case Study ↗</a>\n              </div>\n            </div>'
    idx = content.find(insert_marker, proj4_start)
    if idx != -1:
        insertion_index = idx + len(insert_marker)
        content = content[:insertion_index] + '\n' + projects_5_to_12 + content[insertion_index:]
        
        with open('portfolio.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully inserted items into the correct grid location.")
    else:
        print("Could not find the end of Project 4.")
else:
    print("Could not find Project 4.")

