import { component$, useSignal, $, useStyles$ } from '@builder.io/qwik';

export const TeamSection = component$(() => {
    // Style animacji
    useStyles$(`
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .slide-anim {
            animation: slideIn 0.4s ease-out forwards;
        }
    `);

    const currentIndex = useSignal(0);

    // DANE ZDEFINIOWANE LOKALNIE (Gwarancja działania kolorów UnoCSS)
    const team = [
        {
            name: 'k8bus',
            role: 'Director',
            theme: 'from-pink-500/40 via-purple-500/40 to-cyan-500/40',
            quote: 'Building dreams, one block at a time.',
            textClass: 'text-pink-500',
            borderClass: 'border-pink-500',
            borderColorClass: 'border-pink-500/30',
            bgClass: 'bg-pink-500',
            ringClass: 'ring-pink-500',
            shadowClass: 'shadow-pink-500/40',
            glowClass: 'shadow-[0_0_40px_rgba(236,72,153,0.2)]'
        },
        {
            name: 'm4t3k33',
            role: 'Lead Engineer',
            theme: 'from-blue-600/40 via-indigo-500/40 to-cyan-400/40',
            quote: 'Efficiency is the key to success.',
            textClass: 'text-blue-500',
            borderClass: 'border-blue-500',
            borderColorClass: 'border-blue-500/30',
            bgClass: 'bg-blue-500',
            ringClass: 'ring-blue-500',
            shadowClass: 'shadow-blue-500/40',
            glowClass: 'shadow-[0_0_40px_rgba(37,99,235,0.2)]'
        },
        {
            name: 'nejt12475',
            role: 'Engineer',
            theme: 'from-emerald-500/40 via-teal-500/40 to-lime-400/40',
            quote: 'Solving problems you didn\'t know you had.',
            textClass: 'text-emerald-500',
            borderClass: 'border-emerald-500',
            borderColorClass: 'border-emerald-500/30',
            bgClass: 'bg-emerald-500',
            ringClass: 'ring-emerald-500',
            shadowClass: 'shadow-emerald-500/40',
            glowClass: 'shadow-[0_0_40px_rgba(16,185,129,0.2)]'
        },
        {
            name: 'MALYMATI2007',
            role: 'Engineer',
            theme: 'from-orange-500/40 via-red-500/40 to-yellow-400/40',
            quote: 'Innovation never sleeps.',
            textClass: 'text-orange-500',
            borderClass: 'border-orange-500',
            borderColorClass: 'border-orange-500/30',
            bgClass: 'bg-orange-500',
            ringClass: 'ring-orange-500',
            shadowClass: 'shadow-orange-500/40',
            glowClass: 'shadow-[0_0_40px_rgba(249,115,22,0.2)]'
        },
        {
            name: 'Ayame',
            role: 'Pixel Artist',
            theme: 'from-violet-500/40 via-fuchsia-500/40 to-rose-400/40',
            quote: 'Pixel perfect, every time.',
            textClass: 'text-violet-500',
            borderClass: 'border-violet-500',
            borderColorClass: 'border-violet-500/30',
            bgClass: 'bg-violet-500',
            ringClass: 'ring-violet-500',
            shadowClass: 'shadow-violet-500/40',
            glowClass: 'shadow-[0_0_40px_rgba(139,92,246,0.2)]'
        }
    ];

    const next = $(() => (currentIndex.value = (currentIndex.value + 1) % team.length));
    const prev = $(() => (currentIndex.value = (currentIndex.value - 1 + team.length) % team.length));
    const setIndex = $((index: number) => (currentIndex.value = index));

    const active = team[currentIndex.value];

    return (
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-8 items-stretch min-h-[600px]">

            {/* --- LEWE OKNO: INFO I NAWIGACJA --- */}
            <div class={`lg:col-span-7 bg-gradient-to-br from-white/5 to-white/[0.02] border ${active.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] p-6 lg:p-12 backdrop-blur-3xl flex flex-col justify-center relative overflow-hidden group ${active.glowClass} transition-all duration-700`}>

                {/* Tło Ambient */}
                <div class={`absolute -top-24 -right-24 w-96 h-96 bg-gradient-to-br ${active.theme} blur-[100px] opacity-20 transition-all duration-1000 pointer-events-none`}></div>

                {/* Status Badge */}
                <div class="absolute top-6 lg:top-12 left-6 lg:left-12 inline-block px-3 lg:px-4 py-1 lg:py-1.5 bg-cyan-400/10 border border-cyan-400/20 rounded-full text-[8px] lg:text-[10px] font-black text-cyan-400 uppercase tracking-[0.2em]">
                    Online Profile // CC-2026
                </div>

                {/* Główna treść (Tekst po lewej) */}
                <div key={active.name} class="mt-16 lg:mt-8 mb-6 lg:mb-8 relative z-10 slide-anim">
                    <h5 class="text-3xl lg:text-5xl font-black text-white uppercase italic tracking-tighter transition-all duration-300 mb-2 pr-4">
                        {active.name}
                    </h5>
                    <p class={`${active.textClass} font-black text-[10px] lg:text-xs uppercase tracking-[0.3em] mb-4 lg:mb-8`}>
                        {active.role}
                    </p>

                    <p class={`text-white/60 text-base lg:text-lg italic font-medium border-l-4 ${active.borderClass} pl-4 lg:pl-6 max-w-lg leading-relaxed`}>
                        "{active.quote}"
                    </p>
                </div>

                {/* PASEK NAWIGACJI */}
                <div class="flex flex-col items-center gap-4 mt-auto pt-6 lg:pt-8 border-t border-white/5 relative z-10 w-full">

                    {/* Górny rząd: Tylko głowy na mobile / Strzałki + głowy na desktop */}
                    <div class="flex items-center justify-center w-full gap-2 lg:gap-4">

                        {/* Lewa Strzałka - Widoczna tylko od LG w górę */}
                        <button
                            onClick$={prev}
                            class="hidden lg:flex w-10 h-10 items-center justify-center text-white/40 hover:text-white hover:scale-125 transition-all duration-300 shrink-0"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                            </svg>
                        </button>

                        {/* Lista Głów */}
                        <div class="flex items-center justify-center gap-2 lg:gap-3 py-2 px-3 bg-white/[0.02] rounded-xl border border-white/5">
                            {team.map((member, index) => (
                                <button
                                    key={member.name}
                                    onClick$={() => setIndex(index)}
                                    class={`relative w-9 h-9 sm:w-10 sm:h-10 lg:w-12 lg:h-12 rounded-lg overflow-hidden transition-all duration-300 shrink-0 
                                        ${currentIndex.value === index
                                        ? `ring-2 ${member.ringClass} scale-110 shadow-lg ${member.shadowClass} opacity-100 z-10`
                                        : `opacity-40 grayscale hover:opacity-100 hover:grayscale-0 hover:scale-110 hover:ring-2 ${member.ringClass} hover:shadow-lg ${member.shadowClass} z-0 hover:z-10`
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

                        {/* Prawa Strzałka - Widoczna tylko od LG w górę */}
                        <button
                            onClick$={next}
                            class="hidden lg:flex w-10 h-10 items-center justify-center text-white/40 hover:text-white hover:scale-125 transition-all duration-300 shrink-0"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </button>
                    </div>

                    {/* Dolny rząd: Strzałki widoczne TYLKO na mobile (poniżej LG) */}
                    <div class="flex lg:hidden items-center gap-8">
                        <button
                            onClick$={prev}
                            class="w-12 h-12 flex items-center justify-center rounded-full bg-white/5 border border-white/10 text-white/60 active:scale-90 transition-all"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                            </svg>
                        </button>

                        <button
                            onClick$={next}
                            class="w-12 h-12 flex items-center justify-center rounded-full bg-white/5 border border-white/10 text-white/60 active:scale-90 transition-all"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>

            {/* --- PRAWE OKNO: POSTAĆ 3D (NEON SPLASH) --- */}
            <div class={`lg:col-span-5 bg-gradient-to-br ${active.theme} backdrop-blur-3xl border ${active.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] relative overflow-hidden min-h-[400px] lg:min-h-[600px] flex items-center justify-center ${active.glowClass}`}>

                {/* Postać */}
                <div key={active.name} class="absolute inset-0 flex items-center justify-center p-4 lg:p-10 slide-anim z-10">
                    <img
                        src={`https://mc-heads.net/body/${active.name}/400`}
                        alt={active.name}
                        class="h-[80%] lg:h-[90%] w-auto object-contain drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] scale-x-[-1]"
                    />
                </div>

                {/*KARTA INFORMACYJNA (Na dole) */}
                <div key={active.name + 'info'} class="absolute bottom-4 lg:bottom-8 left-4 lg:left-8 right-4 lg:right-8 p-4 lg:p-8 bg-black/40 backdrop-blur-xl border border-white/10 rounded-[1.5rem] lg:rounded-[2.5rem] slide-anim z-20">
                    <div class="flex flex-col items-center">
                        <span class="text-3xl lg:text-5xl font-black italic text-white uppercase tracking-tighter leading-none mb-2 text-center">
                            {active.name}
                        </span>
                        <div class="flex items-center gap-2 lg:gap-4">
                            <div class={`h-[2px] w-6 lg:w-8 ${active.bgClass}`}></div>
                            <span class="text-[8px] lg:text-[10px] font-black text-white/60 uppercase tracking-[0.4em]">{active.role}</span>
                            <div class={`h-[2px] w-6 lg:w-8 ${active.bgClass}`}></div>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    );
});