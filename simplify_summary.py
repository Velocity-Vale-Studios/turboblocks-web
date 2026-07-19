import os
import re

FILE_PATH = r"s:\turboblocks-web\src\pages\checkout.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the Summary HTML structure
old_summary_html = r'<h3 class="text-sm font-bold text-white uppercase tracking-widest mb-6 flex items-center gap-3">\s*<span class="w-2 h-2 rounded-full bg-cyan-400 shadow-\[0_0_10px_rgba\(34,211,238,0\.8\)\]"></span> Podsumowanie\s*</h3>\s*<div class="space-y-4 mb-6">\s*<div class="flex justify-between items-center">\s*<span class="text-xs text-white/50 font-medium">Przedmioty</span>\s*<span id="ck-subtotal" class="text-sm font-bold text-white">0 TC</span>\s*</div>.*?<div class="flex justify-between items-center">\s*<span class="text-base font-black text-white uppercase">Suma \(<span class="fiat-label">PLN</span>\)</span>\s*<span id="ck-total-fiat" class="text-base font-black text-amber-200 tracking-tight">0\.00 zł</span>\s*</div>\s*</div>'

new_summary_html = """<div class="flex justify-between items-center mb-6">
                        <h3 class="text-sm font-bold text-white uppercase tracking-widest flex items-center gap-3">
                            <span class="w-2 h-2 rounded-full bg-cyan-400 shadow-[0_0_10px_rgba(34,211,238,0.8)]"></span> Podsumowanie
                        </h3>
                        <select id="checkout-currency" class="bg-white/5 border border-white/10 rounded-lg text-xs font-bold px-3 py-1.5 focus:outline-none focus:border-cyan-500/50 text-white cursor-pointer hover:bg-white/10 transition-colors">
                            <option value="PLN">PLN (zł)</option>
                            <option value="EUR">EUR (€)</option>
                            <option value="USD">USD ($)</option>
                        </select>
                    </div>

                    <div class="space-y-4 mb-6">
                        <div class="flex justify-between items-center">
                            <span class="text-xs text-white/50 font-medium">Wartość</span>
                            <div class="flex flex-col items-end gap-1">
                                <span id="ck-subtotal-tc" class="text-sm font-bold text-pink-400">0 TC</span>
                                <span id="ck-subtotal-fiat" class="text-sm font-bold text-amber-300">0.00 zł</span>
                            </div>
                        </div>
                        <div id="discount-row" class="hidden flex justify-between items-center">
                            <span class="text-xs text-white/50 font-medium">Zniżka</span>
                            <div class="flex flex-col items-end gap-1">
                                <span id="ck-discount-tc" class="text-sm font-bold text-green-400">-0 TC</span>
                                <span id="ck-discount-fiat" class="text-sm font-bold text-green-400">-0.00 zł</span>
                            </div>
                        </div>
                        <div class="h-[1px] bg-white/10"></div>
                        <div class="flex justify-between items-end pt-2">
                            <span class="text-base font-black text-white uppercase pb-1">Suma</span>
                            <div class="flex flex-col items-end gap-1">
                                <span id="ck-total-tc" class="text-2xl font-black italic text-transparent bg-clip-text bg-gradient-to-r from-pink-400 to-purple-400 tracking-tighter">0 TC</span>
                                <span id="ck-total-fiat" class="text-2xl font-black italic text-transparent bg-clip-text bg-gradient-to-r from-amber-200 to-yellow-400 tracking-tighter">0.00 zł</span>
                            </div>
                        </div>
                    </div>"""

content = re.sub(old_summary_html, new_summary_html, content, flags=re.DOTALL)


# 2. Update JS logic in renderCheckout
old_js_vars = r"const subtotalEl = document\.getElementById\('ck-subtotal'\);\s*const subtotalPlnEl = document\.getElementById\('ck-subtotal-fiat'\);\s*const totalEl = document\.getElementById\('ck-total'\);\s*const totalPlnEl = document\.getElementById\('ck-total-fiat'\);\s*const discountAmountEl = document\.getElementById\('ck-discount-amount'\);"

new_js_vars = """const subtotalTcEl = document.getElementById('ck-subtotal-tc');
        const subtotalFiatEl = document.getElementById('ck-subtotal-fiat');
        const totalTcEl = document.getElementById('ck-total-tc');
        const totalFiatEl = document.getElementById('ck-total-fiat');
        const discountTcEl = document.getElementById('ck-discount-tc');
        const discountFiatEl = document.getElementById('ck-discount-fiat');"""

content = re.sub(old_js_vars, new_js_vars, content)


old_js_empty = r"if \(subtotalEl\) subtotalEl\.innerText = '0 TC';\s*if \(totalEl\) totalEl\.innerText = '0 TC';\s*if \(subtotalPlnEl\) subtotalPlnEl\.innerText = '0\.00 ' \+ sym;\s*if \(totalPlnEl\) totalPlnEl\.innerText = '0\.00 ' \+ sym;"

new_js_empty = """if (subtotalTcEl) subtotalTcEl.innerText = '0 TC';
            if (totalTcEl) totalTcEl.innerText = '0 TC';
            if (subtotalFiatEl) subtotalFiatEl.innerText = '0.00 ' + sym;
            if (totalFiatEl) totalFiatEl.innerText = '0.00 ' + sym;
            if (subtotalTcEl) subtotalTcEl.style.display = '';
            if (subtotalFiatEl) subtotalFiatEl.style.display = 'none';
            if (totalTcEl) totalTcEl.style.display = '';
            if (totalFiatEl) totalFiatEl.style.display = 'none';"""

content = re.sub(old_js_empty, new_js_empty, content)


old_js_discount = r"if \(discountAmountEl\) \{\s*discountAmountEl\.innerText = `-\$\{activeDiscountPercent\}% \(-\$\{tcDiscount\} TC / -\$\{fiatDiscount\.toFixed\(2\)\} \$\{sym\}\)`;\s*\}.*?if \(discountAmountEl\) \{\s*discountAmountEl\.innerText = '-0 TC';\s*\}"

new_js_discount = """if (discountTcEl) discountTcEl.innerText = `-${tcDiscount} TC`;
                if (discountFiatEl) discountFiatEl.innerText = `-${fiatDiscount.toFixed(2)} ${sym}`;
                if (discountTcEl) discountTcEl.style.display = tcDiscount > 0 ? '' : 'none';
                if (discountFiatEl) discountFiatEl.style.display = fiatDiscount > 0 ? '' : 'none';
            } else {
                if (discountRow) discountRow.classList.add('hidden');
            }"""

content = re.sub(old_js_discount, new_js_discount, content, flags=re.DOTALL)


old_js_total = r"if \(subtotalEl\) subtotalEl\.innerText = totalTc \+ ' TC';\s*if \(totalEl\) totalEl\.innerText = totalTc \+ ' TC';\s*if \(subtotalPlnEl\) subtotalPlnEl\.innerText = totalFiat\.toFixed\(2\) \+ ' ' \+ sym;\s*if \(totalPlnEl\) totalPlnEl\.innerText = totalFiat\.toFixed\(2\) \+ ' ' \+ sym;"

new_js_total = """if (subtotalTcEl) {
            subtotalTcEl.innerText = totalTc + ' TC';
            subtotalTcEl.style.display = totalTc > 0 ? '' : 'none';
        }
        if (totalTcEl) {
            totalTcEl.innerText = totalTc + ' TC';
            totalTcEl.style.display = totalTc > 0 ? '' : 'none';
        }
        if (subtotalFiatEl) {
            subtotalFiatEl.innerText = totalFiat.toFixed(2) + ' ' + sym;
            subtotalFiatEl.style.display = totalFiat > 0 ? '' : 'none';
        }
        if (totalFiatEl) {
            totalFiatEl.innerText = totalFiat.toFixed(2) + ' ' + sym;
            totalFiatEl.style.display = totalFiat > 0 ? '' : 'none';
        }"""

content = re.sub(old_js_total, new_js_total, content)


with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Simplified summary card!")
