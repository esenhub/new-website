
(function() {
    const trackingKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'name', 'email', 'phone'];

    function captureData() {
        const urlParams = new URLSearchParams(window.location.search);
        let storedData = JSON.parse(localStorage.getItem('monetise_marketing_data')) || {};
        let updated = false;

        trackingKeys.forEach(key => {
            if (urlParams.has(key)) {
                storedData[key] = urlParams.get(key);
                updated = true;
            }
        });

        if (updated) {
            localStorage.setItem('monetise_marketing_data', JSON.stringify(storedData));
        }
    }

    function applyDataToLinks() {
        const storedValue = localStorage.getItem('monetise_marketing_data');
        if (!storedValue) return;
        const marketingData = JSON.parse(storedValue);

        document.querySelectorAll('a, iframe').forEach(el => {
            try {
                let attr = el.tagName === 'A' ? 'href' : 'src';
                if (!el[attr] || el[attr].startsWith('#') || el[attr].startsWith('mailto:')) return;

                const url = new URL(el[attr]);
                if (url.hostname.includes('whop.com') || url.hostname.includes('monetise.com') || url.hostname.includes('tally.so')) {
                    Object.keys(marketingData).forEach(key => {
                        url.searchParams.set(key, marketingData[key]);
                    });
                    el[attr] = url.toString();
                }
            } catch (e) {}
        });
    }

    window.addEventListener('load', () => {
        captureData();
        applyDataToLinks();
        const observer = new MutationObserver(() => applyDataToLinks());
        observer.observe(document.body, { childList: true, subtree: true });
    });
})();
