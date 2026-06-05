const contactForm = document.querySelector("form[action*='formspree']");

if (contactForm) {
  contactForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const button = contactForm.querySelector("button[type='submit']");
    if (!button) return;
    
    button.disabled = true;
    button.textContent = "Sending…";
    try {
      const response = await fetch(contactForm.action, {
        method: "POST",
        body: new FormData(contactForm),
        headers: { "Accept": "application/json" },
      });
      if (response.ok) {
        window.location.href = "/thank_you.html";
      } else {
        button.disabled = false;
        button.textContent = "Send message";
        alert("Something went wrong. Please email us directly at hello@plainwebworks.co");
      }
    } catch {
      button.disabled = false;
      button.textContent = "Send message";
      alert("Something went wrong. Please email us directly at hello@plainwebworks.co");
    }
  });
}

const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector("#nav-menu");
const year = document.querySelector("#year");

if (year) {
  year.textContent = new Date().getFullYear();
}

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navMenu.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      navMenu.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}
