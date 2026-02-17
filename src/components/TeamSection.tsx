import { component$, useSignal, $, useStyles$ } from '@builder.io/qwik';
import teamData from '../data/team.json';

export const TeamSection = component$(() => {
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
    const team = teamData;
    const active = team[currentIndex.value];

    const next = $(() => (currentIndex.value = (currentIndex.value + 1) % team.length));
    const prev = $(() => (currentIndex.value = (currentIndex.value - 1 + team.length) % team.length));
    const setIndex = $((index: number) => (currentIndex.value = index));

    return (
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-8 items-stretch">
            {/* LEWE OKNO */}
            <div class={`lg:col-span-7 bg-gradient-to-br from-white/5 to-white/[0.02] border ${active.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] p-6 lg:p-12 backdrop-blur-3xl flex flex-col justify-center relative overflow-hidden group ${active.glowClass} transition-all duration-700`}>
                <div class={`absolute -top-24 -right-24 w-96 h-96 bg-gradient-to-br ${active.theme} blur-[100px] opacity-20 transition-all duration-1000`}></div>

                <div key={active.name} class="mt-6 lg:mt-8 mb-6 lg:mb-8 relative z-10 slide-anim">
                    <h5 class="text-3xl lg:text-5xl font-black text-white uppercase italic tracking-tighter mb-2">{active.name}</h5>
                    <p class={`${active.textClass} font-black text-[10px] lg:text-xs uppercase tracking-[0.3em] mb-4 lg:mb-8`}>{active.role}</p>
                    <p class={`text-white/60 text-base lg:text-lg italic font-medium border-l-4 ${active.borderClass} pl-4 lg:pl-6 max-w-lg leading-relaxed`}>
                        "{active.quote}"
                    </p>
                </div>

                {/* NAWIGACJA */}
                <div class="flex items-center justify-center gap-2 lg:gap-4 mt-auto pt-6 lg:pt-8 border-t border-white/5 relative z-10 flex-wrap">
                    <button onClick$={prev} class="text-white/40 hover:text-white transition-all scale-125">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                        </svg>
                    </button>

                    <div class="flex items-center gap-2 lg:gap-3 py-2 px-4 bg-white/[0.02] rounded-xl border border-white/5">
                        {team.map((member, index) => (
                            <button
                                key={member.name}
                                onClick$={() => setIndex(index)}
                                class={`relative w-10 h-10 lg:w-12 lg:h-12 rounded-lg overflow-hidden transition-all duration-300 ${
                                    currentIndex.value === index ? `ring-2 ${member.ringClass} scale-110 opacity-100` : 'opacity-40 grayscale hover:opacity-100'
                                }`}
                            >
                                <img src={`https://mc-heads.net/avatar/${member.name}/100`} alt={member.name} class="w-full h-full object-cover" />
                            </button>
                        ))}
                    </div>

                    <button onClick$={next} class="text-white/40 hover:text-white transition-all scale-125">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                        </svg>
                    </button>
                </div>
            </div>

            {/* PRAWE OKNO */}
            <div class={`lg:col-span-5 bg-gradient-to-br ${active.theme} backdrop-blur-3xl border ${active.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] relative overflow-hidden min-h-[400px] flex items-center justify-center ${active.glowClass}`}>
                <div key={active.name} class="absolute inset-0 flex items-center justify-center p-10 slide-anim">
                    <img src={`https://mc-heads.net/body/${active.name}/400`} alt={active.name} class="h-[90%] w-auto object-contain drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] scale-x-[-1]" />
                </div>
            </div>
        </div>
    );
});