document.addEventListener('DOMContentLoaded', () => {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    
    question.addEventListener('click', () => {
      // Check if this item is currently active
      const isActive = item.classList.contains('active');
      
      // Close all items
      faqItems.forEach(faqItem => {
        faqItem.classList.remove('active');
      });
      
      // If it wasn't active, open it
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
});
