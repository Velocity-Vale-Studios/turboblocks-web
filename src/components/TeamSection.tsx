import { component$, useSignal, $ } from '@builder.io/qwik';

export const TeamSection = component$(() => {
    const currentIndex = useSignal(0);

    const team = [
        {
            name: 'k8bus',
            role: 'Director',
            img: '/image/k8busSFIRST.png',
            theme: 'from-pink-500/40 via-purple-500/40 to-cyan-500/40'
        },
        {
            name: 'm4t3k33',
            role: 'Lead Engineer',
            img: '/image/image-13.jpg',
            theme: 'from-blue-600/40 via-indigo-500/40 to-cyan-400/40'
        },
        {
            name: 'nejt12475',
            role: 'Engineer',
            img: '/image/image-13.jpg',
            theme: 'from-emerald-500/40 via-teal-500/40 to-lime-400/40'
        },
        {
            name: 'MALYMATI2007',
            role: 'Engineer',
            img: '/image/image-13.jpg',
            theme: 'from-orange-500/40 via-red-500/40 to-yellow-400/40'
        },
        {
            name: 'Ayame',
            role: 'Pixel Artist',
            img: '/image/image-13.jpg',
            theme: 'from-violet-500/40 via-fuchsia-500/40 to-rose-400/40'
        }
    ];

    const next = $(() => (currentIndex.value = (currentIndex.value + 1) % team.length));
    const prev = $(() => (currentIndex.value = (currentIndex.value - 1 + team.length) % team.length));
    const setIndex = $((index: number) => (currentIndex.value = index));

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

                {/* Kontroler Slidera - STYL ORIGIN REALMS */}
                <div class="bg-white/[0.03] border border-white/10 rounded-[2.5rem] p-8 relative overflow-hidden group/item">

                    {/* Główny opis aktywnej osoby */}
                    <div class="mb-8">
                        <h5 class="text-3xl font-black text-white uppercase italic tracking-tighter transition-all duration-300">{active.name}</h5>
                        <p class="text-cyan-400 font-black text-[10px] uppercase tracking-[0.3em]">{active.role}</p>
                    </div>

                    {/* PASEK NAWIGACJI (HEADS STRIP) */}
                    <div class="flex items-center justify-between gap-4">

                        {/* Lewa Strzałka */}
                        <button onClick$={prev} class="w-8 h-8 flex items-center justify-center text-white/40 hover:text-white hover:scale-125 transition-all duration-300">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                            </svg>
                        </button>

                        {/* Lista Głów */}
                        <div class="flex items-center gap-3 overflow-x-auto no-scrollbar py-2 px-1">
                            {team.map((member, index) => (
                                <button
                                    key={member.name}
                                    onClick$={() => setIndex(index)}
                                    class={`relative w-10 h-10 rounded-lg overflow-hidden transition-all duration-300 ${
                                        currentIndex.value === index
                                            ? 'ring-2 ring-cyan-400 scale-110 shadow-[0_0_15px_rgba(34,211,238,0.4)] opacity-100 grayscale-0'
                                            : 'opacity-40 grayscale hover:opacity-100 hover:grayscale-0 hover:scale-105'
                                    }`}
                                >
                                    <img
                                        src={`https://mc-heads.net/avatar/${member.name}/100`}
                                        alt={member.name}
                                        class="w-full h-full object-cover"
                                    />
                                </button>
                            ))}
                        </div>

                        {/* Prawa Strzałka */}
                        <button onClick$={next} class="w-8 h-8 flex items-center justify-center text-white/40 hover:text-white hover:scale-125 transition-all duration-300">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </button>

                    </div>
                </div>
            </div>

            {/* PRAWE OKNO: NEON SPLASH (Bez zmian) */}
            <div class={`lg:col-span-5 bg-gradient-to-br ${active.theme} border border-white/20 rounded-[3.5rem] relative overflow-hidden min-h-[600px] flex items-center justify-center transition-all duration-1000 shadow-[0_0_50px_rgba(255,255,255,0.05)]`}>
                <div class="absolute inset-0 flex items-center justify-center p-10">
                    <img
                        src={`https://mc-heads.net/body/${active.name}/400`}
                        alt={active.name}
                        class="h-[90%] w-auto object-contain drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] transition-all duration-700 group-hover:scale-105 scale-x-[-1]"
                    />
                </div>

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