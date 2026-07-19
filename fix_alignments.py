import os
import re

FILE_PATH = r"s:\turboblocks-web\src\pages\checkout.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Progress Bar Fix
old_progress_bar = r'<div class="flex items-center justify-between relative px-4">.*?</div>\s*</div>\s*</div>'
new_progress_bar = """<div class="relative grid grid-cols-4 px-0 sm:px-4">
                <!-- Line background -->
                <div class="absolute left-[12.5%] right-[12.5%] top-[11px] h-[2px] bg-white/5 -z-10 rounded-full"></div>
                <!-- Line progress -->
                <div id="progress-line" class="absolute left-[12.5%] top-[11px] h-[2px] bg-gradient-to-r from-fuchsia-500 to-cyan-500 -z-10 transition-all duration-700 w-0 rounded-full shadow-[0_0_10px_rgba(217,70,239,0.5)]"></div>
                
                <!-- Steps -->
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="0">
                    <div class="step-circle w-[24px] h-[24px] rounded-full bg-fuchsia-500 border-2 border-black flex items-center justify-center text-black transition-all shadow-[0_0_15px_rgba(217,70,239,0.5)] scale-110">
                        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                    </div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white">Koszyk</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="1">
                    <div class="step-circle w-[24px] h-[24px] rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all">2</div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center">Dane</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="2">
                    <div class="step-circle w-[24px] h-[24px] rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all">3</div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center">Płatność</span>
                </div>
                
                <div class="step-indicator flex flex-col items-center gap-3 relative z-10" data-step="3">
                    <div class="step-circle w-[24px] h-[24px] rounded-full bg-black border-2 border-white/20 flex items-center justify-center text-white/30 text-[10px] font-black transition-all">4</div>
                    <span class="text-[9px] uppercase font-bold tracking-[0.2em] text-white/30 text-center">Gotowe</span>
                </div>
            </div>
        </div>"""
content = re.sub(old_progress_bar, new_progress_bar, content, flags=re.DOTALL)

# Update JS for progress line
# old: if(currentStage === 0) line.style.width = '0%'; else if(currentStage === 1) line.style.width = '33%';
old_js_progress = r"if\(currentStage === 0\) line\.style\.width = '0%';\s*else if\(currentStage === 1\) line\.style\.width = '33%';\s*else if\(currentStage === 2\) line\.style\.width = '66%';\s*else if\(currentStage === 3\) line\.style\.width = '100%';"
new_js_progress = "line.style.width = (currentStage * 33.333) + '%';"
content = re.sub(old_js_progress, new_js_progress, content)


# 2. Fix the styling of sections to match "Podsumowanie"
# Cart section
content = content.replace('class="group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-3xl rounded-[2.5rem] overflow-hidden border-[rgba(var(--theme-rgb),0.3)] shadow-[0_0_50px_rgba(var(--theme-rgb),0.2)] hover:shadow-[0_0_80px_rgba(var(--theme-rgb),0.3)] transition-all duration-700"', 'class="group relative bg-gradient-to-b from-white/[0.05] to-transparent backdrop-blur-2xl rounded-3xl overflow-hidden border border-white/[0.05] shadow-2xl transition-all duration-700"')

# Login section
content = content.replace('class="hidden group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-3xl rounded-[2.5rem] p-6 md:p-8 border-[rgba(var(--theme-rgb),0.3)] shadow-[0_0_50px_rgba(var(--theme-rgb),0.2)] hover:shadow-[0_0_80px_rgba(var(--theme-rgb),0.3)] transition-all duration-700"', 'class="hidden group relative bg-gradient-to-b from-white/[0.05] to-transparent backdrop-blur-2xl rounded-3xl p-6 md:p-8 border border-white/[0.05] shadow-2xl transition-all duration-700"')

# Payment method section
content = content.replace('class="hidden group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-3xl rounded-[2.5rem] p-6 md:p-8 border-[rgba(var(--theme-rgb),0.3)] shadow-[0_0_50px_rgba(var(--theme-rgb),0.2)] hover:shadow-[0_0_80px_rgba(var(--theme-rgb),0.3)] transition-all duration-700"', 'class="hidden group relative bg-gradient-to-b from-white/[0.05] to-transparent backdrop-blur-2xl rounded-3xl p-6 md:p-8 border border-white/[0.05] shadow-2xl transition-all duration-700"')

# Success section
content = content.replace('class="hidden group relative bg-gradient-to-br from-white/5 to-white/[0.02] backdrop-blur-3xl rounded-[2.5rem] p-10 border-[rgba(var(--theme-rgb),0.3)] shadow-[0_0_50px_rgba(var(--theme-rgb),0.2)] text-center transition-all duration-700"', 'class="hidden group relative bg-gradient-to-b from-white/[0.05] to-transparent backdrop-blur-2xl rounded-3xl p-10 border border-white/[0.05] shadow-2xl text-center transition-all duration-700"')


# 3. Clean up inner titles of the old sections to match Podsumowanie's clean title
# Login:
# <h2 class="text-xl font-black text-white uppercase italic tracking-tighter mb-2">Twoje Dane</h2>
content = content.replace('<h2 class="text-xl font-black text-white uppercase italic tracking-tighter mb-2">Twoje Dane</h2>', '<h3 class="text-sm font-bold text-white uppercase tracking-widest mb-2 flex items-center gap-3"><span class="w-2 h-2 rounded-full bg-purple-400 shadow-[0_0_10px_rgba(168,85,247,0.8)]"></span> Twoje Dane</h3>')
# <p class="text-xs text-white/50 font-bold mb-6">
content = content.replace('<p class="text-xs text-white/50 font-bold mb-6">', '<p class="text-xs text-white/40 font-medium mb-8">')

# Payment:
# <span class="inline-block text-[9px] font-black uppercase tracking-[0.3em] py-1.5 px-3 rounded-lg border border-white/10 shadow-2xl mb-6" style="...">METODA PŁATNOŚCI</span>
old_pay_title = r'<span class="inline-block text-\[9px\] font-black uppercase tracking-\[0\.3em\].*?METODA PŁATNOŚCI\s*</span>'
new_pay_title = '<h3 class="text-sm font-bold text-white uppercase tracking-widest mb-6 flex items-center gap-3"><span class="w-2 h-2 rounded-full bg-purple-400 shadow-[0_0_10px_rgba(168,85,247,0.8)]"></span> Metoda Płatności</h3>'
content = re.sub(old_pay_title, new_pay_title, content, flags=re.DOTALL)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Alignment fixed")
