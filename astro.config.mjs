import { defineConfig } from 'astro/config';
import qwikdev from '@qwikdev/astro';
import unocss from 'unocss/astro';

export default defineConfig({
  integrations: [
    unocss({
      injectReset: true,
      // Dodaj to, aby wymusić generowanie stylów przed Qwikiem
    }),
    qwikdev(),
  ],
  vite: {
    // UnoCSS musi być też tutaj jako plugin Vite,
    // żeby Qwik widział wygenerowane klasy podczas budowania wysp
    plugins: [],
    server: {
      allowedHosts: ['turboblocks.eu', 'www.turboblocks.eu', '.turboblocks.eu', 'all']
    },
    preview: {
      allowedHosts: ['turboblocks.eu', 'www.turboblocks.eu', '.turboblocks.eu', 'all']
    }
  }
});