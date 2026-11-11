document.addEventListener("DOMContentLoaded", function () {
  // --- Mobile menu ---
  var toggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("program-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  // --- Shows: move past dates out of "Upcoming" automatically ---
  // A show stays "upcoming" through the end of its date, then moves.
  var now = new Date();
  var today = now.getFullYear() + "-" +
    String(now.getMonth() + 1).padStart(2, "0") + "-" +
    String(now.getDate()).padStart(2, "0");

  document.querySelectorAll('[data-show-list="upcoming"]').forEach(function (grid) {
    var past = grid.dataset.pastTarget ? document.getElementById(grid.dataset.pastTarget) : null;
    grid.querySelectorAll(".ticket[data-date]").forEach(function (card) {
      if (card.dataset.date < today) {
        if (past) {
          // Past cards don't need times, notes, or ticket links
          card.querySelectorAll(".ticket__meta, .ticket__desc, .ticket__main > a").forEach(function (el) { el.remove(); });
          past.appendChild(card);
        } else {
          card.remove();
        }
      }
    });

    var limit = parseInt(grid.dataset.limit, 10);
    if (limit) {
      grid.querySelectorAll(".ticket").forEach(function (card, i) {
        if (i >= limit) card.remove();
      });
    }

    if (!grid.querySelector(".ticket")) {
      grid.hidden = true;
      var empty = grid.nextElementSibling;
      if (empty && empty.classList.contains("show-list-empty")) empty.hidden = false;
    }
  });

  // --- Anything marked data-expires="YYYY-MM-DD" disappears after that date ---
  document.querySelectorAll("[data-expires]").forEach(function (el) {
    if (el.dataset.expires && el.dataset.expires < today) {
      var fallback = el.nextElementSibling;
      el.remove();
      if (fallback && fallback.hasAttribute("data-expired-fallback")) fallback.hidden = false;
    }
  });
});
