import re
import os

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the NUCLEAR OPTION
pattern = r'<style>\s*/\*\s*NUCLEAR OPTION TO FIX INVISIBLE TEXT.*?</style>\s*'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# 2. Build the new Pricing Grid
new_pricing_grid = """
        <!-- NEW 4-COLUMN PRICING GRID -->
        <div class="pricing-grid-4">
          <!-- Tier 1: Starter -->
          <div class="pricing-card glass-card">
            <div class="pricing-badge-wrap">Starter</div>
            <h3 class="pricing-tier-title">For Small Businesses</h3>
            <div class="pricing-rate">
              <div class="first-month-label">$0 / First Month</div>
              <div class="rate-price-row">
                <span class="rate-currency">$</span><span class="rate-price">49</span><span class="rate-period">/mo</span>
              </div>
            </div>
            <ul class="pricing-bullet-list">
              <li>3–5 Pages</li>
              <li>Template-Based Design</li>
              <li>Mobile Optimized</li>
              <li>Hosting Included</li>
              <li>Basic Support</li>
            </ul>
            <a href="contact.html" class="btn-secondary rate-cta">Get Started</a>
          </div>

          <!-- Tier 2: Growth -->
          <div class="pricing-card glass-card highlighted">
            <div class="card-glow-edge"></div>
            <div class="pricing-badge-wrap" style="background: linear-gradient(135deg, #0055ff, #00bfff); color: #fff;">MOST POPULAR</div>
            <h3 class="pricing-tier-title">Growth</h3>
            <div class="pricing-rate">
              <div class="first-month-label highlight-label">$0 / First Month</div>
              <div class="rate-price-row">
                <span class="rate-currency">$</span><span class="rate-price">69</span><span class="rate-period">/mo</span>
              </div>
            </div>
            <ul class="pricing-bullet-list">
              <li>5–10 Pages</li>
              <li>Custom Design Edits</li>
              <li>Mobile Optimized</li>
              <li>SEO-Ready Structure</li>
              <li>Hosting & Maintenance</li>
              <li>Ongoing Updates</li>
              <li>Priority Support</li>
            </ul>
            <a href="contact.html" class="btn-primary rate-cta">Scale Now</a>
          </div>

          <!-- Tier 3: Pro -->
          <div class="pricing-card glass-card">
            <div class="pricing-badge-wrap">Pro</div>
            <h3 class="pricing-tier-title">For Growing Brands</h3>
            <div class="pricing-rate">
              <div class="first-month-label">$0 / First Month</div>
              <div class="rate-price-row">
                <span class="rate-currency">$</span><span class="rate-price">99</span><span class="rate-period">/mo</span>
              </div>
            </div>
            <ul class="pricing-bullet-list">
              <li>Fully Custom Design</li>
              <li>Advanced UI/UX</li>
              <li>Speed Optimization</li>
              <li>Form & CRM Integration</li>
              <li>Monthly Improvements</li>
              <li>Priority Support</li>
            </ul>
            <a href="contact.html" class="btn-secondary rate-cta">Go Pro</a>
          </div>

          <!-- Tier 4: Elite -->
          <div class="pricing-card glass-card">
            <div class="pricing-badge-wrap">Elite</div>
            <h3 class="pricing-tier-title">For Scaling Businesses</h3>
            <div class="pricing-rate">
              <div class="first-month-label">$0 / First Month</div>
              <div class="rate-price-row">
                <span class="rate-currency">$</span><span class="rate-price">149</span><span class="rate-period">/mo</span>
              </div>
            </div>
            <ul class="pricing-bullet-list">
              <li>Everything in Pro</li>
              <li>AI Automation Integration</li>
              <li>Lead Generation Systems</li>
              <li>Conversion Optimization</li>
              <li>Monthly Strategy Support</li>
            </ul>
            <a href="contact.html" class="btn-secondary rate-cta">Join Elite</a>
          </div>
        </div>
"""

# Replace the old `<div class="pricing-grid">` with our new one
# The old block ends right before `</div>\n    </section>`

start_marker = '<div class="pricing-grid">'
start_idx = content.find(start_marker)

end_marker = '        </div>\n      </div>\n    </section>'
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Remove the toggle wrapper too, since these packages are monthly only?
    # The prompt doesn't mention annual. Let's remove the toggle wrap.
    toggle_start = content.rfind('<div class="pricing-toggle-wrap">', 0, start_idx)
    if toggle_start != -1:
        start_idx = toggle_start
    
    content = content[:start_idx] + new_pricing_grid + content[end_idx:]
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced pricing grid successfully.")
else:
    print("Could not find the pricing grid section.")

# 3. Append CSS for pricing-grid-4
new_css = """
/* ==========================================================================
   4-COLUMN PRICING GRID STYLES (LIGHT LUXURY)
   ========================================================================== */
.pricing-grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

@media (max-width: 1280px) {
  .pricing-grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .pricing-grid-4 {
    grid-template-columns: 1fr;
  }
}

.pricing-grid-4 .pricing-card {
  padding: 2.5rem 1.5rem;
  display: flex;
  flex-direction: column;
  position: relative;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(9, 11, 20, 0.05);
  border-radius: 24px;
  box-shadow: 0 20px 40px rgba(9, 11, 20, 0.02);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.pricing-grid-4 .pricing-card.highlighted {
  background: #ffffff;
  border-color: rgba(0, 85, 255, 0.2);
  box-shadow: 0 30px 60px rgba(0, 85, 255, 0.1);
  transform: translateY(-10px);
}

.pricing-grid-4 .pricing-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 30px 60px rgba(9, 11, 20, 0.05);
}

.pricing-grid-4 .pricing-card.highlighted:hover {
  transform: translateY(-15px);
  box-shadow: 0 40px 80px rgba(0, 85, 255, 0.15);
}

.first-month-label {
  font-size: 1rem;
  font-weight: 700;
  color: #0b0f19;
  opacity: 0.6;
  margin-bottom: 0.2rem;
}

.highlight-label {
  color: #0055ff;
  opacity: 1;
}

.rate-price-row {
  display: flex;
  align-items: baseline;
  justify-content: center;
  margin-bottom: 2rem;
}

.pricing-grid-4 .rate-price {
  font-family: var(--font-heading);
  font-size: 4rem;
  font-weight: 800;
  color: #0b0f19;
  line-height: 1;
}

.pricing-grid-4 .rate-currency {
  font-size: 1.5rem;
  font-weight: 600;
  color: #0b0f19;
  opacity: 0.6;
  margin-right: 0.2rem;
}

.pricing-grid-4 .rate-period {
  font-size: 1rem;
  color: #64748b;
  margin-left: 0.2rem;
}

.pricing-grid-4 .pricing-tier-title {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 700;
  color: #0b0f19;
  text-align: center;
  margin-bottom: 1.5rem;
  height: 3rem; /* Align titles */
}

.pricing-grid-4 .pricing-badge-wrap {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(9, 11, 20, 0.05);
  color: #0b0f19;
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 0.05em;
  padding: 0.4rem 1.2rem;
  border-radius: 100px;
  border: 1px solid rgba(9, 11, 20, 0.1);
  text-transform: uppercase;
}

.pricing-grid-4 .pricing-bullet-list {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem 0;
  flex: 1;
}

.pricing-grid-4 .pricing-bullet-list li {
  position: relative;
  padding-left: 1.8rem;
  margin-bottom: 1rem;
  font-size: 0.95rem;
  color: #475569;
  line-height: 1.4;
}

.pricing-grid-4 .pricing-bullet-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  top: 0;
  color: #0055ff;
  font-weight: 800;
  font-size: 1.1rem;
}

.pricing-grid-4 .rate-cta {
  width: 100%;
  text-align: center;
  justify-content: center;
  margin-top: auto;
}
"""

with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Appended pricing grid CSS to combined.css")
