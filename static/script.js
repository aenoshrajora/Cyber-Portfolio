
  new TypeIt("#experience-header", {
    strings: ["$ cat 'Experience'"],
    speed: 70,
    breakLines: false,
    loop: true,
    waitUntilVisible: true,
    nextStringDelay: 1000,
    lifeLike: true,
    cursor: true,
  }).go();

  new TypeIt("#ctf-header", {
    strings: ["$ grep CTF's"],
    speed: 70,
    breakLines: false,
    loop: true,
    waitUntilVisible: true,
    nextStringDelay: 1000,
    lifeLike: true,
    cursor: true,
  }).go();

  new TypeIt("#skills-header", {
    strings: ["$ ls 'Skills'"],
    speed: 70,
    breakLines: false,
    loop: true,
    waitUntilVisible: true,
    nextStringDelay: 1000,
    lifeLike: true,
    cursor: true,
  }).go();

const canvas = document.getElementById('mouseTrail');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});

const particles = [];

class Particle {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.radius = Math.random() * 3 + 1;
    this.alpha = 1;
    this.velocity = {
      x: (Math.random() - 0.5) * 2,
      y: (Math.random() - 0.5) * 2
    };
  }

  draw() {
    ctx.beginPath();
    ctx.shadowColor = 'cyan';
    ctx.shadowBlur = 10;
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(0, 255, 255, ${this.alpha})`;
    ctx.fill();
  }

  update() {
    this.x += this.velocity.x;
    this.y += this.velocity.y;
    this.alpha -= 0.02;
  }
}

document.addEventListener('mousemove', (e) => {
  for (let i = 0; i < 4; i++) {
    particles.push(new Particle(e.clientX, e.clientY));
  }
});

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < particles.length; i++) {
    particles[i].update();
    particles[i].draw();

    if (particles[i].alpha <= 0) {
      particles.splice(i, 1);
      i--;
    }
  }

  requestAnimationFrame(animate);
}

animate();
