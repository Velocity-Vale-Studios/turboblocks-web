import { defineConfig } from 'astro/config';
import qwikdev from '@qwikdev/astro';
import unocss from 'unocss/astro';

export default defineConfig({
  integrations: [
    qwikdev(),
    unocss({ injectReset: true }),
  ],
  vite: {
    server: {
      allowedHosts: ['turboblocks.eu', 'www.turboblocks.eu', '.turboblocks.eu', 'all']
    },
    preview: {
      allowedHosts: ['turboblocks.eu', 'www.turboblocks.eu', '.turboblocks.eu', 'all']
    }
  }
});