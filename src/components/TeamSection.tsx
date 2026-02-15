import { component$, useSignal, $ } from '@builder.io/qwik';

export const TeamSection = component$(() => {
    const currentIndex = useSignal(0);

    const team = [
        {
            name: 'k8bus',
            role: 'Director',
            img: '/image/k8busSFIRST.png',
            theme: 'from-pink-500/40 via-purple-500/40 to-cyan-500/40' // Originalish
        },
        {
            name: 'm4t3k33',
            role: 'Lead Engineer',
            img: '/image/image-13.jpg',
            theme: 'from-blue-600/40 via-indigo-500/40 to-cyan-400/40' // Deep Blue Tech
        },
        {
            name: 'nejt12475',
            role: 'Engineer',
            img: '/image/image-13.jpg',
            theme: 'from-emerald-500/40 via-teal-500/40 to-lime-400/40' // Green Matrix
        },
        {
            name: 'MALYMATI2007',
            role: 'Engineer',
            img: '/image/image-13.jpg',
            theme: 'from-orange-500/40 via-red-500/40 to-yellow-400/40' // Fiery
        },
        {
            name: 'Ayame',
            role: 'Pixel Artist',
            img: '/image/image-13.jpg',
            theme: 'from-violet-500/40 via-fuchsia-500/40 to-rose-400/40' // Artistic Purple
        }

    ];

    const next = $(() => (currentIndex.value = (currentIndex.value + 1) % team.length));
    const prev = $(() => (currentIndex.value = (currentIndex.value - 1 + team.length) % team.length));

    const active = team[currentIndex.value];

    return (
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">

            {/* LEWE OKNO: SZKLANY PANEL */}
            <div class="lg:col-span-7 bg-white/[0.02] border border-white/10 rounded-[3.5rem] p-12 backdrop-blur-2xl flex flex-col justify-between relative overflow-hidden group">
                <div class={`absolute -top-24 -right-24 w-96 h-96 bg-gradient-to-br ${active.theme} blur-[100px] opacity-20 transition-all duration-1000`}></div>

                <div class="relative z-10">
                    <div class="inline-block px-4 py-1.5 bg-cyan-400/10 border border-cyan-400/20 rounded-full text-[10px] font-black text-cyan-400 uppercase tracking-[0.2em] mb-8">
                        Online Profile // CC-2026
                    </div>
                    <h4 class="text-6xl font-black italic text-white uppercase tracking-tighter mb-6 leading-tight">
                        The <span class="text-transparent bg-clip-text bg-gradient-to-r from-pink-300 to-cyan-300">Founders</span>
                    </h4>
                    <p class="text-white/40 text-sm leading-relaxed max-w-md mb-12 font-medium">
                        W świecie Color Clash każdy kolor ma znaczenie. Poznaj ludzi, którzy namalowali tę rzeczywistość od zera.
                    </p>
                </div>

                {/* Kontroler Slidera */}
                <div class="bg-white/[0.03] border border-white/10 rounded-[2.5rem] p-8 relative overflow-hidden group/item">
                    <div class="flex items-center gap-6">
                        <div class="w-20 h-20 flex-shrink-0 perspective-500">
                            <img
                                src={`https://mc-heads.net/avatar/${active.name}/100`}
                                alt={active.name}
                                class="w-full h-full object-contain drop-shadow-lg rounded-xl"
                            />
                        </div>
                        <div>
                            <h5 class="text-3xl font-black text-white uppercase italic tracking-tighter">{active.name}</h5>
                            <p class="text-cyan-400 font-black text-[10px] uppercase tracking-[0.3em]">{active.role}</p>
                        </div>
                    </div>

                    <div class="flex gap-3 mt-10">
                        <button onClick$={prev} class="w-14 h-14 bg-white/5 border border-white/10 text-white rounded-2xl hover:bg-cyan-400 hover:text-black transition-all font-black shadow-lg">←</button>
                        <button onClick$={next} class="w-14 h-14 bg-white/5 border border-white/10 text-white rounded-2xl hover:bg-pink-400 hover:text-black transition-all font-black shadow-lg">→</button>
                    </div>
                </div>
            </div>

            {/* PRAWE OKNO: NEON SPLASH */}
            <div class={`lg:col-span-5 bg-gradient-to-br ${active.theme} border border-white/20 rounded-[3.5rem] relative overflow-hidden min-h-[600px] flex items-center justify-center transition-all duration-1000 shadow-[0_0_50px_rgba(255,255,255,0.05)]`}>

                {/* Render Postaci */}
                <div class="absolute inset-0 flex items-center justify-center p-10">
                    <img
                        src={`https://mc-heads.net/body/${active.name}/400`}
                        alt={active.name}
                        class="h-[90%] w-auto object-contain drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] transition-all duration-700 group-hover:scale-105 scale-x-[-1]"
                    />
                </div>

                {/* Podpis - Neon Glass style */}
                <div class="absolute bottom-8 left-8 right-8 p-8 bg-black/40 backdrop-blur-xl border border-white/10 rounded-[2.5rem]">
                    <div class="flex flex-col items-center">
                        <span class="text-5xl font-black italic text-white uppercase tracking-tighter leading-none mb-2">
                            {active.name}
                        </span>
                        <div class="flex items-center gap-4">
                            <div class="h-[2px] w-8 bg-gradient-to-r from-cyan-400 to-pink-400"></div>
                            <span class="text-[10px] font-black text-white/60 uppercase tracking-[0.4em]">{active.role}</span>
                            <div class="h-[2px] w-8 bg-gradient-to-r from-pink-400 to-cyan-400"></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    );
});