// uno.config.ts
import { defineConfig, presetUno, presetWebFonts } from 'unocss'

export default defineConfig({
    presets: [
        presetUno(),
        presetWebFonts({
            provider: 'google',
            fonts: {
                // Zostawiamy Inter do tekstu, ale nagłówki robimy czyste i szerokie
                sans: 'Inter:300,400,600',
                heading: 'Plus Jakarta Sans:200,800',
            },
        }),
    ],
    theme: {
        colors: {
            premium: {
                bg: '#0a0b10',        // Bardzo głęboki granat, nie czarny
                card: 'rgba(255, 255, 255, 0.03)',
                border: 'rgba(255, 255, 255, 0.08)',
                // Pastele
                mint: '#e0fbfc',      // Miętowy pastel
                lavender: '#e2e2ff',  // Lawendowy pastel
                peach: '#ffd4b8',     // Brzoskwiniowy pastel
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
                pastel_pink: '#ffb3d9',
                pastel_blue: '#b3d9ff',
                pastel_green: '#b3ffb3',
                pastel_yellow: '#ffffb3',
                pastel_purple: '#e6b3ff',
                pastel_orange: '#ffd9b3',
            }
        }
    }
})