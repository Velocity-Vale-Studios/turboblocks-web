import { colorMap } from './colors.js';

// Upewniamy się, że skrypt uruchomi się poprawnie, jeśli na stronie są triggery
const triggers = document.querySelectorAll('.team-trigger');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

if (triggers.length > 0) {
    let currentIndex = 0;
    const totalMembers = triggers.length;
    let autoCycleInterval;

    const elements = {
        info: document.getElementById('info-window'),
        visual: document.getElementById('visual-window'),
        ambient: document.getElementById('ambient-glow'),
        name: document.getElementById('m-name'),
        role: document.getElementById('m-role'),
        quote: document.getElementById('m-quote'),
        body: document.getElementById('m-body'),
        vName: document.getElementById('m-visual-name'),
        vRole: document.getElementById('m-visual-role'),
        vLine1: document.getElementById('v-line-1'),
        vLine2: document.getElementById('v-line-2'),
        tTarget: document.getElementById('text-anim-target'),
        vTarget: document.getElementById('visual-anim-target')
    };

    function update(idx, isManual = false) {
        currentIndex = idx;
        const btn = triggers[idx];
        const data = JSON.parse(btn.getAttribute('data-member'));
        const color = data.textClass.split('-')[1];

        // 1. UI Reset & Active state
        triggers.forEach(t => {
            t.setAttribute('data-active', 'false');
            t.classList.remove('ring-pink-500', 'ring-blue-500', 'ring-emerald-500', 'ring-orange-500', 'ring-violet-500');
        });
        btn.setAttribute('data-active', 'true');
        btn.classList.add(data.ringClass);

        // 2. Restart Animations
        [elements.tTarget, elements.vTarget].forEach(el => {
            el.classList.remove('slide-anim');
            void el.offsetWidth; // Trigger reflow
            el.classList.add('slide-anim');
        });

        // 3. Update Styles & Content
        elements.info.className = `lg:col-span-7 bg-gradient-to-br from-white/5 to-white/[0.02] border ${data.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] p-6 lg:p-12 backdrop-blur-3xl flex flex-col justify-center relative overflow-hidden group ${data.glowClass} transition-all duration-700`;
        elements.visual.className = `lg:col-span-5 bg-gradient-to-br ${data.theme} backdrop-blur-3xl border ${data.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] relative overflow-hidden min-h-[400px] lg:min-h-[600px] flex items-center justify-center ${data.glowClass} transition-all duration-700`;
        elements.ambient.className = `absolute -top-24 -right-24 w-96 h-96 bg-gradient-to-br ${data.theme} blur-[100px] opacity-20 transition-all duration-1000 pointer-events-none`;

        elements.name.innerText = data.name;
        elements.vName.innerText = data.name;
        elements.role.innerText = data.role;
        elements.role.className = `${data.textClass} font-black text-[10px] lg:text-xs uppercase tracking-[0.3em] mb-4 lg:mb-8`;
        elements.quote.innerText = `"${data.quote}"`;
        elements.quote.className = `text-white/60 text-base lg:text-lg italic font-medium border-l-4 ${data.borderClass} pl-4 lg:pl-6 max-w-lg leading-relaxed line-clamp-2 lg:line-clamp-3`;
        elements.body.src = `https://mc-heads.net/body/${data.name}/400`;
        elements.body.style.filter = `drop-shadow(0 0 40px ${colorMap[color]}) drop-shadow(0 0 10px white)`;
        elements.vRole.innerText = data.role;
        elements.vLine1.className = `h-[2px] w-6 lg:w-8 ${data.bgClass}`;
        elements.vLine2.className = `h-[2px] w-6 lg:w-8 ${data.bgClass}`;

        if (isManual) startAutoCycle();
    }

    function startAutoCycle() {
        clearInterval(autoCycleInterval);
        autoCycleInterval = setInterval(() => {
            let nextIdx = (currentIndex + 1) % totalMembers;
            update(nextIdx);
        }, 15000);
    }

    triggers.forEach((b, i) => b.addEventListener('click', () => update(i, true)));

    prevBtn?.addEventListener('click', () => {
        let prevIdx = (currentIndex - 1 + totalMembers) % totalMembers;
        update(prevIdx, true);
    });

    nextBtn?.addEventListener('click', () => {
        let nextIdx = (currentIndex + 1) % totalMembers;
        update(nextIdx, true);
    });

    startAutoCycle();
}