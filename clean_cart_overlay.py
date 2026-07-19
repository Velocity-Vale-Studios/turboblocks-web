import os
import re

FILE_PATH = r"s:\turboblocks-web\src\components\shop\CartOverlay.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Wrapper (remove shadow-2xl, background-glow, top-glowing line)
old_wrapper = r'<div style="--cart-hex: #FF00CC; --cart-rgb: 255,0,204;" class="w-full bg-gradient-to-b from-white/\[0\.05\] to-transparent backdrop-blur-\[40px\] border border-white/5 rounded-\[2\.5rem\] shadow-2xl overflow-hidden flex flex-col relative group">\s*\{/\* Soft background glow \*/\}\s*<div class="absolute top-0 left-0 w-full h-\[200px\] bg-gradient-to-b from-\[rgba\(var\(--cart-rgb\),0\.1\)\] to-transparent pointer-events-none"></div>\s*\{/\* Top glowing line \*/\}\s*<div class="absolute top-0 left-0 w-full h-\[2px\] transition-all duration-700" style={`background: linear-gradient\(90deg, transparent, var\(--cart-hex\), transparent\);`}></div>'

new_wrapper = r"""<div style="--cart-hex: #FF00CC; --cart-rgb: 255,0,204;" class="w-full bg-[#0a0514]/90 backdrop-blur-3xl border border-white/10 rounded-[2rem] overflow-hidden flex flex-col relative group">"""

content = re.sub(old_wrapper, new_wrapper, content)

# 2. Update Checkout Button
old_btn = r'<a id="checkout-btn" href="/checkout" class="relative overflow-hidden w-full py-4 rounded-2xl text-white font-black uppercase tracking-\[0\.2em\] text-\[11px\] transition-all duration-300 hover:scale-\[1\.02\] active:scale-\[0\.98\] flex items-center justify-center gap-3 border border-transparent group/btn no-underline"\s*style={`background: \$\{btnGradient\}; box-shadow: inset 0 0 10px rgba\(255,255,255,0\.2\);`}>'

new_btn = r'<a id="checkout-btn" href="/checkout" class="relative overflow-hidden w-full py-4 rounded-2xl text-white font-black uppercase tracking-[0.2em] text-[11px] transition-all duration-300 hover:bg-white/10 flex items-center justify-center gap-3 border border-white/10 group/btn no-underline bg-gradient-to-r from-fuchsia-600 to-purple-600">'

content = re.sub(old_btn, new_btn, content)

# 3. Fix 0.00 zł
old_pln_update = r"if \(totalPlnDisplay\) totalPlnDisplay\.innerText = totalPln\.toFixed\(2\) \+ ' zł';"
new_pln_update = r"if (totalPlnDisplay) { totalPlnDisplay.innerText = totalPln.toFixed(2) + ' zł'; totalPlnDisplay.style.display = totalPln > 0 ? '' : 'none'; }"
content = re.sub(old_pln_update, new_pln_update, content)

# 4. Remove CART PREVIEW pink background
old_cart_preview = r'style={`color: var\(--cart-hex\); background: rgba\(var\(--cart-rgb\), 0\.08\); box-shadow: inset 0 0 0 1px rgba\(var\(--cart-rgb\),0\.25\);`}'
new_cart_preview = r'class="text-[9px] font-black uppercase tracking-[0.3em] py-1.5 px-3 rounded-xl border border-white/10 text-white/50 bg-white/5"'
content = re.sub(old_cart_preview, new_cart_preview, content)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("CartOverlay fully decluttered!")
