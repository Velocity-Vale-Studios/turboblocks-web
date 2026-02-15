import { defineConfig } from 'astro/config';
import qwikdev from '@qwikdev/astro'; // Czasem to: import { qwikdev } from '@qwikdev/astro';
import unocss from 'unocss/astro';

export default defineConfig({
  integrations: [
    qwikdev(),
    unocss({ injectReset: true }),
  ],
});