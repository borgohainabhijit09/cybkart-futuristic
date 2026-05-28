/* ==========================================================================
   CYBKART GLOBAL - HERO INTERACTIVE DASHBOARD CONTROLLER (dashboard.js)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Export our dashboard triggers to the global scope for trigger synchronization
  window.initDashboardAnimations = initDashboard;
});

function initDashboard() {
  const mockup = document.getElementById('dashboard-mockup');
  
  if (!mockup) return;

  // 1. Draw SVG chart line drawing path
  animateSVGChart();

  // 2. Start 3D Mouse Parallax Hover Tilt
  init3DParallaxTilt(mockup);

  // 3. Trigger chatbot discussion typed elements loop
  initChatbotTypingLoop();

  // 4. Trigger rolling hot lead notifications sequence
  initLeadNotificationsLoop();
}

/* 1. Draw SVG chart line drawing path */
function animateSVGChart() {
  const path = document.querySelector('.chart-line-path');
  const area = document.querySelector('.chart-area-path');
  const marker = document.querySelector('.chart-marker');

  if (!path || !area) return;

  // Calculate SVG line boundaries
  const length = path.getTotalLength();
  
  // Set initial hidden parameters
  gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
  gsap.set(area, { opacity: 0, scaleY: 0, transformOrigin: 'bottom center' });
  gsap.set(marker, { opacity: 0, scale: 0 });

  // Draw timeline
  const tl = gsap.timeline({ delay: 0.5 });
  
  tl.to(path, {
    strokeDashoffset: 0,
    duration: 2.2,
    ease: 'power2.inOut'
  });

  tl.to(area, {
    opacity: 1,
    scaleY: 1,
    duration: 1.2,
    ease: 'power3.out'
  }, '-=1.2');

  tl.to(marker, {
    opacity: 1,
    scale: 1,
    duration: 0.6,
    ease: 'back.out(2)'
  }, '-=0.4');
}

/* 2. 3D Mouse Parallax Hover Tilt coordinate mapping */
function init3DParallaxTilt(mockup) {
  const container = mockup.parentElement;
  
  if (!container) return;

  const handleMouseMove = (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - rect.left; // x position within element
    const y = e.clientY - rect.top;  // y position within element
    
    // Normalize coordinates from -0.5 to 0.5
    const normX = (x / rect.width) - 0.5;
    const normY = (y / rect.height) - 0.5;

    // Set maximum deflection angles (deg)
    const maxRotateX = 25; // Vertical rotation limits
    const maxRotateY = 30; // Horizontal rotation limits

    // Calculate rotation coordinates based on normalized cursor position
    const targetRotateX = -normY * maxRotateX; // Vertical deflection matches y offset
    const targetRotateY = normX * maxRotateY;   // Horizontal deflection matches x offset

    // Apply smooth tracking transforms using GSAP
    gsap.to(mockup, {
      rotateX: 12 + targetRotateX, // Base neutral offset of 12 degrees X
      rotateY: -18 + targetRotateY, // Base neutral offset of -18 degrees Y
      rotateZ: 3 + (normX * 5),
      duration: 0.6,
      ease: 'power2.out',
      overwrite: 'auto'
    });

    // Subtly parallax shift depth components
    const tiltElements = mockup.querySelectorAll('.scroll-tilt');
    tiltElements.forEach(el => {
      const depth = parseFloat(el.dataset.depth || 0.1);
      gsap.to(el, {
        x: normX * 40 * depth,
        y: normY * 40 * depth,
        duration: 0.6,
        ease: 'power2.out',
        overwrite: 'auto'
      });
    });
  };

  const handleMouseLeave = () => {
    // Gracefully return to beautiful baseline perspective
    gsap.to(mockup, {
      rotateX: 15,
      rotateY: -20,
      rotateZ: 3,
      duration: 1.2,
      ease: 'power3.out',
      overwrite: 'auto'
    });

    const tiltElements = mockup.querySelectorAll('.scroll-tilt');
    tiltElements.forEach(el => {
      gsap.to(el, {
        x: 0,
        y: 0,
        duration: 1.2,
        ease: 'power3.out',
        overwrite: 'auto'
      });
    });
  };

  container.addEventListener('mousemove', handleMouseMove);
  container.addEventListener('mouseleave', handleMouseLeave);
}

/* 3. Infinite dialogue loops inside floating chatbot card mockup */
function initChatbotTypingLoop() {
  const bubbles = document.querySelectorAll('#chatbot-dialogue .chat-bubble');
  if (bubbles.length === 0) return;

  const runSequence = () => {
    // Hide all bubbles
    bubbles.forEach(b => b.classList.remove('visible'));
    
    // Staggered trigger typed overlays
    const tl = gsap.timeline({ 
      onComplete: () => {
        // Wait 4 seconds and loop the typing script again
        gsap.delayedCall(4, runSequence);
      }
    });

    bubbles.forEach((bubble, index) => {
      tl.call(() => {
        bubble.classList.add('visible');
      }, null, `+=${index === 0 ? 0.2 : 1.5}`); // Staggered delays
    });
  };

  // Start sequence
  runSequence();
}

/* 4. Rotating mockup notification lead streams simulation */
function initLeadNotificationsLoop() {
  const leadCard = document.querySelector('.lead-card');
  const titleEl = leadCard?.querySelector('.lead-title');
  const metaEl = leadCard?.querySelector('.lead-meta');
  const timeEl = leadCard?.querySelector('.lead-time');

  if (!leadCard || !titleEl || !metaEl) return;

  // Sequence pool representing realistic automated high-value client acquisitions
  const leadPool = [
    { name: "New Enterprise SaaS Secured", meta: "Apex Platforms • <span class='cyan-text'>$8,500/mo Retainer</span>", time: "Just Now" },
    { name: "High-Ticket App Deployed", meta: "Vanguard Fintech • <span class='cyan-text'>$24,500 System</span>", time: "1m ago" },
    { name: "Headless Commerce Launch", meta: "Luma Storefronts • <span class='cyan-text'>$12,000 Contract</span>", time: "Just Now" },
    { name: "Custom LLM Model Synced", meta: "Synapse AI Core • <span class='cyan-text'>Model Training Active</span>", time: "3m ago" },
    { name: "Scale Consultation Booked", meta: "Outfit Media Portal • <span class='cyan-text'>Automated Setup Active</span>", time: "Just Now" }
  ];

  let poolIndex = 0;

  const pushNextLead = () => {
    // Slide notification card down and fade out
    gsap.timeline({
      onComplete: () => {
        // Pick new lead variables
        poolIndex = (poolIndex + 1) % leadPool.length;
        const currentData = leadPool[poolIndex];

        // Swap contents
        titleEl.innerHTML = currentData.name;
        metaEl.innerHTML = currentData.meta;
        timeEl.innerHTML = currentData.time;

        // Slide notification back up in viewport with bounce elastic spring
        gsap.to(leadCard, {
          y: 0,
          opacity: 1,
          duration: 1,
          ease: 'back.out(1.2)'
        });
      }
    })
    .to(leadCard, {
      y: 30,
      opacity: 0,
      duration: 0.6,
      ease: 'power3.in',
      delay: 5 // Delay before changing current card (5 seconds read-time)
    });
  };

  // Set repeating interval
  setInterval(pushNextLead, 9000); // Trigger lead roll every 9 seconds
}
