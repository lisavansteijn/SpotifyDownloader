# SpotifyDownloader

A simple way to load in your favourite songs into a MP3 player! 

I've been recently been finding a way to start collecting music the good old fashioned way, but at the same time I have so many spotify playlists I've made over the years. 
While there are some options to simply parse in a spotify link, I wasn't quite happy with the queueing and the subscriptions I'd often find. So... why not use my web development powers to bypass all that! No more subscriptions, more music.

Note: I'm still going through the techstack and see what's redundant and what isn't. So things may change in the future.

# Current Techstack:

## Frontend:
- Vue 3 (TS) & Pinia
- Vite
- Tailwindcss & DaisyUI
- Cypress
- Playwright
- oxlint

## Backend:
- Django REST framework
- [spotDL](https://spotdl.readthedocs.io/en/latest/#music-sourcing-and-audio-quality)

If you clone this project, make sure to also set things up in your spotify developer dashboard!

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
pnpm install
```

### Compile and Hot-Reload for Development

```sh
pnpm dev
```


### Setting up the django server:

```sh
# Create a virtual environment to isolate our package dependencies locally
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
python manage.py runserver 
```

### Migrating changes:
```sh
# Create a virtual environment to isolate our package dependencies locally
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
python manage.py makemmigrations djangospotifydownloader
pythin manage.py migrate 
```

### Type-Check, Compile and Minify for Production

```sh
pnpm build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
pnpm test:unit
```

### Run End-to-End Tests with [Cypress](https://www.cypress.io/)

```sh
pnpm test:e2e:dev
```

This runs the end-to-end tests against the Vite development server.
It is much faster than the production build.

But it's still recommended to test the production build with `test:e2e` before deploying (e.g. in CI environments):

```sh
pnpm build
pnpm test:e2e
```

### Lint with [ESLint](https://eslint.org/)

```sh
pnpm lint
```
