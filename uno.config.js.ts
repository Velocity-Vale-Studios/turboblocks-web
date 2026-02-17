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
    // Wymuszone klasy dla dynamicznych danych z JSONa
    safelist: [
        // Glows (Neony)
        'shadow-[0_0_40px_rgba(236,72,153,0.2)]', // Pink
        'shadow-[0_0_40px_rgba(37,99,235,0.2)]',  // Blue
        'shadow-[0_0_40px_rgba(16,185,129,0.2)]', // Emerald (Nejt)
        'shadow-[0_0_40px_rgba(249,115,22,0.2)]',  // Orange
        'shadow-[0_0_40px_rgba(139,92,246,0.2)]', // Violet (Ayame)
        // Border colors
        'border-pink-500/30', 'border-blue-500/30', 'border-emerald-500/30', 'border-orange-500/30', 'border-violet-500/30',
        // Text colors
        'text-pink-500', 'text-blue-500', 'text-emerald-500', 'text-orange-500', 'text-violet-500'
    ],
    content: {
        pipeline: {
            include: [/\.(vue|svelte|[jt]sx|mdx?|astro|elm|php|phtml|html|json)($|\?)/],
        },
    },
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