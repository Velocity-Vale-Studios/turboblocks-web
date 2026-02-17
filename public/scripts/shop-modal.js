(() => {
    // Helper for rarity styles
    const getRarityStyles = (rarity) => {
        switch(rarity) {
            case 'Legendary': return 'border-yellow-500/50 shadow-[0_0_30px_rgba(234,179,8,0.2)] text-yellow-400';
            case 'Epic': return 'border-purple-500/40 shadow-[0_0_20px_rgba(168,85,247,0.15)] text-purple-400';
            case 'Rare': return 'border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.1)] text-blue-400';
            default: return 'border-white/10 text-white/60';
        }
    };

    // Cart Logic Helper
    const addToCart = (item) => {
        const event = new CustomEvent('shop:add', { detail: item });
        window.dispatchEvent(event);
    };

    // Modal Opening Logic
    const openItemDetails = (itemData) => {
        let item = itemData;

        // Ensure item is an object
        if (typeof itemData === 'string') {
            try {
                item = JSON.parse(itemData);
            } catch (e) {
                console.error("Failed to parse item data", e);
                return;
            }
        }

        const modal = document.getElementById('item-modal');
        const content = document.getElementById('modal-content');

        if(!modal || !content) {
            console.error("Modal elements not found!");
            return;
        }

        // Populate Content
        const iconEl = document.getElementById('modal-icon');
        const titleEl = document.getElementById('modal-title');
        const typeEl = document.getElementById('modal-type');
        const descEl = document.getElementById('modal-desc');
        const priceEl = document.getElementById('modal-price');
        const rarityBadge = document.getElementById('modal-rarity');

        if(iconEl) iconEl.innerHTML = item.icon || '';
        if(titleEl) titleEl.innerText = item.name || '';
        if(typeEl) typeEl.innerText = item.type || '';
        if(descEl) descEl.innerText = item.desc || '';
        if(priceEl) priceEl.innerText = item.price || '';

        // Rarity Styles
        if(rarityBadge) {
            rarityBadge.className = `px-4 py-1.5 rounded-xl border bg-black/50 text-xs font-black uppercase tracking-[0.2em] backdrop-blur-md ${getRarityStyles(item.rarity)}`;
            rarityBadge.innerText = item.rarity || '';
        }

        // Updated Add to Cart Button in Modal
        const modalBtn = document.getElementById('modal-btn');
        if(modalBtn) {
            // Remove old listeners by cloning
            const newBtn = modalBtn.cloneNode(true);
            modalBtn.parentNode.replaceChild(newBtn, modalBtn);

            newBtn.onclick = () => {
                addToCart(item);
                closeModal();
            };
        }

        // Show Modal
        modal.style.display = 'flex';
        modal.classList.remove('opacity-0', 'pointer-events-none');

        // Animation
        setTimeout(() => {
             content.classList.remove('opacity-0', 'scale-95');
             content.classList.add('opacity-100', 'scale-100');
        }, 10);
    };

    // Modal Closing Logic
    const closeModal = () => {
         const modal = document.getElementById('item-modal');
        const content = document.getElementById('modal-content');

        if(!modal || !content) return;

        content.classList.remove('opacity-100', 'scale-100');
        content.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
            modal.classList.add('opacity-0', 'pointer-events-none');
            // Allow pointer events to pass through again
        }, 300);
    };

    // Expose close to window for backdrop click
    window.closeModal = closeModal;

    // Delegate Click Event Listener on Document Body
    document.body.addEventListener('click', (e) => {
        // Handle "Add to Cart" button click
        const btn = e.target.closest('.add-to-cart-btn');
        if (btn) {
            e.stopPropagation(); // prevent triggering the card click
            console.log("Button clicked");
            const itemData = btn.dataset.item;
            if (itemData) {
                try {
                    const item = JSON.parse(itemData);
                    addToCart(item);
                } catch (err) {
                    console.error("Error parsing cart item", err);
                }
            }
            return; // stop further processing
        }

        // Handle "Item Card" click
        const card = e.target.closest('.item-card');
        if (card) {
            const itemData = card.dataset.item;
            console.log("Card clicked:", itemData);
            if (itemData) openItemDetails(itemData);
        }
    });

})();
