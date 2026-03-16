import { defineConfig } from 'astro/config';
import qwikdev from '@qwikdev/astro';
import unocss from 'unocss/astro';

export default defineConfig({
  integrations: [
    qwikdev(),
    unocss({ injectReset: true }),
  ],
  // TĘ CZĘŚĆ MUSISZ DOPISAĆ:
  vite: {
    server: {
      allowedHosts: true
    },
    preview: {
      allowedHosts: true
    }
  }
});