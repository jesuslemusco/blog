document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle Logic
  const themeToggleButton = document.getElementById('theme-toggle');
  const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
  const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

  if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
    themeToggleLightIcon.classList.remove('hidden');
  } else {
    document.documentElement.classList.remove('dark');
    themeToggleDarkIcon.classList.remove('hidden');
  }

  themeToggleButton.addEventListener('click', () => {
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');
    if (localStorage.getItem('color-theme')) {
      if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      }
    } else {
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      }
    }
  });
  
  // Mobile Menu Logic
  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mobileMenuCloseButton = document.getElementById('mobile-menu-close-button');
  const mobileMenu = document.getElementById('mobile-menu');
  const toggleMenu = (e) => { e && e.stopPropagation(); mobileMenu.classList.toggle('hidden'); };
  mobileMenuButton.addEventListener('click', toggleMenu);
  mobileMenuCloseButton.addEventListener('click', toggleMenu);
  mobileMenu.querySelectorAll('a').forEach(link => link.addEventListener('click', toggleMenu));

  // Footer year
  const y = document.getElementById('year'); 
  if (y) y.textContent = new Date().getFullYear();
});
