import os
import re

FILE_PATH = r"s:\turboblocks-web\src\components\shop\CartOverlay.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Restore CART PREVIEW
old_cart_preview = r'<span class="text-\[9px\] font-black uppercase tracking-\[0\.3em\] py-1\.5 px-3 rounded-xl border border-white/10 shadow-2xl"\s*class="text-\[9px\] font-black uppercase tracking-\[0\.3em\] py-1\.5 px-3 rounded-xl border border-white/10 text-white/50 bg-white/5">\s*CART PREVIEW\s*</span>'
new_cart_preview = r"""<span class="text-[9px] font-black uppercase tracking-[0.3em] py-1.5 px-3 rounded-xl border border-transparent shadow-2xl"
                          style={`color: var(--cart-hex); background: rgba(var(--cart-rgb), 0.08); box-shadow: inset 0 0 0 1px rgba(var(--cart-rgb),0.25);`}>
                        CART PREVIEW
                    </span>"""

content = re.sub(old_cart_preview, new_cart_preview, content)

# Remove gradient from TC total
old_tc_total = r'<span id="cart-total" class="text-2xl font-black italic text-transparent bg-clip-text tracking-tighter" style={`background-image: \$\{cartGradient\};`}>0 TC</span>'
new_tc_total = r'<span id="cart-total" class="text-2xl font-black italic text-cyan-400 tracking-tighter">0 TC</span>'

content = re.sub(old_tc_total, new_tc_total, content)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored CART PREVIEW and removed gradient from TC total.")
