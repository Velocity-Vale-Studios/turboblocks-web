// colors.js is intentionally not imported here; team colors come from server-provided data-member payload

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
        number: document.getElementById('m-number'),
        tTarget: document.getElementById('text-anim-target'),
        vTarget: document.getElementById('visual-anim-target')
        ,
        // header & card accents
        headerLeft: document.getElementById('header-left-line'),
        headerLabel: document.getElementById('header-label'),
        headerRight: document.getElementById('header-right-line'),
        headerCrew: document.getElementById('header-crew'),
        leftStripe: document.getElementById('left-stripe'),
        arcadeDot: document.getElementById('arcade-dot'),
        arcadeLabel: document.getElementById('arcade-label'),
        mLine: document.getElementById('m-line'),
        star: document.getElementById('m-star'),
        nameplateNeon: document.getElementById('nameplate-neon')
    };

    function update(idx, isManual = false) {
        currentIndex = idx;
        const btn = triggers[idx];
        const data = JSON.parse(btn.getAttribute('data-member'));

        // 1. UI Reset & Active state
        triggers.forEach(t => {
            t.setAttribute('data-active', 'false');
            t.style.boxShadow = '';
            t.style.outline = '';

            // also reset avatar visual classes (server render marks first as active)
            try {
                const avatar = t.querySelector(':scope > div');
                if (avatar) {
                    avatar.classList.remove('opacity-100', 'grayscale-0');
                    avatar.classList.add('opacity-40', 'grayscale');
                }
            } catch (e) {
                // :scope selector may not be supported in very old browsers; ignore safely
            }
        });

        // set active styles on the selected trigger
        btn.setAttribute('data-active', 'true');
        btn.style.outline = `2px solid ${data.hex}`;
        btn.style.outlineOffset = '2px';
        btn.style.boxShadow = `0 0 12px ${data.hex}`;

        // ensure the selected avatar is full-opacity / color
        try {
            const activeAvatar = btn.querySelector(':scope > div');
            if (activeAvatar) {
                activeAvatar.classList.remove('opacity-40', 'grayscale');
                activeAvatar.classList.add('opacity-100', 'grayscale-0');
            }
        } catch (e) {
            // ignore
        }

        // 2. Restart animations
        [elements.tTarget, elements.vTarget].forEach(el => {
            if (!el) return;
            el.classList.remove('slide-anim');
            void el.offsetWidth;
            el.classList.add('slide-anim');
        });

        // 3. Outer wrappers
        elements.info.className = `lg:col-span-7 bg-gradient-to-br from-white/5 to-white/[0.02] border ${data.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] p-6 lg:p-12 backdrop-blur-3xl flex flex-col justify-center relative overflow-hidden group ${data.glowClass} transition-all duration-700`;
        elements.visual.className = `lg:col-span-5 bg-gradient-${data.gradient} backdrop-blur-3xl border ${data.borderColorClass} rounded-[2rem] lg:rounded-[3.5rem] relative overflow-hidden min-h-[400px] lg:min-h-[600px] flex items-center justify-center ${data.glowClass} transition-all duration-700`;
        elements.ambient.className = `absolute -top-24 -right-24 w-96 h-96 bg-gradient-${data.gradient}-diag blur-[100px] opacity-20 transition-all duration-1000 pointer-events-none`;

        // 3b. header & card inline accents — removed direct inline updates to avoid desynchronization
        // these accents now rely on the centralized CSS variables (--team-hex / --team-rgb).
        if (elements.star) {
            // replace star glyph with player's avatar head
            try {
                elements.star.src = `https://mc-heads.net/avatar/${data.name}/80`;
                elements.star.alt = data.name;
            } catch (e) {
                // ignore if element is not an <img>
            }
        }
        // 3c. set centralized CSS variables on root so many accents update together
        const root = document.getElementById('team');
        if (root) {
            root.style.setProperty('--team-hex', data.hex);
            root.style.setProperty('--team-rgb', data.rgb);
            root.style.setProperty('--team-gradient', data.gradient);
        }
        // nameplateNeon now uses CSS variable; avoid direct inline updates to keep timing consistent

        // trigger a short accent animation on elements to highlight the color change
        try {
            const animateEls = [elements.headerCrew, elements.leftStripe, elements.mLine, elements.headerLeft, elements.headerRight, elements.arcadeDot, elements.vLine1, elements.nameplateNeon];
            animateEls.forEach(el => { if (el) el.classList.add('accent-change'); });
            // remove class after animation duration (match CSS -- 700ms)
            setTimeout(() => animateEls.forEach(el => { if (el) el.classList.remove('accent-change'); }), 750);
        } catch (e) { /* ignore */ }

        // 4. Text content
        elements.name.innerText = data.name;
        elements.vName.innerText = data.name;
        elements.vRole.innerText = data.role;
        elements.quote.innerText = `"${data.quote}"`;

        // 5. Role with neon color (now uses CSS variable; just set text)
        if (elements.role) elements.role.innerText = data.role;

        // 6. Racing number
        if (elements.number) {
            elements.number.innerText = String(idx + 1).padStart(2, '0');
            // color is driven by CSS variable now
        }

        // 7. Left racing stripe (v-line-1 = quote border) — visual driven by CSS variable

        // 8. Skin drop shadow
        elements.body.src = `https://mc-heads.net/body/${data.name}/400`;
        elements.body.style.filter = `drop-shadow(0 0 35px rgba(${data.rgb}, 0.65)) drop-shadow(0 0 12px white)`;

        if (isManual) startAutoCycle();
    }

    function startAutoCycle() {
        clearInterval(autoCycleInterval);
        autoCycleInterval = setInterval(() => {
            update((currentIndex + 1) % totalMembers);
        }, 15000);
    }

    triggers.forEach((b, i) => b.addEventListener('click', () => update(i, true)));
    prevBtn?.addEventListener('click', () => update((currentIndex - 1 + totalMembers) % totalMembers, true));
    nextBtn?.addEventListener('click', () => update((currentIndex + 1) % totalMembers, true));

    startAutoCycle();
}