// Seleziona il pulsante "Servizi" e il sottomenu
const servicesToggle = document.querySelector('.services-toggle');
const servicesMenu = document.getElementById('services-menu');

// Aggiungi un listener per gestire il click
servicesToggle.addEventListener('click', (e) => {
  e.preventDefault(); // Evita il comportamento predefinito del link
  // Mostra/nascondi il sottomenu
  if (servicesMenu.style.display === 'flex') {
    servicesMenu.style.display = 'none';
  } else {
    servicesMenu.style.display = 'flex';
  }
});

  