/* ─── CUSTOM CURSOR ──────────────────────────────────────────── */
const cursor    = document.getElementById('cursor');
const cursorDot = document.getElementById('cursorDot');

document.addEventListener('mousemove', e => {
  cursor.style.left    = e.clientX + 'px';
  cursor.style.top     = e.clientY + 'px';
  cursorDot.style.left = e.clientX + 'px';
  cursorDot.style.top  = e.clientY + 'px';
});

/* ─── NAVBAR SCROLL ─────────────────────────────────────────── */
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
  document.getElementById('backToTop').classList.toggle('show', window.scrollY > 400);
});

/* ─── HAMBURGER ─────────────────────────────────────────────── */
document.getElementById('hamburger').addEventListener('click', function () {
  const links = document.querySelector('.nav-links');
  const isOpen = links.style.display === 'flex';
  links.style.cssText = isOpen
    ? ''
    : 'display:flex;flex-direction:column;position:absolute;top:72px;left:0;right:0;background:rgba(245,240,235,0.98);padding:1.5rem 2rem;gap:1.2rem;backdrop-filter:blur(14px);border-bottom:1px solid #e0d8cf;';
});

/* ─── TYPEWRITER ─────────────────────────────────────────────── */
const roles = ['Web Developer', 'Content Creator', 'UI/UX Enthusiast', 'Educator & Programmer'];
let rIdx = 0, cIdx = 0, deleting = false;
const tw = document.getElementById('typewriter');

function typeWrite() {
  const word = roles[rIdx];
  tw.textContent = deleting ? word.slice(0, cIdx--) : word.slice(0, cIdx++);
  if (!deleting && cIdx > word.length) {
    deleting = true; setTimeout(typeWrite, 1800); return;
  }
  if (deleting && cIdx < 0) {
    deleting = false; rIdx = (rIdx + 1) % roles.length; cIdx = 0;
    setTimeout(typeWrite, 400); return;
  }
  setTimeout(typeWrite, deleting ? 55 : 95);
}
typeWrite();

/* ─── SCROLL REVEAL ─────────────────────────────────────────── */
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(el => {
    if (el.isIntersecting) {
      el.target.classList.add('revealed');
      // Animate skill bars when visible
      el.target.querySelectorAll('.skill-fill').forEach(bar => {
        bar.style.width = bar.dataset.width + '%';
      });
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal-up,.reveal-left,.reveal-right').forEach(el => revealObs.observe(el));

// Also observe skill fills directly
const skillObs = new IntersectionObserver((entries) => {
  entries.forEach(el => {
    if (el.isIntersecting) {
      el.target.querySelectorAll('.skill-fill').forEach(bar => {
        setTimeout(() => { bar.style.width = bar.dataset.width + '%'; }, 200);
      });
    }
  });
}, { threshold: 0.2 });
document.querySelectorAll('.skills-grid').forEach(el => skillObs.observe(el));

/* ─── PORTFOLIO FILTER ──────────────────────────────────────── */
const filterBtns = document.querySelectorAll('.filter-btn');
const projCards  = document.querySelectorAll('.proj-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const cat = btn.dataset.filter;
    projCards.forEach(card => {
      const match = cat === 'all' || card.dataset.category === cat;
      card.style.transition = 'opacity 0.3s, transform 0.3s';
      if (match) {
        card.classList.remove('hidden');
        card.style.opacity = '1'; card.style.transform = '';
      } else {
        card.style.opacity = '0'; card.style.transform = 'scale(0.95)';
        setTimeout(() => card.classList.add('hidden'), 300);
      }
    });
  });
});

/* ─── CONTACT FORM ──────────────────────────────────────────── */
const form    = document.getElementById('contactForm');
const formMsg = document.getElementById('formMsg');
const btnText = document.getElementById('btnText');
const btnLoad = document.getElementById('btnLoading');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  btnText.style.display = 'none';
  btnLoad.style.display = 'inline';
  formMsg.className = 'form-msg';

  const payload = {
    name:    document.getElementById('name').value,
    email:   document.getElementById('email').value,
    message: document.getElementById('message').value,
  };

  try {
    const res  = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    formMsg.textContent = data.msg;
    formMsg.className   = 'form-msg ' + (data.success ? 'success' : 'error');
    if (data.success) form.reset();
  } catch {
    formMsg.textContent = 'Terjadi kesalahan. Silakan coba lagi.';
    formMsg.className   = 'form-msg error';
  } finally {
    btnText.style.display = 'inline';
    btnLoad.style.display = 'none';
  }
});

/* ─── SMOOTH NAV LINKS ──────────────────────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    // Close mobile menu
    document.querySelector('.nav-links').style.cssText = '';
  });
});

/* ─── NUMBER COUNT-UP ───────────────────────────────────────── */
function countUp(el, target, suffix) {
  let cur = 0;
  const step = Math.ceil(target / 50);
  const timer = setInterval(() => {
    cur = Math.min(cur + step, target);
    el.textContent = cur + suffix;
    if (cur >= target) clearInterval(timer);
  }, 30);
}

const statObs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.stat-num').forEach(el => {
        const raw = el.textContent;
        const num = parseInt(raw);
        const suf = raw.replace(/[0-9]/g, '');
        countUp(el, num, suf);
      });
      statObs.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stats-bar').forEach(el => statObs.observe(el));
