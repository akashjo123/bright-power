document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const hamburger = document.querySelector('.hamburger');
  const body = document.body;
  const header = document.querySelector('.header') || document.querySelector('.header-pill');

  if (hamburger) {
    hamburger.addEventListener('click', () => {
      body.classList.toggle('mobile-menu-active');
      const icon = hamburger.querySelector('i');
      if (icon) {
        if (body.classList.contains('mobile-menu-active')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-times');
        } else {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      }
    });
  }

  // Close mobile menu on link click
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      body.classList.remove('mobile-menu-active');
      const icon = hamburger?.querySelector('i');
      if (icon) {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
      }
    });
  });

  // Sticky Header on Scroll
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 10) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // Fade Up Scroll Animations
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.1
  };

  const fadeUpElements = document.querySelectorAll('.fade-up');
  
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Unobserve after animating to only animate once
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  fadeUpElements.forEach((element, index) => {
    // Add staggered delay for grid items
    if (element.parentElement && (
        element.parentElement.classList.contains('grid-2') || 
        element.parentElement.classList.contains('grid-3') || 
        element.parentElement.classList.contains('grid-4') ||
        element.parentElement.classList.contains('bento-grid') ||
        element.parentElement.classList.contains('trust-items'))) {
      
      const children = Array.from(element.parentElement.children);
      const elIndex = children.indexOf(element);
      
      if (elIndex !== -1) {
        element.style.transitionDelay = `${elIndex * 0.1}s`;
      }
    }
    
    observer.observe(element);
  });
});
