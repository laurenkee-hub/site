# laurenkee.com — Jekyll site

A Jekyll site for storyteller Lauren Kee: the solo show **Dealbreaker**,
workshops, partnerships/booking info, and writing. Built with the
"github-pages" gem, so it deploys straight to GitHub Pages with no
build step of your own.

Design: a "playbill / marquee" theme — dark stage background, marquee-gold
accent, and a reusable "ticket stub" card used for show dates, workshop
sessions, and writing pieces.

## 1. Preview it locally (optional but recommended)

You'll need Ruby installed. Then, from this folder:

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000 in your browser. Edit any `.md` or `.html`
file and the site rebuilds automatically.

## 2. Switch the theme (colors, fonts, corner style)

The whole visual identity — background/text colors, accent colors,
fonts, and corner rounding — is controlled by **one line** in
`_config.yml`:

```yaml
theme_name: "theatrical"   # or "literary", "minimal", "blush", "meadow", "sherbet"
```

Change it, save, and push (or restart `jekyll serve` locally) — every
page re-skins automatically. The six built-in options:

| `theme_name`  | Feel                                                    | Fonts                     |
|---------------|-----------------------------------------------------------|-----------------------------|
| `theatrical`  | Bold & dramatic — dark stage, marquee gold, deep red       | Anton / Source Serif 4     |
| `literary`    | Warm & muted — cream paper, ink brown, forest green        | Playfair Display / Lora    |
| `minimal`     | Clean & modern — white space, near-black, one accent       | Space Grotesk / Inter      |
| `blush`       | Warm & romantic — raspberry & apricot, pillowy-soft        | Fraunces / Nunito          |
| `meadow`      | Warm & botanical — dusty rose & sage, quiet cottagecore    | DM Serif Display / Karla   |
| `sherbet`     | Warm & playful — coral & teal, bright citrus energy        | Fredoka / Mulish           |

**How it works:** every color/font/radius decision lives as a CSS
variable in a file under `_sass/themes/` (one per theme). The rest of
the site's CSS (`_sass/base.scss`) never
hardcodes a color — it only reads those variables, so it automatically
looks right under any theme.

**To make your own theme:** duplicate one of the files in
`_sass/themes/`, rename it (e.g. `_sunrise.scss`), tweak the values,
then set `theme_name: "sunrise"` in `_config.yml`. Tokens you can set:
`--bg`, `--bg-2`, `--accent`, `--accent-dim`, `--accent-2`,
`--accent-2-dim`, `--surface`, `--surface-dim`, `--text`, `--text-dim`,
`--text-on-surface`, `--text-on-surface-dim`, `--card-light`,
`--font-display`, `--font-body`, `--font-mono`, `--radius`,
`--heading-tracking`. If your new theme needs fonts that aren't
already loaded, add them to the Google Fonts link in
`_includes/head.html`.

## 3. Put your real content in

Everything in this repo is a placeholder you should replace:

- **`_config.yml`** — site title, author, email, social links
- **`index.md`** — homepage hero, intro, and the four ticket cards
- **`dealbreaker.md`** — show description, tour dates
- **`workshops.md`** — session formats, past partners
- **`partnerships.md`** — tech rider, booking terms, past presenters
- **`about.md`** — full bio, press links
- **`contact.md`** — the contact form (see step 4 below)
- **`_writing/*.md`** — one file per writing piece. Duplicate one to add
  a new piece; delete the ones you don't want.
- **`assets/images/`** — add real photos here, then swap the `[ Portrait
  photo ]` placeholder `<div class="portrait">` blocks for real `<img>` tags.

## 4. Put it on GitHub

```bash
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

Then in the repo on GitHub: **Settings → Pages → Build and deployment →
Source: Deploy from a branch → Branch: main / (root)**. Save.

## 5. Connect laurenkee.com (bought on Porkbun)

You already have `laurenkee.com` — here's how to point it at this site.

**A. In this repo**
The `CNAME` file at the root already contains `www.laurenkee.com`, and
`_config.yml`'s `url` is set to `https://www.laurenkee.com`. That part's done.

**B. In Porkbun's DNS settings for laurenkee.com**
Go to Porkbun → Domain Management → laurenkee.com → DNS Records, and add:

| Type  | Host | Answer                  |
|-------|------|--------------------------|
| A     | (blank / @) | 185.199.108.153   |
| A     | (blank / @) | 185.199.109.153   |
| A     | (blank / @) | 185.199.110.153   |
| A     | (blank / @) | 185.199.111.153   |
| CNAME | www  | YOUR-USERNAME.github.io |

(Those four `A` records are GitHub's official Pages IPs — they point the
bare `laurenkee.com` at GitHub. The `CNAME` record points `www` at your
GitHub Pages address.) Remove/replace any existing `A` or `ALIAS` records
Porkbun added by default for the root domain (e.g. its default parking
page or URL-forwarding record) so they don't conflict.

**C. Back in GitHub → Settings → Pages**
Under "Custom domain," enter `www.laurenkee.com` and save. Wait a few
minutes to a few hours for DNS to propagate, then check the box for
**Enforce HTTPS** once it becomes available (GitHub provisions the SSL
certificate automatically — this can take up to 24 hours). GitHub will
automatically redirect the bare `laurenkee.com` to `www.laurenkee.com`.

## 6. Turn on the contact form

The form on `/contact/` posts to Formspree (a free service that emails
you form submissions — no server needed):

1. Create a free account at https://formspree.io
2. Create a new form, copy its ID (the form action looks like
   `https://formspree.io/f/abcdwxyz`)
3. In `contact.md`, replace `YOUR_FORM_ID` in the form's `action`
   attribute with your real ID.

## 7. Ongoing edits

- **Add a tour date:** copy one `{% include ticket.html %}` block in
  `dealbreaker.md` and edit the label/title/meta/desc.
- **Add a writing piece:** duplicate a file in `_writing/`, edit the
  front matter, write the piece.
- **Change colors/fonts:** all design tokens live at the top of
  `assets/css/style.scss` under `:root`.

Any push to `main` automatically rebuilds and redeploys the live site —
no separate publish step needed.
