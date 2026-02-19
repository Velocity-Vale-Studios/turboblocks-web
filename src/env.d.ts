/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />

interface ImportMetaEnv {
    // Tu możesz dopisać swoje zmienne z .env, np.:
    // readonly SECRET_TOKEN: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}