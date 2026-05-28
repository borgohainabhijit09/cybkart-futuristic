/* ==========================================================================
   CYBKART GLOBAL - DYNAMIC SPA TRANSITION & BLUR REVEAL ENGINE (transitions.js)
   ========================================================================== */

import { lenis } from './app.js';

document.addEventListener('DOMContentLoaded', () => {
  initTransitions();
  initMobileMenu();
});

function initTransitions() {
  const overlay = document.getElementById('page-transition-overlay');
  const titleText = document.getElementById('transition-title-text');
  const transitionEyebrow = document.querySelector('.transition-eyebrow');
  const blurFilter = document.getElementById('blur-filter');
  
  if (!overlay || !titleText || !blurFilter) return;

  // Title strings mapping for cinematic uppercase reveals
  const viewTitles = {
    home: "CYBKART GLOBAL",
    services: "LUXURY ENGINE",
    industries: "TARGET VERTICALS",
    toolkit: "THE CYBER STACK",
    portfolio: "CASE STUDIES",
    pricing: "GROWTH INVESTMENT",
    contact: "STRATEGY BRIEFING"
  };

  // Intercept all navigation links
  const transitionLinks = document.querySelectorAll('[data-view]');

  transitionLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const targetView = link.getAttribute('data-view');
      const currentActive = document.querySelector('.page-view.active');
      
      // If view is already active or doesn't exist, bypass custom transition
      if (!targetView || (currentActive && currentActive.id === `view-${targetView}`)) {
        e.preventDefault();
        return;
      }

      e.preventDefault();
      
      // Close hamburger overlays immediately if active
      closeMobileMenu();

      // Trigger full cinematic GSAP wipe timeline
      executeCinematicTransition(targetView);
    });
  });

  function executeCinematicTransition(targetView) {
    // 1. Prepare overlay title text
    const label = viewTitles[targetView] || "LOADING CORE";
    titleText.textContent = label;

    // Reset SplitType context on text if initialized
    let splitChars = [];
    if (window.SplitType) {
      const splitInstance = new SplitType(titleText, { types: 'chars' });
      splitChars = splitInstance.chars;
    }

    // Set initial layout parameters
    gsap.set(overlay, { translateY: '100%', visibility: 'visible' });
    gsap.set(transitionEyebrow, { opacity: 0, y: -20 });
    
    // Set heavy horizontal blur on text before starting reveal
    const blurObj = { x: 50 };
    blurFilter.setAttribute('stdDeviation', '50, 0');

    if (splitChars.length > 0) {
      gsap.set(splitChars, { opacity: 0, scale: 0.6, z: -100 });
    } else {
      gsap.set(titleText, { opacity: 0, scale: 0.8 });
    }

    // Disable Lenis scroll during layout swap
    if (lenis) lenis.stop();

    // 2. Cinematic GSAP timeline
    const tl = gsap.timeline({
      onComplete: () => {
        // Swap actual active panel DOMs
        swapViews(targetView);

        // Slide overlay upwards to leave screen
        gsap.timeline({
          onComplete: () => {
            // Restore Lenis scroll controls
            if (lenis) lenis.start();
          }
        })
        .to(overlay, {
          translateY: '-100%',
          duration: 1.1,
          ease: 'power4.inOut'
        })
        .set(overlay, { translateY: '100%', visibility: 'hidden' }); // Reset position silently at bottom
      }
    });

    // Slide transition board up in view frame
    tl.to(overlay, {
      translateY: '0%',
      duration: 1,
      ease: 'power4.inOut'
    });

    // Reveal eyebrow badge
    tl.to(transitionEyebrow, {
      opacity: 1,
      y: 0,
      duration: 0.6,
      ease: 'power2.out'
    }, '-=0.2');

    // Cinematic Letter-by-letter reveal with horizontal blur
    if (splitChars.length > 0) {
      tl.to(splitChars, {
        opacity: 1,
        scale: 1,
        z: 0,
        stagger: 0.04,
        duration: 1.2,
        ease: 'power4.out'
      }, '-=0.6');
    } else {
      tl.to(titleText, {
        opacity: 1,
        scale: 1,
        duration: 1,
        ease: 'power4.out'
      }, '-=0.6');
    }

    // Animate standard deviation values of SVG Filter (reducing motion blur to zero)
    tl.to(blurObj, {
      x: 0,
      duration: 1.4,
      ease: 'power3.out',
      onUpdate: () => {
        blurFilter.setAttribute('stdDeviation', `${blurObj.x}, 0`);
      }
    }, '-=1.2');

    // Wait slightly at center before leaving
    tl.to({}, { duration: 0.5 });
  }

  function swapViews(targetView) {
    // Fade out previous view content & mark inactive
    const activeView = document.querySelector('.page-view.active');
    if (activeView) {
      activeView.classList.remove('active');
    }

    // Locate target view segment and display
    const newView = document.getElementById(`view-${targetView}`);
    if (newView) {
      newView.classList.add('active');
    }

    // Sync navbar link active markers
    const allLinks = document.querySelectorAll('.nav-link, .mobile-link');
    allLinks.forEach(lnk => {
      if (lnk.getAttribute('data-view') === targetView) {
        lnk.classList.add('active');
      } else {
        lnk.classList.remove('active');
      }
    });

    // Instantly snap scrollbar tracker to top (via Lenis smooth controller)
    if (lenis) {
      lenis.scrollTo(0, { immediate: true });
    } else {
      window.scrollTo(0, 0);
    }

    // Trigger individual GSAP ScrollTrigger refresh
    ScrollTrigger.refresh();

    // Trigger entrance animation timelines on the newly active sub-page elements
    triggerSectionEntranceTimeline(newView);
  }

  function triggerSectionEntranceTimeline(section) {
    if (!section) return;
    
    const items = section.querySelectorAll('.service-card, .tool-item, .portfolio-item, .pricing-card, .contact-grid');
    
    // Play quick staggered rise layout
    if (items.length > 0) {
      gsap.from(items, {
        opacity: 0,
        y: 40,
        stagger: 0.1,
        duration: 1.1,
        ease: 'power3.out',
        overwrite: 'auto'
      });
    }
  }
}

/* Hamburger mobile control overlay events */
function initMobileMenu() {
  const btn = document.getElementById('hamburger-btn');
  const menu = document.getElementById('mobile-menu');

  if (!btn || !menu) return;

  btn.addEventListener('click', () => {
    btn.classList.toggle('active');
    menu.classList.toggle('active');
    
    // Lock Lenis scroll in backdrop if menu overlay is open
    if (lenis) {
      if (menu.classList.contains('active')) {
        lenis.stop();
      } else {
        lenis.start();
      }
    }
  });
}

function closeMobileMenu() {
  const btn = document.getElementById('hamburger-btn');
  const menu = document.getElementById('mobile-menu');

  if (btn && menu) {
    btn.classList.remove('active');
    menu.classList.remove('active');
  }
}
