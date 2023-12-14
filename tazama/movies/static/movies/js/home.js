/* Refresh page on clicking the logo */
function refreshPage() {
    location.reload();
}


/************** Navigation Bar ************** */
const toggleMenu = () => {
  const navigation = document.querySelector('.navigation');

  const burgerMenu = document.querySelector(".menu-icon");
  const src = burgerMenu.getAttribute("src");

  const isBurger = (src === burgerImagePath );

  const iconName = isBurger ?
      closeImagePath
      :
      burgerImagePath;

  burgerMenu.setAttribute(
      "src", iconName
  );

  if (!isBurger) {
      navigation.classList.add("navigation--mobile--fadeout");
      setTimeout (() => {
          navigation.classList.toggle (
              "navigation--mobile"
          );
      }, 300)
  } else {
      navigation.classList.remove("navigation--mobile--fadeout");
      navigation.classList.toggle (
          "navigation--mobile"
      );
  }
};



/* Function to show the search form and hide recommendation button */
function toggleFormAndOptions() {
  let form = document.getElementById("search_form");
  let button = document.getElementById("toggle_button");
  let heroTitle = document.getElementById("hero_title");
  let mainTitle = document.getElementById("main_title");
  let secondaryTitle = document.getElementById("secondary_title");

  if (form.style.display === "none") {
      // Show recommendation options
      form.style.display = "block";
      button.style.display = "none";
      // Update hero title
      mainTitle.innerText = "Get a holiday movie recommendation ";
      secondaryTitle.innerText = "Based on Genre(s)";
  } else {
      // Show search form
      form.style.display = "none";
      button.style.display = "block";
      // Reset hero title
      mainTitle.innerText = "Yule Love It!";
      secondaryTitle.innerText = "With Our Christmas Movie Picks!";
  }
}


// JavaScript function to go back
function goBack() {
    window.history.back();
}
