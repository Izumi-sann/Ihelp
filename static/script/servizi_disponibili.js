function openServicesPopup() {
    document.getElementById("servicesPopup").style.display = "flex";
}

function closeServicesPopup() {
    document.getElementById("servicesPopup").style.display = "none";
}

// Associa l'evento di apertura al bottone "Servizi"
document.querySelector(".services-toggle").addEventListener("click", openServicesPopup);