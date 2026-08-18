---
title: Writing
permalink: /writing/
---

<section class="hero" style="padding: 70px 0 50px;">
  <div class="wrap">
    <p class="eyebrow">Writing</p>
    <h1>Selected pieces</h1>
    <p class="tagline">Essays and short work — some that fed into Dealbreaker, some that stayed on the page.</p>
  </div>
</section>
<div class="bulb-strip" aria-hidden="true"></div>

<section class="section">
  <div class="wrap">
    <div class="ticket-grid">
      {% assign pieces = site.writing | sort: "date" | reverse %}
      {% for piece in pieces %}
        {% include ticket.html
          label=piece.piece_type
          title=piece.title
          meta=piece.date | date: "%B %-d, %Y"
          desc=piece.excerpt_note
          link=piece.url
          link_text="Read"
          stub="Read" %}
      {% endfor %}
    </div>

    {% if site.writing.size == 0 %}
      <p>New pieces coming soon.</p>
    {% endif %}
  </div>
</section>
