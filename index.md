---
title: Home
permalink: /
---

<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Storyteller &middot; Solo Performer &middot; Producer</p>
    <h1>{{ site.author }}</h1>
    <p class="tagline">Creator and performer of the solo show <strong>Dealbreaker</strong>.</p>
    <div class="hero-actions">
      <a class="btn btn--solid" href="#upcoming">Upcoming shows</a>
      <a class="btn" href="mailto:{{ site.social.email }}">Get in touch</a>
    </div>
  </div>
</section>
<div class="bulb-strip" aria-hidden="true"></div>

<!-- Intro -->
<section class="section">
  <div class="wrap split">
    <img src="{{ '/assets/images/lauren-home-portrait.jpg' | relative_url }}" alt="Lauren Kee" style="width:100%; height:auto; display:block; border-radius: var(--radius);">
    <div>
      <h2 class="mt-0">Hi, I'm Lauren!</h2>
      <p>I'm a storyteller, solo performer, and producer. I love telling stories about girlhood and growth, and helping other performers bring their stories to the stage!</p>
      <p><a href="{{ '/about/' | relative_url }}">More about me &rarr;</a></p>
    </div>
  </div>
</section>

<hr class="tear">

<!-- Upcoming shows: every type, pulled from _data/shows.yml -->
<section class="section section--paper" id="upcoming">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Upcoming</p>
      <h2>Come to a show</h2>
    </div>
    {% include show-list.html limit=3 stub_type=true empty="New dates coming soon. Follow along on Instagram for announcements." %}
    <p class="section-links">
      <a href="{{ '/dealbreaker/' | relative_url }}#upcoming">All Dealbreaker dates &rarr;</a>
      <a href="{{ '/storytelling/' | relative_url }}#upcoming">All storytelling dates &rarr;</a>
    </p>
  </div>
</section>

<hr class="tear tear--paper">

<!-- Dealbreaker -->
<section class="section">
  <div class="wrap split">
    <img src="{{ '/assets/images/dealbreaker-production-2.jpg' | relative_url }}" alt="Lauren Kee performing Dealbreaker" style="width:100%; height:auto; display:block; border-radius: var(--radius);">
    <div>
      <p class="eyebrow">Solo Show</p>
      <h2 class="mt-0">Dealbreaker</h2>
      <p>A one-woman show about herpes, heartbreak, and the death of the one-night stand. Part storytelling, part comedy, 100% stigma-squashing.</p>
      <a class="btn btn--solid" href="{{ '/dealbreaker/' | relative_url }}">About the show &amp; tour dates</a>
    </div>
  </div>
</section>

<!-- Press & Praise -->
<section class="section section--paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Press &amp; Praise</p>
      <h2>What people are saying</h2>
    </div>
    <div class="quote-grid">
      <blockquote class="pull-quote">
        &ldquo;A journey of accepting yourself and finding love in this crazy world.&rdquo;
        <cite><a href="https://www.broadwayworld.com/central-pa/article/Review-HARRISBURG-FRINGE-2026-at-Various-Venues-In-Harrisburg-20260720">BroadwayWorld.com</a></cite>
      </blockquote>
      <blockquote class="pull-quote">
        &ldquo;Warm, honest, funny, and easy to root for.&rdquo;
        <cite>Stuart Landon, Artistic Director, Open Stage of Harrisburg</cite>
      </blockquote>
      <blockquote class="pull-quote">
        &ldquo;It opens the door to conversations most people avoid and handles them with both wit and care.&rdquo;
        <cite>Barbara Belcore, Chicago-based midwife</cite>
      </blockquote>
      <blockquote class="pull-quote">
        &ldquo;Lauren shows how we can show up as we are, authentically, including the stuff that's a little messy.&rdquo;
        <cite>Dr. Noelle Sullivan, Northwestern University</cite>
      </blockquote>
      <blockquote class="pull-quote">
        &ldquo;A slick, hilarious solo show - and educational too! Top notch writing and storytelling.&rdquo;
        <cite>Elgin Fringe Festival audience member</cite>
      </blockquote>
    </div>
  </div>
</section>

<hr class="tear tear--paper">

<!-- Storytelling -->
<section class="section">
  <div class="wrap split split--flip">
    <div>
      <p class="eyebrow">True Stories</p>
      <h2 class="mt-0">Storytelling</h2>
      <p>Stories about growth, girlhood, and the messy moments in between. Catch one live or watch a few from home.</p>
      <a class="btn btn--solid" href="{{ '/storytelling/' | relative_url }}">Watch my stories</a>
    </div>
    <div style="position:relative; width:100%; padding-top:56.25%; border-radius: var(--radius); overflow:hidden;">
      <iframe src="https://www.youtube.com/embed/61Qoc6E2VLE" title="Lauren Kee storytelling" loading="lazy" style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
  </div>
</section>

<hr class="tear">

<!-- Solo Sunday -->
<section class="section section--paper">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Producer</p>
      <h2>Solo Sunday</h2>
      <p class="narrow">I produce Solo Sunday, a series that gives solo artists a cozy pop-up stage without the cost of a traditional theater.</p>
    </div>
    {% include solo-sunday-next.html %}
    <p class="section-links"><a href="{{ '/solo-sunday/' | relative_url }}">About Solo Sunday &rarr;</a></p>
  </div>
</section>

<hr class="tear tear--paper">

<!-- Closing -->
<section class="section center">
  <div class="wrap">
    <h2 class="mt-0">Let's work together</h2>
    <p class="narrow" style="margin-left:auto; margin-right:auto;">Want to book Dealbreaker or have me tell a story at your event?</p>
    <div class="hero-actions" style="justify-content:center;">
      <a class="btn btn--solid" href="mailto:{{ site.social.email }}">Get in touch</a>
      <a class="btn" href="{{ site.social.instagram }}">Follow on Instagram</a>
    </div>
  </div>
</section>
