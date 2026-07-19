import os
import re

# 1. Update CartTrigger.astro
cart_trigger_path = r"s:\turboblocks-web\src\components\navbar\shared\CartTrigger.astro"
with open(cart_trigger_path, "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace(
    'shadow-[0_0_20px_rgba(236,72,153,0.3)] hover:shadow-[0_0_30px_rgba(236,72,153,0.6)]',
    'hover:shadow-[0_0_15px_rgba(236,72,153,0.4)]'
)
with open(cart_trigger_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Update DesktopNavbar.astro
desktop_navbar_path = r"s:\turboblocks-web\src\components\navbar\desktop\DesktopNavbar.astro"
with open(desktop_navbar_path, "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace(
    'shadow-[0_0_20px_rgba(236,72,153,0.3)] hover:shadow-[0_0_30px_rgba(236,72,153,0.6)]',
    'hover:shadow-[0_0_15px_rgba(236,72,153,0.4)]'
)
with open(desktop_navbar_path, "w", encoding="utf-8") as f:
    f.write(content)

# 3. Update CartOverlay.astro
cart_overlay_path = r"s:\turboblocks-web\src\components\shop\CartOverlay.astro"
with open(cart_overlay_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace wrapper class and style
old_wrapper = r'<div style="--cart-hex: #FF00CC; --cart-rgb: 255,0,204;" class="w-full bg-\[#0a0514\]/70 backdrop-blur-\[40px\] border-\[rgba\(var\(--cart-rgb\),0\.25\)\] border rounded-\[2\.5rem\] shadow-\[0_0_60px_rgba\(var\(--cart-rgb\),0\.15\)\] overflow-hidden flex flex-col relative group">'
new_wrapper = r'<div style="--cart-hex: #FF00CC; --cart-rgb: 255,0,204;" class="w-full bg-gradient-to-b from-white/[0.05] to-transparent backdrop-blur-[40px] border border-white/5 rounded-[2.5rem] shadow-2xl overflow-hidden flex flex-col relative group">'
content = re.sub(old_wrapper, new_wrapper, content)

# Remove shadow from YOUR CART text
old_cart_text = r'<span class="neon-text-animated pr-2" style={`background-image: \$\{cartGradient\}; filter: drop-shadow\(0 0 15px rgba\(var\(--cart-rgb\),0\.4\)\);`}>CART</span>'
new_cart_text = r'<span class="neon-text-animated pr-2" style={`background-image: ${cartGradient};`}>CART</span>'
content = re.sub(old_cart_text, new_cart_text, content)

# Remove box-shadow from PROCEED TO CHECKOUT button
old_btn = r'style={`background: \$\{btnGradient\}; box-shadow: 0 0 20px rgba\(var\(--cart-rgb\),0\.4\), inset 0 0 10px rgba\(255,255,255,0\.2\);`}'
new_btn = r'style={`background: ${btnGradient}; box-shadow: inset 0 0 10px rgba(255,255,255,0.2);`}'
content = re.sub(old_btn, new_btn, content)

# Hide 0.00 zł dynamically in JS
old_js_update = r"document\.getElementById\('cart-total-pln'\)\.innerText = totalPln\.toFixed\(2\) \+ ' zł';"
new_js_update = """const plnEl = document.getElementById('cart-total-pln');
        plnEl.innerText = totalPln.toFixed(2) + ' zł';
        plnEl.style.display = totalPln > 0 ? '' : 'none';"""
content = re.sub(old_js_update, new_js_update, content)

with open(cart_overlay_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Neon effects toned down successfully!")
