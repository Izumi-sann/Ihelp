// SCRIPT PER CHIUDERE MENU' PRINCIPALE
document.querySelector('.close-menu').addEventListener('click', () => {
    const menuCheckbox = document.getElementById('menu-toggle');
    menuCheckbox.checked = false; // Deseleziona la checkbox per chiudere il menu
  });


