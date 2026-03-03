/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />

interface ImportMetaEnv {
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}

declare module "*.json" {
    const value: any;
    export default value;
}