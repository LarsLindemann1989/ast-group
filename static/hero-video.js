const heroVideo = document.querySelector('.hero-video');
const heroVideoToggle = document.querySelector('.hero-video-toggle');

if (heroVideo && heroVideoToggle) {
  const updateToggle = () => {
    const label = heroVideo.paused ? 'Play video' : 'Pause video';
    heroVideoToggle.textContent = label;
    heroVideoToggle.setAttribute('aria-label', label);
  };

  heroVideoToggle.addEventListener('click', () => {
    if (heroVideo.paused) {
      heroVideo.play().catch(updateToggle);
    } else {
      heroVideo.pause();
    }
  });

  heroVideo.addEventListener('play', updateToggle);
  heroVideo.addEventListener('pause', updateToggle);
  heroVideo.addEventListener('loadeddata', () => {
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && heroVideo.paused) {
      heroVideo.play().catch(updateToggle);
    }
  });

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    heroVideo.autoplay = false;
    heroVideo.pause();
  }

  updateToggle();
}
