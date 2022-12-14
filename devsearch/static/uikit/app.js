// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}

// if (alertWrapper) {
//   alertClose.addEventListener("click", () => (alertWrapper.style.display = "none"));
// }

// function closeButton() {
//   alertWrapper.style.display = "none"
// }

// alertClose.addEventListener("click", closeButton) 