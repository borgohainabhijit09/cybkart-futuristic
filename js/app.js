/* ==========================================================================
   CYBKART GLOBAL - APP ENTRY & GENERAL SCROLL ANIMATION CORE (app.js)
   ========================================================================== */

// Make sure GSAP plugins are registered globally
gsap.registerPlugin(ScrollTrigger);

// Ensure all heading and badge elements are visible on page load
// This prevents GSAP animations from leaving elements invisible if JS is slow
gsap.set('.section-title, .eyebrow-badge, h1, h2, h3', { opacity: 1 });

// Global state variables
export let lenis;

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initLenis();
  initNavbarScroll();
  initNavbarMagneticUnderline();
  initNavbarMegaMenu();
  initSectionRevealAnimations();
  initHomepageSectionScrollAnimations();
  initIndustryTabs();
  initPricingToggle();
  initHeroMockupTilt();
  initMilestonesReveal();
  initHeroCanvas();
});

/* 1. Preloader — brand-first, fast (≈1s), never gets stuck */
function initPreloader() {
  const preloader = document.getElementById('preloader');
  if (!preloader) return;

  // Hard failsafe — if something goes wrong, force-dismiss after 3s max
  const FAILSAFE = setTimeout(() => dismissPreloader(preloader), 3000);

  const barFill  = document.getElementById('pl-bar-fill');
  const pctEl    = document.getElementById('pl-pct');

  // Animate the wordmark in from below right away
  const wordmark = preloader.querySelector('.pl-wordmark');
  const tagline  = preloader.querySelector('.pl-tagline');
  if (wordmark) gsap.fromTo(wordmark, { y: 24, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: 'power3.out' });
  if (tagline)  gsap.fromTo(tagline,  { y: 12, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: 'power3.out', delay: 0.15 });

  // Count 0→100 in 0.9s, update bar + percentage
  const obj = { val: 0 };
  gsap.to(obj, {
    val: 100,
    duration: 0.9,
    ease: 'power2.inOut',
    onUpdate() {
      const p = Math.floor(obj.val);
      if (pctEl)   pctEl.textContent   = `${p}%`;
      if (barFill) barFill.style.width = `${p}%`;
    },
    onComplete() {
      clearTimeout(FAILSAFE);
      // Brief pause at 100%, then dismiss
      setTimeout(() => dismissPreloader(preloader), 120);
    }
  });
}

function dismissPreloader(preloader) {
  if (!preloader || preloader.style.display === 'none') return;
  gsap.to(preloader, {
    opacity: 0,
    y: '-6%',
    duration: 0.55,
    ease: 'power3.inOut',
    onComplete: () => {
      preloader.style.display = 'none';
      document.body.classList.add('loaded');
      triggerHeroReveal();
      setTimeout(() => ScrollTrigger.refresh(), 200);
    }
  });
}


/* 2. Hero entrance staggered text reveals */
function triggerHeroReveal() {
  const tl = gsap.timeline({ defaults: { ease: 'power4.out' } });

  // 1. Eyebrow pill fades in
  tl.to('#hero-eyebrow', {
    opacity: 1,
    y: 0,
    duration: 0.9,
  });

  // 2. Title lines burst up one by one
  const lineInners = document.querySelectorAll('.hero-title .line-inner');
  if (lineInners.length) {
    tl.to(lineInners, {
      opacity: 1,
      y: '0%',
      duration: 1.1,
      stagger: 0.12,
      ease: 'power3.out',
    }, '-=0.5');
  }

  // 3. Subtitle fades up
  tl.to('#hero-subtitle', {
    opacity: 1,
    y: 0,
    duration: 0.9,
  }, '-=0.7');

  // 4. CTA buttons
  tl.to('#hero-actions', {
    opacity: 1,
    y: 0,
    duration: 0.8,
  }, '-=0.65');

  // 5. Stats row
  tl.to('#hero-stats', {
    opacity: 1,
    y: 0,
    duration: 0.8,
  }, '-=0.55');

  // 6. Right visual panel rises in from right
  tl.to('#hero-visual', {
    opacity: 1,
    y: 0,
    x: 0,
    duration: 1.3,
    ease: 'power3.out',
  }, '-=0.5');

  // 7. Counter animations for stats
  tl.add(() => {
    document.querySelectorAll('.count-num').forEach(el => {
      const target = parseInt(el.dataset.target, 10);
      const obj = { val: 0 };
      gsap.to(obj, {
        val: target,
        duration: 2,
        ease: 'power2.out',
        onUpdate: () => {
          el.textContent = Math.floor(obj.val);
        }
      });
    });

    // Animate the performance speed bar to 99%
    const speedBar = document.getElementById('speed-bar-fill');
    if (speedBar) {
      gsap.to(speedBar, {
        width: '99%',
        duration: 2,
        ease: 'power2.out',
        delay: 0.3,
      });
    }
  }, '-=0.8');
}


/* 3. Lenis Smooth Scrolling Engine Setup */
function initLenis() {
  if (typeof Lenis === 'undefined') return;

  lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // Buttery easeOutQuad/Quart
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1,
    smoothTouch: false, // Touch devices use native momentum
    touchMultiplier: 2,
    infinite: false,
  });

  // Sync scroll events with GSAP ScrollTrigger
  lenis.on('scroll', ScrollTrigger.update);

  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });

  gsap.ticker.lagSmoothing(0);
}

/* 4. Navbar shrink and border-reveal logic on scroll */
function initNavbarScroll() {
  const navbar = document.getElementById('luxury-navbar');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
}

/* 5. Capsule Floating Navbar Active Underline sliding tracker */
function initNavbarMagneticUnderline() {
  const underline = document.getElementById('nav-underline');
  const links = document.querySelectorAll('.nav-link');
  const activeLink = document.querySelector('.nav-link.active');

  if (!underline || links.length === 0) return;

  // Function to move underline background
  const moveUnderline = (target) => {
    const rect = target.getBoundingClientRect();
    const containerRect = target.parentElement.getBoundingClientRect();
    
    gsap.to(underline, {
      left: rect.left - containerRect.left,
      width: rect.width,
      duration: 0.45,
      ease: 'power3.out'
    });
  };

  // Set initial position
  if (activeLink) {
    // Small timeout to allow element rect rendering
    setTimeout(() => moveUnderline(activeLink), 100);
  }

  // Hover and leave events
  links.forEach(link => {
    link.addEventListener('mouseenter', (e) => {
      moveUnderline(e.target);
    });

    link.addEventListener('mouseleave', () => {
      const currentActive = document.querySelector('.nav-link.active');
      if (currentActive) {
        moveUnderline(currentActive);
      }
    });
  });

  // Resize listener
  window.addEventListener('resize', () => {
    const currentActive = document.querySelector('.nav-link.active');
    if (currentActive) {
      moveUnderline(currentActive);
    }
  });
}

/* 6. High-end ScrollTrigger reveals for section contents */
function initSectionRevealAnimations() {
  const sections = document.querySelectorAll('.page-view');
  
  sections.forEach(section => {
    if (section.id === 'view-home') return; // Hero has its own trigger

    const header = section.querySelector('.section-header, .services-editorial-header');
    const cards = section.querySelectorAll('.service-card, .ed-service-card, .tool-item, .tool-pill, .portfolio-item, .ed-portfolio-item, .pricing-card');

    if (header) {
      // Header reveal (staggered fade up)
      gsap.from(header.children, {
        scrollTrigger: {
          trigger: header,
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: 30,
        stagger: 0.15,
        duration: 1,
        ease: 'power3.out'
      });
    }

    // Content items reveal (slide and scale up gently)
    if (cards.length > 0) {
      gsap.from(cards, {
        scrollTrigger: {
          trigger: cards[0],
          start: 'top 80%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: 40,
        stagger: 0.12,
        duration: 1.2,
        ease: 'power3.out'
      });
    }
  });
}

/* 7. Premium scroll animations for new homepage sections */
function initHomepageSectionScrollAnimations() {
  // Trust section - fade in logo marquee
  const trustTitle = document.querySelector('.trust-title');
  if (trustTitle) {
    gsap.from(trustTitle, {
      scrollTrigger: {
        trigger: trustTitle,
        start: 'top 85%',
        toggleActions: 'play none none none'
      },
      opacity: 0,
      y: 20,
      duration: 1,
      ease: 'power3.out'
    });
  }

  const logoMarquee = document.querySelector('.logo-marquee');
  if (logoMarquee) {
    gsap.from(logoMarquee, {
      scrollTrigger: {
        trigger: logoMarquee,
        start: 'top 80%',
        toggleActions: 'play none none none'
      },
      opacity: 0,
      y: 30,
      duration: 1.2,
      ease: 'power3.out',
      delay: 0.2
    });
  }

  // CORE CAPABILITIES - Bento Grid
  const bentoHeader = document.querySelector('.bento-capabilities-section .section-header');
  if (bentoHeader) {
    gsap.fromTo(bentoHeader.children, 
      { opacity: 0, y: 30 },
      {
        scrollTrigger: {
          trigger: bentoHeader,
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        opacity: 1,
        y: 0,
        stagger: 0.12,
        duration: 0.9,
        ease: 'power3.out'
      }
    );
  }

  const bentoCards = document.querySelectorAll('.bento-card');
  if (bentoCards.length > 0) {
    const bentoTimeline = gsap.timeline({
      scrollTrigger: {
        trigger: '.bento-grid',
        start: 'top 80%',
        toggleActions: 'play none none none'
      }
    });

    // 1. Reveal bento cards
    bentoTimeline.fromTo(bentoCards,
      { opacity: 0, y: 40, scale: 0.95 },
      {
        opacity: 1,
        y: 0,
        scale: 1,
        stagger: 0.15,
        duration: 1.1,
        ease: 'power3.out'
      }
    );

    // 2. Animate Speed widget fill
    const speedBar = document.getElementById('bento-fill-cyb');
    if (speedBar) {
      bentoTimeline.fromTo(speedBar,
        { width: '0%' },
        {
          width: '98%',
          duration: 1.2,
          ease: 'power3.out'
        },
        '-=0.6'
      );
    }

    // 3. Animate SEO rank list
    const rankItems = document.querySelectorAll('.bento-rank-item');
    if (rankItems.length > 0) {
      bentoTimeline.fromTo(rankItems,
        { opacity: 0, x: -20 },
        {
          opacity: 1,
          x: 0,
          stagger: 0.2,
          duration: 0.8,
          ease: 'power2.out'
        },
        '-=0.8'
      );
    }

    // 4. Animate Lead SMS bubbles
    const smsBubbles = document.querySelectorAll('.bento-sms-bubble');
    if (smsBubbles.length > 0) {
      bentoTimeline.fromTo(smsBubbles,
        { opacity: 0, y: 15, scale: 0.85 },
        {
          opacity: 1,
          y: 0,
          scale: 1,
          stagger: 0.3,
          duration: 0.6,
          ease: 'back.out(1.5)'
        },
        '-=0.6'
      );
    }
  }

  // ── PORTFOLIO — Pinned Vertical Slider ─────────────────────────────
  const pfSection = document.querySelector('.pf-pin-section');
  const pfTrack = document.querySelector('#pf-track');
  const pfSlides = document.querySelectorAll('.pf-slide');

  if (pfSection && pfTrack && pfSlides.length > 0) {
    const totalSlides = pfSlides.length;

    // DOM Elements for dynamic updates
    const domInd = document.getElementById('pf-industry');
    const domTitle = document.getElementById('pf-proj-title');
    const domTags = document.getElementById('pf-tags');
    const domMetrics = document.getElementById('pf-metrics');
    const domCur = document.getElementById('pf-cur');
    const domProgress = document.getElementById('pf-progress');
    const domTotal = document.getElementById('pf-total');
    
    if (domTotal) domTotal.textContent = String(totalSlides).padStart(2, '0');

    const dotsContainer = document.getElementById('pf-dots');
    let pfDots = [];
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      for (let i = 0; i < totalSlides; i++) {
        const btn = document.createElement('button');
        btn.className = i === 0 ? 'pf-dot active' : 'pf-dot';
        btn.dataset.idx = i;
        btn.setAttribute('aria-label', `Project ${i + 1}`);
        dotsContainer.appendChild(btn);
        pfDots.push(btn);
      }
    } else {
      pfDots = Array.from(document.querySelectorAll('.pf-dot'));
    }

    // Setup matchMedia so pinning only happens on desktop
    let mm = gsap.matchMedia();

    mm.add("(min-width: 992px)", () => {
      // 3D Stacking Initialization
      gsap.set(pfTrack, { perspective: 2000, transformStyle: "preserve-3d" });

      pfSlides.forEach((slide, i) => {
        if (i === 0) {
          gsap.set(slide, { x: 0, z: 0, rotateY: 0, opacity: 1 });
        } else {
          // Push remaining slides back and to the right, angled like Vista Flip 3D
          gsap.set(slide, { 
            x: 120 * i, 
            z: -400 * i, 
            rotateY: -35, 
            opacity: Math.max(0, 1 - (i * 0.2))
          });
        }
      });

      let slideHeight = window.innerHeight;
      let totalScrollHeight = slideHeight * (totalSlides - 1); // how far we scroll to see all

      // Create a master timeline for the scrubbing
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: pfSection,
          start: 'top top',
          end: `+=${totalScrollHeight}`, // Scroll distance
          pin: '.pf-pin-inner',
          scrub: 1, // Smooth scrubbing
          onUpdate: (self) => {
            let progress = self.progress; // 0 to 1
            if (domProgress) domProgress.style.width = `${progress * 100}%`;

            let activeIndex = Math.min(
              totalSlides - 1,
              Math.floor(progress * totalSlides)
            );
            if (progress > 0.95) activeIndex = totalSlides - 1;
            updatePortfolioData(activeIndex);
          }
        }
      });

      // Build the transitions for the timeline
      for (let i = 0; i < totalSlides - 1; i++) {
        let stepTl = gsap.timeline();
        
        pfSlides.forEach((slide, j) => {
          if (j < i) {
            // It already flew off screen, stay there
          } else if (j === i) {
            // Currently active slide flies to the left and towards camera
            stepTl.to(slide, {
              x: -600,
              z: 300,
              rotateY: 25,
              opacity: 0,
              duration: 1,
              ease: 'power2.inOut'
            }, 0);
          } else if (j === i + 1) {
            // The NEXT slide becomes fully active (front & flat)
            stepTl.to(slide, {
              x: 0,
              z: 0,
              rotateY: 0,
              opacity: 1,
              duration: 1,
              ease: 'power2.inOut'
            }, 0);
          } else {
            // Slides further back move up one slot
            const offset = j - (i + 1); // new offset
            stepTl.to(slide, {
              x: 120 * offset,
              z: -400 * offset,
              rotateY: -35,
              opacity: Math.max(0, 1 - (offset * 0.2)),
              duration: 1,
              ease: 'power2.inOut'
            }, 0);
          }
        });
        
        tl.add(stepTl);
      }

      // Click on dots to scroll to that section
      pfDots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
          let scrollTarget = pfSection.offsetTop + (slideHeight * i);
          gsap.to(window, {
            scrollTo: scrollTarget,
            duration: 1,
            ease: "power2.out"
          });
        });
      });

      return () => {
        // Cleanup if needed
      };
    });

    // Helper to update the static left panel
    let currentActiveIdx = -1;
    function updatePortfolioData(idx) {
      if (idx === currentActiveIdx) return;
      currentActiveIdx = idx;

      // Update Slides 'active' class for browser popup animation
      pfSlides.forEach((s, i) => s.classList.toggle('is-active', i === idx));

      // Update dots
      pfDots.forEach((d, i) => d.classList.toggle('active', i === idx));

      // Update Counter
      if (domCur) domCur.textContent = String(idx + 1).padStart(2, '0');

      // Get Data from active slide
      const slide = pfSlides[idx];
      if (!slide) return;

      const ind = slide.dataset.industry;
      const title = slide.dataset.title;
      const tags = slide.dataset.tags.split(',');
      const m1Val = slide.dataset.m1Val;
      const m1Lbl = slide.dataset.m1Label;
      const m2Val = slide.dataset.m2Val;
      const m2Lbl = slide.dataset.m2Label;

      // Animate text changes
      gsap.to([domInd, domTitle, domTags, domMetrics], {
        opacity: 0,
        y: -10,
        duration: 0.2,
        onComplete: () => {
          if (domInd) domInd.textContent = ind;
          if (domTitle) domTitle.textContent = title;
          
          if (domTags) {
            domTags.innerHTML = tags.map(t => `<span>${t.trim()}</span>`).join('');
          }
          
          if (domMetrics) {
            domMetrics.innerHTML = `
              <div class="pf-metric"><span class="pf-metric-val">${m1Val}</span><span class="pf-metric-label">${m1Lbl}</span></div>
              <div class="pf-metric"><span class="pf-metric-val">${m2Val}</span><span class="pf-metric-label">${m2Lbl}</span></div>
            `;
          }

          gsap.to([domInd, domTitle, domTags, domMetrics], {
            opacity: 1,
            y: 0,
            duration: 0.3,
            stagger: 0.05
          });
        }
      });
    }

    // Initialize first slide on load
    updatePortfolioData(0);
  }


  // THE CYBKART METHOD WORKFLOW (ANIMATED FLOWCHART)
  const workflowSection = document.querySelector('.workflow-section');
  if (workflowSection) {
    // Header Animation
    const workflowHeader = workflowSection.querySelector('.section-header');
    if (workflowHeader) {
      gsap.from(workflowHeader.children, {
        scrollTrigger: {
          trigger: workflowHeader,
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: 30,
        stagger: 0.1,
        duration: 0.9,
        ease: 'power3.out'
      });
    }

    const flowLineFill = document.getElementById('flow-line-fill');
    const flowSteps = document.querySelectorAll('.flow-step');
    
    if (flowLineFill && flowSteps.length > 0) {
      let mmWorkflow = gsap.matchMedia();

      // Desktop: Horizontal Line Fill
      mmWorkflow.add("(min-width: 992px)", () => {
        gsap.to(flowLineFill, {
          scrollTrigger: {
            trigger: '.workflow-flowchart',
            start: 'top 60%',
            end: 'bottom 40%',
            scrub: 1
          },
          width: '100%',
          ease: 'none'
        });
      });

      // Mobile: Vertical Line Fill
      mmWorkflow.add("(max-width: 991px)", () => {
        gsap.to(flowLineFill, {
          scrollTrigger: {
            trigger: '.workflow-flowchart',
            start: 'top 70%',
            end: 'bottom 60%',
            scrub: 1
          },
          height: '100%',
          ease: 'none'
        });
      });

      // Active State for Nodes
      flowSteps.forEach((step) => {
        ScrollTrigger.create({
          trigger: step,
          start: 'top 75%',
          toggleClass: 'active'
        });
      });
    }
  }

  // REVIEWS SECTION ANIMATION
  const reviewsSection = document.querySelector('.reviews-section');
  if (reviewsSection) {
    const reviewsHeader = reviewsSection.querySelector('.section-header');
    if (reviewsHeader) {
      gsap.from(reviewsHeader.children, {
        scrollTrigger: {
          trigger: reviewsHeader,
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: 30,
        stagger: 0.1,
        duration: 0.9,
        ease: 'power3.out'
      });
    }

    const sliderContainer = document.querySelector('.reviews-slider-container');
    if (sliderContainer) {
      gsap.from(sliderContainer, {
        scrollTrigger: {
          trigger: sliderContainer,
          start: 'top 80%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: 50,
        duration: 1,
        ease: 'power3.out'
      });
    }
  }

  // Parallax effect for portfolio visual badges
  document.querySelectorAll('.portfolio-visual-badge').forEach(badge => {
    gsap.to(badge, {
      scrollTrigger: {
        trigger: badge.closest('.portfolio-card'),
        start: 'top bottom',
        end: 'bottom top',
        scrub: 0.5
      },
      y: -15,
      opacity: 0.7,
      ease: 'none'
    });
  });

  // Parallax tilt effect for service cards
  document.querySelectorAll('.service-card-home').forEach((card, idx) => {
    gsap.to(card, {
      scrollTrigger: {
        trigger: card,
        start: 'center bottom',
        end: 'center center',
        scrub: 1
      },
      rotation: idx % 2 === 0 ? 1 : -1,
      opacity: 1,
      ease: 'none'
    });
  });

  // Benefit cards staggered parallax
  document.querySelectorAll('.benefit-card').forEach((card, idx) => {
    gsap.to(card, {
      scrollTrigger: {
        trigger: card,
        start: 'top 75%',
        end: 'center 50%',
        scrub: 0.6
      },
      y: -20 + (idx % 2) * 40,
      ease: 'none'
    });
  });
}

/* 7. Industry tabs panel interactions */
function initIndustryTabs() {
  const tabs = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.tab-panel');

  if (tabs.length === 0 || panels.length === 0) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.tab;

      // Reset active tabs
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      // Swap active panels with fade animation
      panels.forEach(panel => {
        if (panel.id === `tab-${target}`) {
          panel.style.display = 'block';
          setTimeout(() => {
            panel.classList.add('active');
          }, 50);
        } else {
          panel.classList.remove('active');
          panel.style.display = 'none';
        }
      });
    });
  });
}

/* 8. Pricing Toggles (Monthly / Annual rate rates swaps) */
function initPricingToggle() {
  const btn = document.getElementById('pricing-toggle');
  const monthlyLabel = document.getElementById('lbl-monthly');
  const annualLabel = document.getElementById('lbl-annual');
  const rateTexts = document.querySelectorAll('.rate-price');

  if (!btn || !rateTexts.length) return;

  btn.addEventListener('click', () => {
    const isAnnual = btn.classList.toggle('active');

    if (isAnnual) {
      monthlyLabel.classList.remove('active');
      annualLabel.classList.add('active');
    } else {
      monthlyLabel.classList.add('active');
      annualLabel.classList.remove('active');
    }

    // GSAP numeric stagger count transition for price values
    rateTexts.forEach(rate => {
      const targetPrice = isAnnual ? rate.dataset.annual : rate.dataset.monthly;
      const obj = { val: parseFloat(rate.textContent.replace(',', '')) };
      
      gsap.to(obj, {
        val: parseFloat(targetPrice.replace(',', '')),
        duration: 0.6,
        ease: 'power3.out',
        onUpdate: () => {
          // Format number with commas
          rate.textContent = Math.floor(obj.val).toLocaleString();
        }
      });
    });
  });
}

/* 9. Floating navbar services mega-menu dropdown interactions */
function initNavbarMegaMenu() {
  const trigger = document.getElementById('nav-services-trigger');
  const megaMenu = document.getElementById('services-mega-menu');

  if (!trigger || !megaMenu) return;

  let timeoutId = null;

  const showMenu = () => {
    clearTimeout(timeoutId);
    megaMenu.classList.add('active');
    trigger.classList.add('dropdown-active');
  };

  const hideMenu = () => {
    // 150ms buffer window so that the cursor can glide seamlessly between navbar and dropdown card
    timeoutId = setTimeout(() => {
      megaMenu.classList.remove('active');
      trigger.classList.remove('dropdown-active');
    }, 150);
  };

  // Bind mouse listeners for responsive, delay-buffered hover action
  trigger.addEventListener('mouseenter', showMenu);
  trigger.addEventListener('mouseleave', hideMenu);

  megaMenu.addEventListener('mouseenter', showMenu);
  megaMenu.addEventListener('mouseleave', hideMenu);

  // Close mega menu immediately when any sub-link is clicked to enhance SPA cinematic transition feel
  const megaSubLinks = megaMenu.querySelectorAll('a[data-view]');
  megaSubLinks.forEach(link => {
    link.addEventListener('click', () => {
      megaMenu.classList.remove('active');
      trigger.classList.remove('dropdown-active');
    });
  });
}

/* 10. Hero Browser Mockup 3D Parallax Tilt on Mouse Move */
function initHeroMockupTilt() {
  const stage = document.getElementById('hero-visual');
  const mockup = document.querySelector('.hero-browser-mockup');

  if (!stage || !mockup) return;

  const MAX_TILT   = 8;   // degrees
  const MAX_SHIFT  = 6;   // px for float cards parallax

  let targetRX = 0, targetRY = 0;
  let currentRX = 0, currentRY = 0;
  let rafId = null;

  stage.addEventListener('mousemove', (e) => {
    const rect = stage.getBoundingClientRect();
    const cx = rect.left + rect.width  / 2;
    const cy = rect.top  + rect.height / 2;
    // Normalised -1 → 1
    const nx = (e.clientX - cx) / (rect.width  / 2);
    const ny = (e.clientY - cy) / (rect.height / 2);

    targetRY =  nx * MAX_TILT;
    targetRX = -ny * MAX_TILT;

    // Float card subtle counter-parallax
    document.querySelectorAll('.hero-float-card').forEach(card => {
      gsap.to(card, {
        x: -nx * MAX_SHIFT,
        y: -ny * MAX_SHIFT,
        duration: 1,
        ease: 'power2.out',
        overwrite: 'auto',
      });
    });

    if (!rafId) {
      rafId = requestAnimationFrame(animateTilt);
    }
  });

  stage.addEventListener('mouseleave', () => {
    targetRX = 0;
    targetRY = 0;
    document.querySelectorAll('.hero-float-card').forEach(card => {
      gsap.to(card, { x: 0, y: 0, duration: 1.2, ease: 'power3.out', overwrite: 'auto' });
    });
  });

  function animateTilt() {
    // Lerp towards target
    currentRX += (targetRX - currentRX) * 0.08;
    currentRY += (targetRY - currentRY) * 0.08;

    gsap.set(mockup, {
      rotationX: currentRX,
      rotationY: currentRY,
      transformPerspective: 1200,
      transformOrigin: 'center center',
    });

    // Keep looping only while values haven't settled
    if (Math.abs(targetRX - currentRX) > 0.01 || Math.abs(targetRY - currentRY) > 0.01) {
      rafId = requestAnimationFrame(animateTilt);
    } else {
      rafId = null;
    }
  }
}

/* 11. Milestones strip IntersectionObserver reveal */
function initMilestonesReveal() {
  const strip = document.querySelector('.milestones-strip');
  if (!strip) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          strip.classList.add('strip-revealed');
          observer.unobserve(strip); // fire once
        }
      });
    },
    { threshold: 0.25 }
  );

  observer.observe(strip);
}

/* 12. Hero Canvas Particle Constellation Field */
function initHeroCanvas() {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let W, H;

  const resize = () => {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  };
  resize();
  window.addEventListener('resize', resize);

  const COUNT    = 60;
  const MAX_DIST = 145;
  const particles = [];

  for (let i = 0; i < COUNT; i++) {
    particles.push({
      x:  Math.random() * (W || 1200),
      y:  Math.random() * (H || 800),
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      r:  Math.random() * 1.3 + 0.4,
      a:  Math.random() * 0.35 + 0.15,
    });
  }

  let mX = -9999, mY = -9999;
  const hero = document.getElementById('hero');
  if (hero) {
    hero.addEventListener('mousemove', e => {
      const r = canvas.getBoundingClientRect();
      mX = e.clientX - r.left;
      mY = e.clientY - r.top;
    });
    hero.addEventListener('mouseleave', () => { mX = -9999; mY = -9999; });
  }

  const draw = () => {
    ctx.clearRect(0, 0, W, H);

    for (const p of particles) {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) p.x = W;
      if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H;
      if (p.y > H) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(59, 158, 255, ${p.a})`;
      ctx.fill();
    }

    // Connections between close particles
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const d  = Math.sqrt(dx * dx + dy * dy);
        if (d < MAX_DIST) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(59, 158, 255, ${(1 - d / MAX_DIST) * 0.11})`;
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }

      // Mouse proximity: draw a line from the particle to the cursor
      if (mX > 0) {
        const dx = particles[i].x - mX;
        const dy = particles[i].y - mY;
        const d  = Math.sqrt(dx * dx + dy * dy);
        if (d < MAX_DIST * 1.6) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(mX, mY);
          ctx.strokeStyle = `rgba(0, 212, 255, ${(1 - d / (MAX_DIST * 1.6)) * 0.22})`;
          ctx.lineWidth = 0.7;
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(draw);
  };

  draw();
}




// ==========================================================================
// CYBKART ADVANCED AI ASSISTANT (HYBRID ENGINE)
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  const chatWidget = document.querySelector('.floating-chat-widget');
  const chatBotUI = document.getElementById('ai-chatbot');
  const chatCloseBtn = document.getElementById('chatbot-close-btn');
  const chatForm = document.getElementById('chatbot-form');
  const chatInput = document.getElementById('chatbot-input');
  const chatMessages = document.getElementById('chatbot-messages');

  // Insert your OpenAI API Key here for true AI capabilities
  // Note: In production, route this through your backend to protect the key.
  const OPENAI_API_KEY = ""; 

  // Conversation Memory System
  let conversationHistory = [];
  let userContext = {
    industry: null,
    servicesDiscussed: [],
    pricingDiscussed: false,
    objectionsHandled: []
  };

  if (chatWidget && chatBotUI) {
    chatWidget.addEventListener('click', () => {
      chatBotUI.classList.add('active');
      if (conversationHistory.length === 0) {
        initiateGreeting();
      }
    });

    chatCloseBtn.addEventListener('click', () => {
      chatBotUI.classList.remove('active');
    });

    const formatTime = () => {
      const now = new Date();
      return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    };

    const addMessageToUI = (text, sender, isHTML = false) => {
      const msgDiv = document.createElement('div');
      msgDiv.className = `chat-message ${sender}-message`;
      
      const contentDiv = document.createElement('div');
      contentDiv.className = 'message-content';
      if (isHTML) {
        contentDiv.innerHTML = text;
      } else {
        contentDiv.textContent = text;
      }

      const timeDiv = document.createElement('div');
      timeDiv.className = 'message-time';
      timeDiv.textContent = formatTime();

      msgDiv.appendChild(contentDiv);
      msgDiv.appendChild(timeDiv);
      chatMessages.appendChild(msgDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      
      return contentDiv;
    };

    const showTypingIndicator = () => {
      const typingDiv = document.createElement('div');
      typingDiv.className = 'chat-message bot-message typing-indicator-msg';
      typingDiv.innerHTML = `
        <div class="message-content" style="padding: 0.6rem 1rem;">
          <div class="typing-indicator">
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
          </div>
        </div>
      `;
      chatMessages.appendChild(typingDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      return typingDiv;
    };

    const initiateGreeting = () => {
      const typing = showTypingIndicator();
      setTimeout(() => {
        typing.remove();
        addMessageToUI("Hello! I'm the CybKart digital growth consultant. Are you looking to upgrade your current digital presence, or building something entirely new today?", 'bot');
        conversationHistory.push({ role: 'assistant', content: "Hello! I'm the CybKart digital growth consultant. Are you looking to upgrade your current digital presence, or building something entirely new today?" });
      }, 1000);
    };

    const simulateStreamingText = (element, text, speed = 15, onComplete) => {
      element.innerHTML = '';
      let i = 0;
      // Handle HTML tags properly during streaming
      const isHTML = text.includes('<');
      if (isHTML) {
        // If it's HTML, we just fade it in smoothly instead of typing letter by letter to prevent broken tags
        element.style.opacity = 0;
        element.innerHTML = text;
        let op = 0;
        const fade = setInterval(() => {
          op += 0.1;
          element.style.opacity = op;
          if (op >= 1) {
            clearInterval(fade);
            if (onComplete) onComplete();
          }
        }, 30);
      } else {
        const interval = setInterval(() => {
          element.textContent += text.charAt(i);
          chatMessages.scrollTop = chatMessages.scrollHeight;
          i++;
          if (i >= text.length) {
            clearInterval(interval);
            if (onComplete) onComplete();
          }
        }, speed);
      }
    };

    const getOpenAIResponse = async (userMessage) => {
      try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${OPENAI_API_KEY}`
          },
          body: JSON.stringify({
            model: 'gpt-4o', // Or gpt-3.5-turbo
            messages: [
              {
                role: 'system',
                content: `You are the CybKart Global AI Architect, a premium digital growth advisor and smart business consultant. You speak confidently, naturally, and proactively. You never sound robotic or use generic phrases like 'How can I help you?'. Your goal is to guide visitors, recommend services, and eventually help them book a consultation via Calendly. When a user is ready to book or asks for a meeting, YOU MUST output EXACTLY this HTML block so they can book inline in the chat: <div style="border-radius:12px; overflow:hidden; margin-top:10px; background:#fff;"><iframe src="https://calendly.com/borgohainabhijit09/book-free-strategy-call?hide_gdpr_banner=1&hide_landing_page_details=1&background_color=ffffff&text_color=090b14&primary_color=0055ff" width="100%" height="400" frameborder="0"></iframe></div> . Do not use standard links for booking. You understand CybKart's services (Premium websites, AI chatbots, Lead gen, Automations, SEO) and pricing (Starter, Professional, Premium). Infer context naturally, don't ask repetitive questions. Suggest solutions based on the user's industry. Handle objections gracefully. Keep responses concise, engaging, and premium.`
              },
              ...conversationHistory,
              { role: 'user', content: userMessage }
            ],
            temperature: 0.7,
            max_tokens: 150
          })
        });

        if (!response.ok) throw new Error('API Error');
        const data = await response.json();
        return data.choices[0].message.content;
      } catch (error) {
        // Fallback to advanced local mock engine
        return getSmartMockResponse(userMessage);
      }
    };

    const getSmartMockResponse = (text) => {
      const lowerText = text.toLowerCase();
      
      // Update Context
      if (lowerText.match(/(detailing|roofing|landscaping|hvac|cleaning|dental|restaurant)/)) {
        const match = lowerText.match(/(detailing|roofing|landscaping|hvac|cleaning|dental|restaurant)/);
        userContext.industry = match[0];
      }

      // Memory & Intent Logic
      
      // Intent: Booking / Consultation
      if (lowerText.match(/(book|appointment|call|meeting|calendly|talk|strategy|schedule)/)) {
        return `Excellent move. Let's get you on a quick strategy call with our lead systems architect so we can map out a specific growth plan for your business.<br><br><div style="border-radius:12px; overflow:hidden; margin-top:10px; background:#fff;"><iframe src="https://calendly.com/borgohainabhijit09/book-free-strategy-call?hide_gdpr_banner=1&hide_landing_page_details=1&background_color=ffffff&text_color=090b14&primary_color=0055ff" width="100%" height="400" frameborder="0"></iframe></div>`;
      }
      
      // Intent: Services / Features
      if (lowerText.match(/(service|web|design|seo|automation|build|create|offer|do you do)/)) {
        userContext.servicesDiscussed.push('general');
        if (userContext.industry) {
          return `For ${userContext.industry} businesses, we typically implement high-converting landing pages tied directly into automated lead-capture and booking systems. It stops leads from falling through the cracks. Are you currently running any specific software to handle bookings?`;
        }
        return `We engineer premium digital systems—not just basic websites. We build conversion-focused web layouts, integrate AI chatbots for 24/7 lead capture, and set up automated review generation. What's the main bottleneck in your current digital setup?`;
      }
      
      // Intent: Pricing
      if (lowerText.match(/(price|pricing|cost|how much|fee|charge|budget|package)/)) {
        userContext.pricingDiscussed = true;
        return `We scale our systems based on what your operations actually need. We have a Starter tier for essential digital presence, a Professional tier optimized for active lead generation, and our Premium tier which fully integrates AI, CRM, and advanced automations.<br><br>The best way to get an exact quote is a quick 15-minute discovery audit. Shall I drop the link to schedule that?`;
      }

      // Intent: Objection - Expensive
      if (lowerText.match(/(expensive|too much|high|not in budget)/)) {
        if (userContext.objectionsHandled.includes('price')) {
          return `I completely understand. We always advise starting where it makes financial sense and scaling up as the new system generates ROI.`;
        }
        userContext.objectionsHandled.push('price');
        return `Totally understandable. Most businesses we work with usually see this as a long-term lead generation investment rather than just a website expense. The automation alone often saves enough administrative hours to pay for itself.`;
      }

      // Intent: Objection - Already have a website
      if (lowerText.match(/(already have|existing site|got a website)/)) {
        return `That actually puts you in a great position. Many of our clients come to us because their existing site looks a bit outdated, loads slowly, or simply isn't generating enough qualified leads. We can audit your current site on a quick call if you'd like?`;
      }

      // Smart Context Inference based on Industry
      if (userContext.industry && !userContext.servicesDiscussed.includes('industry_pitch')) {
        userContext.servicesDiscussed.push('industry_pitch');
        return `Nice — ${userContext.industry} businesses usually benefit a lot from visual-focused websites with before/after galleries, mobile booking, and automated lead capture. Is your current setup capturing leads automatically, or is it mostly a manual process?`;
      }

      // Fallback Conversational Response
      return `I see. To give you the most accurate roadmap for your specific growth targets, it's best we run a quick strategic audit on a brief call. <br><br><div style="border-radius:12px; overflow:hidden; margin-top:10px; background:#fff;"><iframe src="https://calendly.com/borgohainabhijit09/book-free-strategy-call?hide_gdpr_banner=1&hide_landing_page_details=1&background_color=ffffff&text_color=090b14&primary_color=0055ff" width="100%" height="400" frameborder="0"></iframe></div>`;
    };

    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if (!text) return;

      // Add user message
      addMessageToUI(text, 'user');
      chatInput.value = '';
      
      // Add to history
      conversationHistory.push({ role: 'user', content: text });
      
      // Limit history to last 10 messages for context window
      if (conversationHistory.length > 10) {
        conversationHistory = conversationHistory.slice(conversationHistory.length - 10);
      }

      // Show typing indicator
      const typingMsg = showTypingIndicator();

      // Process response
      let responseContent;
      if (OPENAI_API_KEY) {
        responseContent = await getOpenAIResponse(text);
      } else {
        // Simulate network delay for mock engine
        await new Promise(resolve => setTimeout(resolve, 800 + Math.random() * 600));
        responseContent = getSmartMockResponse(text);
      }

      typingMsg.remove();
      
      // Add Bot Message container
      const contentDiv = addMessageToUI('', 'bot', true);
      
      // Simulate Streaming Effect
      simulateStreamingText(contentDiv, responseContent, 15, () => {
        // Save to history once streamed
        conversationHistory.push({ role: 'assistant', content: responseContent });
      });
    });
  }
});
