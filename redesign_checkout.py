import os
import re

FILE_PATH = r"s:\turboblocks-web\src\pages\checkout.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Cleaner Progress Bar
new_progress_bar = """
        {/* Progress Bar Header */}
        <div class="mb-10 md:mb-16 relative z-10 w-full max-w-3xl mx-auto hidden sm:block">
            <div class="flex items-center justify-between relative px-4">
                <!-- Line background -->
                <div class="absolute left-8 right-8 top-1/2 -translate-y-1/2 h-[2px] bg-white/5 -z-10 rounded-full"></div>
                <!-- Line progress -->
                <div id="progress-line" class="absolute left-8 top-1/2 -translate-y-1/2 h-[2px] bg-gradient-to-r from-fuchsia-500 to-cyan-500 -z-10 transition-all duration-700 w-0 rounded-full shadow-[0_0_10px_rgba(217,70,239,0.5)]"></div>
                
                <!-- Steps -->
                <div class="step-indicator flex flex-col items-center gap-2 relative z-10" data-step="0">
                    <div class="step-circle w-6 h-6 rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black transition-all shadow-[0_0_15px_rgba(217,70,239,0.5)] scale-110">
                        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    </div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white">Koszyk</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-2 relative z-10" data-step="1">
                    <div class="step-circle w-6 h-6 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all">2</div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center">Dane</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-2 relative z-10" data-step="2">
                    <div class="step-circle w-6 h-6 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all">3</div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center">Płatność</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-2 relative z-10" data-step="3">
                    <div class="step-circle w-6 h-6 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all">4</div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center">Gotowe</span>
                </div>
            </div>
        </div>
"""
content = re.sub(r'\{\/\* Progress Bar Header \*\/\}.*?<\/div>\s*<\/div>', new_progress_bar, content, flags=re.DOTALL)

# 2. Cleaner Summary Box
summary_box_regex = r'\{\/\* Summary \*\/\}.*?(<div class="space-y-4 mb-6">)'
new_summary_box = """
                {/* Summary */}
                <section style="--theme-hex: #22d3ee; --theme-rgb: 34,211,238;" class="group relative bg-gradient-to-b from-white/[0.05] to-transparent backdrop-blur-2xl rounded-3xl p-6 md:p-8 border border-white/[0.05] shadow-2xl transition-all duration-700">
                    
                    {/* Bloom */}
                    <div class="absolute -inset-[20px] rounded-3xl blur-[50px] -z-10 pointer-events-none transition-all duration-1000 opacity-5 group-hover:opacity-10" style={`background-image: linear-gradient(to bottom right, #22d3ee, #a855f7);`}></div>
                    <div class="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-cyan-500/20 to-transparent"></div>
                    
                    <h3 class="text-sm font-bold text-white uppercase tracking-widest mb-6 flex items-center gap-3">
                        <span class="w-2 h-2 rounded-full bg-cyan-400 shadow-[0_0_10px_rgba(34,211,238,0.8)]"></span> Podsumowanie
                    </h3>

                    <div class="space-y-4 mb-6">
"""
content = re.sub(summary_box_regex, new_summary_box, content, flags=re.DOTALL)

# 3. Clean up the items UI by changing the JS item template
js_item_template_regex = r"el\.className = 'flex items-center gap-4 bg-black/40 border border-white/5 p-4 rounded-2xl backdrop-blur-md transition-all hover:bg-white/5 hover:border-white/10 group/item';(.*?)list\.appendChild\(el\);"
new_js_item_template = """el.className = 'flex items-center gap-4 py-3 border-b border-white/5 last:border-0 group/item';
            el.innerHTML = '<div class="w-12 h-12 bg-white/5 rounded-xl flex items-center justify-center text-xl shrink-0 group-hover/item:scale-105 transition-transform">' + (item.icon||'📦') + '</div>'
                + '<div class="flex-grow overflow-hidden">'
                + '<p class="text-xs font-bold text-white/90 truncate">' + item.name + '</p>'
                + '<div class="flex items-center gap-2 mt-1">'
                + tcPill
                + fiatPill
                + '</div>' + amountLabel + '</div>'
                + '<button type="button" aria-label="Remove item from checkout" onclick="ckRemove(' + index + ')" class="w-8 h-8 rounded-lg flex items-center justify-center text-white/20 hover:text-red-400 hover:bg-red-400/10 transition-all shrink-0">'
                + '<svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg></button>';
            list.appendChild(el);"""
content = re.sub(js_item_template_regex, new_js_item_template, content, flags=re.DOTALL)

# Also remove uppercase/italic from the summary list
content = content.replace('<span class="text-sm text-white/50 font-medium italic">Przedmioty</span>', '<span class="text-xs text-white/50 font-medium">Przedmioty</span>')
content = content.replace('<span id="ck-subtotal" class="text-sm font-black text-white">0 TC</span>', '<span id="ck-subtotal" class="text-sm font-bold text-white">0 TC</span>')

content = content.replace('<span class="text-sm text-white/50 font-medium italic">Waluta</span>', '<span class="text-xs text-white/50 font-medium">Waluta</span>')

content = content.replace('<span class="text-sm text-white/50 font-medium italic">Przedmioty (PLN)</span>', '<span class="text-xs text-white/50 font-medium">Przedmioty (PLN)</span>')
content = content.replace('<span id="ck-subtotal-fiat" class="text-sm font-black text-amber-400">0.00 zł</span>', '<span id="ck-subtotal-fiat" class="text-sm font-bold text-amber-400">0.00 zł</span>')

content = content.replace('<span class="text-sm text-white/50 font-medium italic">Zniżka</span>', '<span class="text-xs text-white/50 font-medium">Zniżka</span>')
content = content.replace('<span id="ck-discount-amount" class="text-sm font-black text-green-400">-0 TC</span>', '<span id="ck-discount-amount" class="text-sm font-bold text-green-400">-0 TC</span>')

content = content.replace('<span class="text-lg font-black text-white uppercase italic tracking-tighter">SUMA</span>', '<span class="text-sm font-bold text-white/80 uppercase tracking-widest">Do zapłaty</span>')
content = content.replace('<span id="ck-total" class="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500 italic">0 TC</span>', '<span id="ck-total" class="text-xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">0 TC</span>')

content = content.replace('<span class="text-lg font-black text-white uppercase italic tracking-tighter">SUMA (PLN)</span>', '<span class="text-sm font-bold text-white/80 uppercase tracking-widest">Suma (PLN)</span>')
content = content.replace('<span id="ck-total-fiat" class="text-2xl font-black text-amber-400 italic">0.00 zł</span>', '<span id="ck-total-fiat" class="text-xl font-black text-amber-400">0.00 zł</span>')

# Simplify the left container header
content = content.replace('<div class="px-6 py-5 border-b border-white/5 flex justify-between items-center bg-black/20">', '<div class="px-8 py-6 border-b border-white/5 flex justify-between items-center bg-transparent">')
content = content.replace('<span class="text-[10px] font-black text-white/40 uppercase tracking-[0.3em]">Your Items</span>', '<h2 class="text-sm font-bold text-white uppercase tracking-widest">Twój Koszyk</h2>')

# Fix progress bar JS class injection
js_progress = """
        document.querySelectorAll('.step-indicator').forEach(ind => {
            const step = parseInt(ind.getAttribute('data-step'));
            const circle = ind.querySelector('.step-circle');
            const text = ind.querySelector('span');
            
            if (step < currentStage) {
                // completed
                circle.className = 'step-circle w-6 h-6 rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black transition-all shadow-[0_0_15px_rgba(217,70,239,0.5)] scale-110';
                circle.innerHTML = '<svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>';
                text.className = 'text-[9px] uppercase font-bold tracking-[0.2em] text-white';
            } else if (step === currentStage) {
                // current
                circle.className = 'step-circle w-6 h-6 rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black font-black text-[10px] transition-all shadow-[0_0_15px_rgba(217,70,239,0.5)] scale-110';
                circle.innerHTML = (step + 1);
                text.className = 'text-[9px] uppercase font-bold tracking-[0.2em] text-white';
            } else {
                // future
                circle.className = 'step-circle w-6 h-6 rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all';
                circle.innerHTML = (step + 1);
                text.className = 'text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center';
            }
        });
"""
content = re.sub(r'document\.querySelectorAll\(\'\.step-indicator\'\)\.forEach\(ind => \{.*?\}\);', js_progress, content, flags=re.DOTALL)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Checkout redesigned.")
