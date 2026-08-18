---
title: Home
permalink: /
---

<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Storyteller &middot; Solo Performer &middot; Facilitator</p>
    <h1>{{ site.author }}</h1>
    <p class="tagline">True stories, told out loud. Creator and performer of the solo show <strong>Dealbreaker</strong> — now booking theaters, festivals, and living rooms.</p>
    <div class="hero-actions">
      <a class="btn btn--solid" href="{{ '/dealbreaker/' | relative_url }}">See the show</a>
      <a class="btn" href="{{ '/contact/' | relative_url }}">Book / get in touch</a>
    </div>
  </div>
</section>
<div class="bulb-strip" aria-hidden="true"></div>

<section class="section">
  <div class="wrap">
    <blockquote class="pull-quote">
      "The bravest thing a storyteller can do is tell the truth and let the audience decide what to do with it."
      <cite>— on the philosophy behind Dealbreaker</cite>
    </blockquote>
  </div>
</section>

<hr class="tear">

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What's On</p>
      <h2>Four ways to work together</h2>
      <p>A solo show, hands-on workshops, presenter partnerships, and writing you can read right now.</p>
    </div>

    <div class="ticket-grid">
      {% include ticket.html
        label="Solo Show"
        title="Dealbreaker"
        meta="70 min &middot; one performer &middot; touring now"
        desc="A true story about the deals we make with ourselves — and the ones we finally refuse to."
        link="/dealbreaker/"
        link_text="About the show"
        stub="Show" %}

      {% include ticket.html
        label="Workshops"
        title="Story Building Sessions"
        meta="60–180 min &middot; groups &amp; 1:1"
        desc="Hands-on sessions for writers, teams, and first-time storytellers who want to find and shape their material."
        link="/workshops/"
        link_text="See formats"
        stub="Workshop" %}

      {% include ticket.html
        label="Partnerships"
        title="Presenters &amp; Venues"
        meta="theaters &middot; festivals &middot; universities"
        desc="Booking info, tech rider, and past presenting partners for producers considering Dealbreaker."
        link="/partnerships/"
        link_text="Partner info"
        stub="Partner" %}

      {% include ticket.html
        label="Writing"
        title="Selected Pieces"
        meta="essays &amp; short work"
        desc="Writing that didn't make it to the stage, or grew out of what did."
        link="/writing/"
        link_text="Start reading"
        stub="Read" %}
    </div>
  </div>
</section>

<hr class="tear">

<section class="section section--paper">
  <div class="wrap split">
    <div class="portrait" aria-hidden="true">[ Portrait photo ]</div>
    <div>
      <p class="eyebrow">About</p>
      <h2 class="mt-0">Hi, I'm {{ site.author }}.</h2>
      <p>I make solo theater and lead storytelling workshops. My show <strong>Dealbreaker</strong> has toured to theaters, storytelling festivals, and living rooms — replace this paragraph with two or three sentences about your own background, training, and the kind of work you make.</p>
      <p><a href="{{ '/about/' | relative_url }}">Read the full bio &rarr;</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <p class="eyebrow">Get In Touch</p>
    <h2>Bring the show to your stage.</h2>
    <p class="narrow" style="margin-left:auto; margin-right:auto;">Whether you're booking Dealbreaker, hiring a workshop, or just want to say hello — I'd love to hear from you.</p>
    <a class="btn btn--solid" href="{{ '/contact/' | relative_url }}">Contact {{ site.author }}</a>
  </div>
</section>
