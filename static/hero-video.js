const heroVideo = document.querySelector('.hero-video');
const heroVideoToggle = document.querySelector('.hero-video-toggle');

if (heroVideo && heroVideoToggle) {
  const heroMedia = heroVideo.closest('.hero-media');
  const showFrame = () => heroMedia.classList.add('has-video-frame');
  const hideFrame = () => heroMedia.classList.remove('has-video-frame');

  // Keep the poster visible until the browser actually presents a video frame.
  if (typeof heroVideo.requestVideoFrameCallback === 'function') {
    heroVideo.requestVideoFrameCallback(showFrame);
    heroVideo.addEventListener('playing', () => heroVideo.requestVideoFrameCallback(showFrame));
  } else {
    heroVideo.addEventListener('timeupdate', () => {
      if (heroVideo.currentTime > 0 && heroVideo.readyState >= 2) showFrame();
    });
  }
  heroVideo.addEventListener('waiting', hideFrame);
  heroVideo.addEventListener('stalled', hideFrame);
  heroVideo.addEventListener('error', hideFrame);

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

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    heroVideo.autoplay = false;
    heroVideo.pause();
  }

  updateToggle();
}
