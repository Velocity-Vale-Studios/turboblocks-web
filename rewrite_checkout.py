import os
import re

FILE_PATH = r"s:\turboblocks-web\src\pages\checkout.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

new_header = """
        {/* Progress Bar Header */}
        <div class="mb-10 md:mb-16 relative z-10 w-full max-w-4xl mx-auto hidden sm:block">
            <div class="flex items-center justify-between relative">
                <!-- Line background -->
                <div class="absolute left-0 top-1/2 -translate-y-1/2 w-full h-px bg-white/10 -z-10"></div>
                <!-- Line progress -->
                <div id="progress-line" class="absolute left-0 top-1/2 -translate-y-1/2 h-px bg-fuchsia-500 -z-10 transition-all duration-500 w-0"></div>
                
                <!-- Steps -->
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="0">
                    <div class="step-circle w-8 h-8 rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black font-bold text-xs transition-colors shadow-[0_0_15px_rgba(217,70,239,0.5)]">
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    </div>
                    <span class="text-[10px] uppercase font-black tracking-widest text-white">Koszyk</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="1">
                    <div class="step-circle w-8 h-8 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/50 font-bold text-xs transition-colors">2</div>
                    <span class="text-[10px] uppercase font-black tracking-widest text-white/50 text-center max-w-[80px]">Dane gracza</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="2">
                    <div class="step-circle w-8 h-8 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/50 font-bold text-xs transition-colors">3</div>
                    <span class="text-[10px] uppercase font-black tracking-widest text-white/50 text-center max-w-[80px]">Płatność</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="3">
                    <div class="step-circle w-8 h-8 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/50 font-bold text-xs transition-colors">4</div>
                    <span class="text-[10px] uppercase font-black tracking-widest text-white/50 text-center max-w-[80px]">Gotowe</span>
                </div>
            </div>
        </div>
        
        {/* Mobile Title */}
        <div class="mb-8 flex flex-col items-center text-center relative z-10 sm:hidden">
            <h1 id="page-title" class="text-4xl font-black italic text-white uppercase tracking-tighter leading-none">
                KOSZ<span class="neon-text-animated pr-4" style="background-image: linear-gradient(to right, #ec4899, #a855f7, #22d3ee); filter: drop-shadow(0 0 20px rgba(236,72,153,0.3));">YK</span>
            </h1>
        </div>
"""

content = re.sub(r'\{\/\* Header \*\/\}.*?<\/h1>\s*<\/div>', new_header, content, flags=re.DOTALL)

login_section = """
                {/* Stage 1: Login / Details (Hidden by default) */}
                <section id="login-section" style="--theme-hex: #a855f7; --theme-rgb: 168,85,247;" class="hidden group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-3xl rounded-[2.5rem] p-6 md:p-8 border-[rgba(var(--theme-rgb),0.3)] shadow-[0_0_50px_rgba(var(--theme-rgb),0.2)] hover:shadow-[0_0_80px_rgba(var(--theme-rgb),0.3)] transition-all duration-700">
                    {/* Bloom */}
                    <div class="absolute -inset-[40px] rounded-[2.5rem] blur-[60px] -z-10 pointer-events-none transition-all duration-1000 opacity-10 group-hover:opacity-20" style={`background-image: linear-gradient(to bottom right, #a855f7, #ec4899);`}></div>
                    <div class="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-purple-500/40 to-transparent"></div>
                    
                    <h2 class="text-xl font-black text-white uppercase italic tracking-tighter mb-2">Twoje Dane</h2>
                    <p class="text-xs text-white/50 font-bold mb-6">Podaj swój nick z gry oraz email, abyśmy mogli zrealizować zamówienie i przypisać je do Twojego konta.</p>
                    
                    <div class="space-y-4">
                        <div class="space-y-1.5">
                            <label for="player-nick" class="text-[10px] font-black text-white/70 uppercase tracking-widest pl-1">Nick z gry (Minecraft)</label>
                            <div class="relative">
                                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-white/20">🎮</span>
                                <input type="text" id="player-nick" placeholder="Np. Notch" class="w-full pl-10 pr-4 py-3 bg-black/40 border border-white/10 rounded-xl text-white text-sm font-bold placeholder-white/20 focus:outline-none focus:border-purple-500/50 focus:bg-white/5 transition-all" />
                            </div>
                        </div>
                        
                        <div class="space-y-1.5">
                            <label for="player-email" class="text-[10px] font-black text-white/70 uppercase tracking-widest pl-1">Adres E-mail</label>
                            <div class="relative">
                                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-white/20">✉️</span>
                                <input type="email" id="player-email" placeholder="twoj@email.com" class="w-full pl-10 pr-4 py-3 bg-black/40 border border-white/10 rounded-xl text-white text-sm font-bold placeholder-white/20 focus:outline-none focus:border-purple-500/50 focus:bg-white/5 transition-all" />
                            </div>
                        </div>
                    </div>
                </section>
                
                {/* Stage 3: Summary Success (Hidden by default) */}
                <section id="success-section" style="--theme-hex: #22c55e; --theme-rgb: 34,197,94;" class="hidden group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-3xl rounded-[2.5rem] p-10 border-[rgba(var(--theme-rgb),0.3)] shadow-[0_0_50px_rgba(var(--theme-rgb),0.2)] text-center transition-all duration-700">
                    <div class="absolute -inset-[40px] rounded-[2.5rem] blur-[60px] -z-10 pointer-events-none opacity-20" style={`background-image: linear-gradient(to bottom right, #22c55e, #10b981);`}></div>
                    
                    <div class="w-20 h-20 mx-auto bg-green-500/20 border border-green-500/50 rounded-full flex items-center justify-center text-4xl mb-6 shadow-[0_0_30px_rgba(34,197,94,0.3)]">
                        ✅
                    </div>
                    <h2 class="text-3xl font-black text-white uppercase italic tracking-tighter mb-2">Płatność Zakończona</h2>
                    <p class="text-sm text-white/70 font-bold mb-8">Dziękujemy za zakup! Przedmioty wkrótce pojawią się na Twoim koncie. Potwierdzenie wysłano na email.</p>
                    <a href="/" class="inline-block px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-black uppercase tracking-[0.2em] text-[10px] rounded-2xl transition-colors border border-white/10">Wróć na stronę główną</a>
                </section>
"""

content = content.replace("</section>\n            </div>\n\n            {/* ===== RIGHT COLUMN: SUMMARY + PAYMENT ===== */}", "</section>\n" + login_section + "            </div>\n\n            {/* ===== RIGHT COLUMN: SUMMARY + PAYMENT ===== */}")

js_replacement = """
<script is:inline>
    const CART_KEY = 'turbo_cart_v1';
    let selectedMethod = null;
    let activeCreatorCode = null;
    let activeDiscountPercent = 0;
    let currentStage = 0; // 0: Cart, 1: Login, 2: Payment, 3: Success

    function getCart() {
        return JSON.parse(localStorage.getItem(CART_KEY) || '[]');
    }
    function saveCartData(cart) {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
        if (window.cart) window.cart = cart;
    }

    window.ckRemove = function(index) {
        const cart = getCart();
        cart.splice(index, 1);
        saveCartData(cart);
        renderCheckout();
    };

    function updateProgressUI() {
        const line = document.getElementById('progress-line');
        if (line) {
            if(currentStage === 0) line.style.width = '0%';
            else if(currentStage === 1) line.style.width = '33%';
            else if(currentStage === 2) line.style.width = '66%';
            else if(currentStage === 3) line.style.width = '100%';
        }
        
        document.querySelectorAll('.step-indicator').forEach(ind => {
            const step = parseInt(ind.getAttribute('data-step'));
            const circle = ind.querySelector('.step-circle');
            const text = ind.querySelector('span');
            
            if (step < currentStage) {
                // completed
                circle.className = 'step-circle w-8 h-8 rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black font-bold text-xs transition-colors shadow-[0_0_15px_rgba(217,70,239,0.5)]';
                circle.innerHTML = '<svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>';
                text.className = 'text-[10px] uppercase font-black tracking-widest text-white text-center max-w-[80px]';
            } else if (step === currentStage) {
                // current
                circle.className = 'step-circle w-8 h-8 rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black font-bold text-xs transition-colors shadow-[0_0_15px_rgba(217,70,239,0.5)]';
                circle.innerHTML = (step + 1);
                text.className = 'text-[10px] uppercase font-black tracking-widest text-white text-center max-w-[80px]';
            } else {
                // future
                circle.className = 'step-circle w-8 h-8 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/50 font-bold text-xs transition-colors';
                circle.innerHTML = (step + 1);
                text.className = 'text-[10px] uppercase font-black tracking-widest text-white/50 text-center max-w-[80px]';
            }
        });
        
        // Hide/Show sections
        const cartSec = document.querySelector('.lg\\\\:col-span-7 section:first-of-type');
        const loginSec = document.getElementById('login-section');
        const paySec = document.getElementById('payment-method-section');
        const successSec = document.getElementById('success-section');
        const summarySec = document.querySelector('.lg\\\\:col-span-5');
        const pageTitle = document.getElementById('page-title');
        
        if (cartSec) cartSec.classList.add('hidden');
        if (loginSec) loginSec.classList.add('hidden');
        if (paySec) paySec.classList.add('hidden');
        if (successSec) successSec.classList.add('hidden');
        
        if (currentStage === 0) {
            if(cartSec) cartSec.classList.remove('hidden');
            if(summarySec) summarySec.style.display = '';
            if(pageTitle) pageTitle.innerHTML = 'KOSZ<span class="neon-text-animated pr-4" style="background-image: linear-gradient(to right, #ec4899, #a855f7, #22d3ee); filter: drop-shadow(0 0 20px rgba(236,72,153,0.3));">YK</span>';
        } else if (currentStage === 1) {
            if(loginSec) loginSec.classList.remove('hidden');
            if(summarySec) summarySec.style.display = '';
            if(pageTitle) pageTitle.innerHTML = 'DA<span class="neon-text-animated pr-4" style="background-image: linear-gradient(to right, #ec4899, #a855f7, #22d3ee); filter: drop-shadow(0 0 20px rgba(236,72,153,0.3));">NE</span>';
        } else if (currentStage === 2) {
            if(paySec) paySec.classList.remove('hidden');
            if(summarySec) summarySec.style.display = '';
            if(pageTitle) pageTitle.innerHTML = 'CHECK<span class="neon-text-animated pr-4" style="background-image: linear-gradient(to right, #ec4899, #a855f7, #22d3ee); filter: drop-shadow(0 0 20px rgba(236,72,153,0.3));">OUT</span>';
        } else if (currentStage === 3) {
            if(successSec) successSec.classList.remove('hidden');
            if(summarySec) summarySec.style.display = 'none'; // hide right column on success
            if(pageTitle) pageTitle.innerHTML = 'GOTO<span class="neon-text-animated pr-4" style="background-image: linear-gradient(to right, #ec4899, #a855f7, #22d3ee); filter: drop-shadow(0 0 20px rgba(236,72,153,0.3));">WE</span>';
        }
    }

    function renderCheckout() {
        const cart = getCart();
        const list = document.getElementById('ck-list');
        const countEl = document.getElementById('ck-count');
        const subtotalEl = document.getElementById('ck-subtotal');
        const subtotalPlnEl = document.getElementById('ck-subtotal-fiat');
        const totalEl = document.getElementById('ck-total');
        const totalPlnEl = document.getElementById('ck-total-fiat');
        const discountAmountEl = document.getElementById('ck-discount-amount');
        if (!list) return;

        const parseTc = (item) => {
            if (item.isCoinPack || item.type === 'Coin Pack') return 0;
            if (typeof item.priceTc === 'number') return item.priceTc;
            return parseInt(String(item.price || '').replace(/[^0-9]/g, ''), 10) || 0;
        };
        const parseAmountTc = (item) => {
            if (typeof item.amountTc === 'number') return item.amountTc;
            if (typeof item.tcAmount === 'number') return item.tcAmount;
            return parseInt(String(item.price || '').replace(/[^0-9]/g, ''), 10) || 0;
        };
        const currencySelect = document.getElementById('checkout-currency');
        const activeCurrency = currencySelect ? currencySelect.value : 'PLN';
        const currencySymbols = { 'PLN': 'zł', 'EUR': '€', 'USD': '$' };
        const sym = currencySymbols[activeCurrency] || '';

        const parseFiat = (item) => {
            if (activeCurrency === 'PLN') return typeof item.cashPricePln === 'number' ? item.cashPricePln : (typeof item.pricePln === 'number' ? item.pricePln : 0);
            if (activeCurrency === 'EUR') return typeof item.cashPriceEur === 'number' ? item.cashPriceEur : 0;
            if (activeCurrency === 'USD') return typeof item.cashPriceUsd === 'number' ? item.cashPriceUsd : 0;
            return 0;
        };

        const n = cart.length;
        if (countEl) countEl.innerText = n === 0 ? '0' : n === 1 ? '1 przedmiot' : n + ' przedmioty';

        document.querySelectorAll('.fiat-label').forEach(el => el.innerText = activeCurrency);

        if (n === 0) {
            list.innerHTML = '<div class="flex flex-col items-center justify-center text-center opacity-40 py-12"><span class="text-5xl mb-4 grayscale">🛒</span><p class="text-white italic uppercase text-[10px] font-black tracking-widest">Twój koszyk jest pusty</p><a href="/shop" class="mt-4 text-[9px] font-black text-cyan-400 uppercase tracking-widest hover:text-white transition-colors">Przejdź do sklepu →</a></div>';
            if (subtotalEl) subtotalEl.innerText = '0 TC';
            if (totalEl) totalEl.innerText = '0 TC';
            if (subtotalPlnEl) subtotalPlnEl.innerText = '0.00 ' + sym;
            if (totalPlnEl) totalPlnEl.innerText = '0.00 ' + sym;
            updatePayBtn();
            return;
        }

        list.innerHTML = '';
        let totalTc = 0;
        let totalFiat = 0;

        cart.forEach(function(item, index) {
            const isCoinPack = item.isCoinPack || item.type === 'Coin Pack';
            const priceTc = parseTc(item);
            const amountTc = parseAmountTc(item);
            
            let priceFiat = parseFiat(item);
            
            if (priceFiat === 0 && isCoinPack) {
                 const normalized = String(item.cashPrice || '').replace(',', '.');
                 const matched = normalized.match(/[0-9]+(\\.[0-9]+)?/);
                 if (activeCurrency === 'PLN' && matched) priceFiat = parseFloat(matched[0]);
            }

            totalTc += priceTc;
            totalFiat += priceFiat;
            const hasFiat = priceFiat > 0;
            
            const tcPill = !isCoinPack
                ? ('<span class="text-[9px] font-bold text-pink-400 uppercase tracking-widest bg-pink-400/10 px-2 py-0.5 rounded-md border border-pink-400/20">' + (priceTc || 0) + ' TC</span>')
                : '';
            const fiatPill = hasFiat
                ? ('<span class="text-[9px] font-bold text-amber-300 tracking-widest bg-amber-300/10 px-2 py-0.5 rounded-md border border-amber-300/20">' + priceFiat.toFixed(2) + ' ' + sym + '</span>')
                : '';
            const amountLabel = isCoinPack && amountTc > 0
                ? ('<p class="text-[8px] text-cyan-300/90 font-black uppercase tracking-widest mt-1.5 border-l-2 border-cyan-400/30 pl-2">Otrzymujesz ' + amountTc + ' TC</p>')
                : '';
            const el = document.createElement('div');
            el.className = 'flex items-center gap-4 bg-black/40 border border-white/5 p-4 rounded-2xl backdrop-blur-md transition-all hover:bg-white/5 hover:border-white/10 group/item';
            el.innerHTML = '<div class="w-14 h-14 bg-gradient-to-br from-white/10 to-transparent rounded-xl flex items-center justify-center text-2xl border border-white/5 shrink-0 shadow-lg group-hover/item:scale-110 transition-transform">' + (item.icon||'📦') + '</div>'
                + '<div class="flex-grow overflow-hidden">'
                + '<p class="text-[11px] sm:text-xs font-black text-white uppercase italic tracking-tighter truncate">' + item.name + '</p>'
                + '<div class="flex items-center gap-2 mt-1.5">'
                + tcPill
                + fiatPill
                + '<span class="text-[8px] text-white/30 font-bold uppercase tracking-widest">' + (item.rarity||'') + '</span>'
                + '</div>' + amountLabel + '</div>'
                + '<button type="button" aria-label="Remove item from checkout" onclick="ckRemove(' + index + ')" class="w-10 h-10 rounded-xl flex items-center justify-center text-white/20 bg-white/5 border border-white/5 hover:text-red-400 hover:bg-red-400/10 hover:border-red-400/20 transition-all shrink-0">'
                + '<svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg></button>';
            list.appendChild(el);
        });

        const discountRow = document.getElementById('discount-row');
        if (activeDiscountPercent > 0) {
            const tcDiscount = Math.floor(totalTc * (activeDiscountPercent / 100));
            const fiatDiscount = totalFiat * (activeDiscountPercent / 100);
            
            totalTc -= tcDiscount;
            totalFiat -= fiatDiscount;
            
            if (discountRow) discountRow.classList.remove('hidden');
            if (discountAmountEl) {
                discountAmountEl.innerText = `-${activeDiscountPercent}% (-${tcDiscount} TC / -${fiatDiscount.toFixed(2)} ${sym})`;
            }
        } else {
            if (discountRow) discountRow.classList.add('hidden');
            if (discountAmountEl) {
                discountAmountEl.innerText = '-0 TC';
            }
        }

        if (subtotalEl) subtotalEl.innerText = totalTc + ' TC';
        if (totalEl) totalEl.innerText = totalTc + ' TC';
        if (subtotalPlnEl) subtotalPlnEl.innerText = totalFiat.toFixed(2) + ' ' + sym;
        if (totalPlnEl) totalPlnEl.innerText = totalFiat.toFixed(2) + ' ' + sym;
        
        updatePayBtn();
    }

    function initPaymentMethods() {
        var methods = document.querySelectorAll('.pay-method');
        var label = document.getElementById('selected-method-label');
        var names = { blik: 'BLIK', paypal: 'PayPal', card: 'Karta płatnicza', turbocoins: 'TurboCoins' };

        methods.forEach(function(btn) {
            btn.addEventListener('click', function() {
                selectedMethod = btn.getAttribute('data-method');
                methods.forEach(function(b) {
                    b.classList.remove('border-pink-500/50', 'bg-pink-500/10', 'border-cyan-500/50', 'bg-cyan-500/10', 'border-purple-500/50', 'bg-purple-500/10', 'border-blue-500/50', 'bg-blue-500/10');
                    b.classList.add('border-white/10', 'bg-black/40');
                });
                btn.classList.remove('border-white/10', 'bg-black/40');
                if (selectedMethod === 'blik') { btn.classList.add('border-pink-500/50', 'bg-pink-500/10'); }
                else if (selectedMethod === 'paypal') { btn.classList.add('border-blue-500/50', 'bg-blue-500/10'); }
                else if (selectedMethod === 'card') { btn.classList.add('border-purple-500/50', 'bg-purple-500/10'); }
                else if (selectedMethod === 'turbocoins') { btn.classList.add('border-cyan-500/50', 'bg-cyan-500/10'); }

                if (label) label.innerText = 'Wybrano: ' + (names[selectedMethod] || selectedMethod);
                updatePayBtn();
            });
        });
    }

    function updatePayBtn() {
        var btn = document.getElementById('ck-pay-btn');
        if (!btn) return;
        var cart = getCart();
        var hasItems = cart.length > 0;
        var hasMethod = !!selectedMethod;

        if (currentStage === 0) {
            if (hasItems) {
                btn.disabled = false;
                btn.className = 'relative overflow-hidden w-full py-5 rounded-[1.5rem] bg-pink-500 text-white font-black uppercase tracking-[0.2em] text-[10px] shadow-[0_0_30px_rgba(236,72,153,0.4)] hover:shadow-[0_0_60px_rgba(236,72,153,0.6)] transition-all duration-300 active:scale-95 flex items-center justify-center gap-3 border border-pink-400 hover:border-pink-300 cursor-pointer group/pay';
                btn.innerHTML = '<span class="relative z-10">Dalej: Dane</span><span class="relative z-10 group-hover/pay:translate-x-1 transition-transform">→</span>';
            } else {
                btn.disabled = true;
                btn.className = 'w-full py-5 rounded-[1.5rem] bg-white/5 text-white/20 font-black uppercase tracking-[0.2em] text-[10px] cursor-not-allowed flex items-center justify-center gap-3 transition-all duration-500 border border-white/10';
                btn.innerHTML = '<span>Koszyk pusty</span>';
            }
        } else if (currentStage === 1) {
            btn.disabled = false;
            btn.className = 'relative overflow-hidden w-full py-5 rounded-[1.5rem] bg-purple-500 text-white font-black uppercase tracking-[0.2em] text-[10px] shadow-[0_0_30px_rgba(168,85,247,0.4)] hover:shadow-[0_0_60px_rgba(168,85,247,0.6)] transition-all duration-300 active:scale-95 flex items-center justify-center gap-3 border border-purple-400 hover:border-purple-300 cursor-pointer group/pay';
            btn.innerHTML = '<span class="relative z-10">Dalej: Płatność</span><span class="relative z-10 group-hover/pay:translate-x-1 transition-transform">→</span>';
        } else if (currentStage === 2) {
            if (hasItems && hasMethod) {
                btn.disabled = false;
                btn.className = 'relative overflow-hidden w-full py-5 rounded-[1.5rem] bg-cyan-500 text-white font-black uppercase tracking-[0.2em] text-[10px] shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:shadow-[0_0_60px_rgba(34,211,238,0.6)] transition-all duration-300 active:scale-95 flex items-center justify-center gap-3 border border-cyan-400 hover:border-cyan-300 cursor-pointer group/pay';
                var names = { blik: 'BLIK', paypal: 'PayPal', card: 'Karty', turbocoins: 'TurboCoins' };
                btn.innerHTML = '<span class="relative z-10">Zapłać przez ' + (names[selectedMethod]||'') + '</span><span class="relative z-10 group-hover/pay:translate-x-1 transition-transform">→</span>';
            } else if (hasItems && !hasMethod) {
                btn.disabled = true;
                btn.className = 'w-full py-5 rounded-[1.5rem] bg-white/5 text-white/20 font-black uppercase tracking-[0.2em] text-[10px] cursor-not-allowed flex items-center justify-center gap-3 transition-all duration-500 border border-white/10';
                btn.innerHTML = '<span>Wybierz metodę płatności</span>';
            }
        }
    }

    renderCheckout();
    initPaymentMethods();
    updateProgressUI();

    const discountInput = document.getElementById('discount-code-input');
    const applyDiscountBtn = document.getElementById('apply-discount-btn');
    if (applyDiscountBtn && discountInput) {
        applyDiscountBtn.addEventListener('click', async () => {
            const code = discountInput.value.trim();
            if (!code) {
                activeCreatorCode = null;
                activeDiscountPercent = 0;
                discountInput.classList.remove('border-green-500', 'border-red-500');
                renderCheckout();
                return;
            }
            
            applyDiscountBtn.disabled = true;
            applyDiscountBtn.innerText = '...';

            const checkoutApp = document.getElementById('checkout-app');
            const apiUrl = checkoutApp ? checkoutApp.dataset.apiUrl : "http://localhost:8000";

            try {
                const res = await fetch(`${apiUrl}/creators/codes/validate?code=${code}`);
                const data = await res.json();
                
                if (data.valid) {
                    activeCreatorCode = code.toUpperCase();
                    activeDiscountPercent = data.discount;
                    discountInput.classList.remove('border-red-500');
                    discountInput.classList.add('border-green-500');
                    alert(`Zastosowano kod! Otrzymujesz ${data.discount}% zniżki.`);
                    renderCheckout();
                } else {
                    activeCreatorCode = null;
                    activeDiscountPercent = 0;
                    discountInput.classList.remove('border-green-500');
                    discountInput.classList.add('border-red-500');
                    alert(data.message || 'Kod jest nieprawidłowy.');
                    renderCheckout();
                }
            } catch (e) {
                console.error(e);
            } finally {
                applyDiscountBtn.disabled = false;
                applyDiscountBtn.innerText = 'OK';
            }
        });
    }

    const currencySelect = document.getElementById('checkout-currency');
    if (currencySelect) {
        currencySelect.addEventListener('change', renderCheckout);
    }

    const payBtn = document.getElementById('ck-pay-btn');
    if (payBtn) {
        payBtn.addEventListener('click', async () => {
            const cart = getCart();
            if (cart.length === 0) return;

            if (currentStage === 0) {
                currentStage = 1;
                updateProgressUI();
                updatePayBtn();
                return;
            }
            
            if (currentStage === 1) {
                const nickInput = document.getElementById('player-nick');
                const emailInput = document.getElementById('player-email');
                if (!nickInput.value.trim() || !emailInput.value.trim() || !emailInput.value.includes('@')) {
                    alert("Proszę podać poprawny nick z gry oraz adres email.");
                    return;
                }
                currentStage = 2;
                updateProgressUI();
                updatePayBtn();
                return;
            }

            if (!selectedMethod) return;

            payBtn.disabled = true;
            payBtn.innerHTML = '<span>Przetwarzanie...</span>';

            const checkoutApp = document.getElementById('checkout-app');
            const apiUrl = checkoutApp ? checkoutApp.dataset.apiUrl : "http://localhost:8000";
            const activeCurrency = currencySelect ? currencySelect.value : 'PLN';
            
            const nick = document.getElementById('player-nick').value.trim();
            const email = document.getElementById('player-email').value.trim();
            
            const promises = cart.map(item => {
                let amount = 0;
                let currency = 'TC';

                if (selectedMethod === 'turbocoins') {
                    amount = item.priceTc || 0;
                } else {
                    currency = activeCurrency;
                    if (typeof item.prices !== 'undefined') {
                        const priceObj = item.prices.find(p => p.currency === activeCurrency);
                        amount = priceObj ? priceObj.final_price : 0;
                    } else if (typeof item.pricePln === 'number') {
                        amount = item.pricePln;
                    } else if (typeof item.cashPricePln === 'number' && activeCurrency === 'PLN') {
                        amount = item.cashPricePln;
                    }
                }

                return fetch(`${apiUrl}/shop/transactions/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        player_username: nick,
                        email: email,
                        item_name: item.name,
                        amount: amount,
                        currency: currency,
                        payment_method: selectedMethod,
                        creator_code: activeCreatorCode
                    })
                });
            });

            try {
                await Promise.all(promises);
                localStorage.setItem('tb_cart', JSON.stringify([]));
                if (window.cart) window.cart = [];
                window.dispatchEvent(new Event('cart:update'));
                
                currentStage = 3;
                updateProgressUI();
                
            } catch (e) {
                console.error(e);
                alert("Wystąpił błąd podczas płatności.");
                payBtn.disabled = false;
                payBtn.innerHTML = '<span>Spróbuj ponownie</span>';
            }
        });
    }
</script>
"""

content = re.sub(r'<script is:inline>.*?</script>', js_replacement, content, flags=re.DOTALL)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Checkout modified.")
