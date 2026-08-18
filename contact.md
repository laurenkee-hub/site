---
title: Contact
permalink: /contact/
---

<section class="hero" style="padding: 70px 0 50px;">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Let's talk</h1>
    <p class="tagline">Booking Dealbreaker, hiring a workshop, or just saying hello — this goes straight to {{ site.author }}.</p>
  </div>
</section>
<div class="bulb-strip" aria-hidden="true"></div>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Direct</p>
      <h2 class="mt-0">Reach out directly</h2>
      <p>Prefer email? Write to <a href="mailto:{{ site.social.email }}">{{ site.social.email }}</a>.</p>
      <p>For time-sensitive bookings, include your preferred dates, venue or organization, and audience size in your first message — it speeds things up.</p>

      <h3>Follow along</h3>
      <ul>
        <li><a href="mailto:{{ site.social.email }}">Email</a></li>
        {% if site.social.instagram and site.social.instagram != "" %}<li><a href="{{ site.social.instagram }}">Instagram</a></li>{% endif %}
        {% if site.social.youtube and site.social.youtube != "" %}<li><a href="{{ site.social.youtube }}">Video / performance clips</a></li>{% endif %}
      </ul>
    </div>

    <div>
      <p class="eyebrow">Message</p>
      <h2 class="mt-0">Send a message</h2>

      <!--
        This form uses Formspree (formspree.io) — a free service that emails
        form submissions to you without needing a server, which works well
        with a static GitHub Pages site.

        Setup:
        1. Create a free account at https://formspree.io
        2. Create a new form and copy its endpoint (looks like
           https://formspree.io/f/xxxxabcd)
        3. Replace YOUR_FORM_ID below with that ID.
        Until you do this, the form will not actually send anywhere.
      -->
      <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
        <div class="form-field">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="form-field">
          <label for="email">Email</label>
          <input type="email" id="email" name="_replyto" required>
        </div>
        <div class="form-field">
          <label for="reason">What's this about?</label>
          <select id="reason" name="reason">
            <option>Booking Dealbreaker</option>
            <option>Hiring a workshop</option>
            <option>Partnership / presenting</option>
            <option>Press / media</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="form-field">
          <label for="message">Message</label>
          <textarea id="message" name="message" rows="6" required></textarea>
        </div>
        <button type="submit" class="btn btn--solid">Send message</button>
      </form>
    </div>
  </div>
</section>
