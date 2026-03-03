import {defineConfig} from "unocss";

export default defineConfig({
    // ... Twoje istniejące presets i theme ...
    safelist: [
        // Dodajemy wszystkie kombinacje kolorów arcade, których używamy
        ...['pink', 'cyan', 'lime', 'orange', 'purple', 'neon_pink', 'neon_purple', 'yellow'].flatMap(c => [
            `text-arcade-${c}`,
            `bg-arcade-${c}`,
            `border-arcade-${c}`,
            `border-arcade-${c}/30`,
            `ring-arcade-${c}`,
            `from-arcade-${c}/40`,
            `via-arcade-${c}/40`,
            `to-arcade-${c}/40`,
        ]),
        // Cienie glow (Uno potrzebuje pełnych stringów w safelist dla customowych wartości)
        'shadow-[0_0_40px_rgba(255,0,110,0.3)]',
        'shadow-[0_0_40px_rgba(0,217,255,0.3)]',
        'shadow-[0_0_40px_rgba(57,255,20,0.3)]',
        'shadow-[0_0_40px_rgba(255,140,0,0.3)]',
        'shadow-[0_0_40px_rgba(181,0,217,0.3)]'
    ]
})