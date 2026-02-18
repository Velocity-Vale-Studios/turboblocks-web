import { defineConfig, presetUno, presetWebFonts } from 'unocss'

export default defineConfig({
    presets: [
        presetUno(),
        presetWebFonts({
            provider: 'google',
            fonts: {
                sans: 'Inter:300,400,600',
                heading: 'Plus Jakarta Sans:200,800',
            },
        }),
    ],
    theme: {
        colors: {
            premium: {
                bg: '#0a0b10',
                card: 'rgba(255, 255, 255, 0.03)',
                border: 'rgba(255, 255, 255, 0.08)',
                mint: '#e0fbfc',
                lavender: '#e2e2ff',
                peach: '#ffd4b8',
            },
            arcade: {
                pink: '#ff006e',
                neon_pink: '#ff4d7d',
                cyan: '#00d9ff',
                lime: '#39ff14',
                purple: '#b500d9',
                neon_purple: '#d946ef',
                yellow: '#ffff00',
                orange: '#ff8c00',
            }
        }
    }
})