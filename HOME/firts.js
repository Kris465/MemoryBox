document.addEventListener('DOMContentLoaded', function() {
    const siteABtn = document.getElementById('siteA');
    const siteBBtn = document.getElementById('siteB');
    const overlay = document.getElementById('transitionOverlay');
    const loadingText = document.getElementById('loadingText');
    const visitCountEl = document.getElementById('visitCount');
    const lastVisitTimeEl = document.getElementById('lastVisitTime');
    const timeBar = document.querySelector('.time-bar');
    const timeMarker = document.getElementById('timeMarker');
    
    let visits = localStorage.getItem('transitionVisits') || 0;
    let lastVisitTime = localStorage.getItem('lastTransitionTime');
    let visitHistory = JSON.parse(localStorage.getItem('visitHistory') || '[]');
    
    function initStats() {
        visitCountEl.textContent = visits;
        
        if (lastVisitTime) {
            const lastVisitDate = new Date(parseInt(lastVisitTime));
            lastVisitTimeEl.textContent = lastVisitDate.toLocaleTimeString() + ' ' + 
                                      lastVisitDate.toLocaleDateString();
        }
        
        updateTimeScale();
    }
    
    function updateTimeScale() {
        if (visitHistory.length === 0) return;
        
        const now = new Date();
        const oneDay = 24 * 60 * 60 * 1000;
        const timePoints = [];

        for (let i = 0; i < 24; i++) {
            timePoints.push({hour: i, count: 0});
        }
        
        visitHistory.forEach(visit => {
            const visitDate = new Date(visit.time);
            const hour = visitDate.getHours();
            timePoints[hour].count++;
        });
        
        const maxCount = Math.max(...timePoints.map(p => p.count), 1);
        
        const currentHour = now.getHours();
        timeMarker.style.left = `${(currentHour / 24) * 100}%`;
        
        let gradientParts = [];
        timePoints.forEach((point, i) => {
            const intensity = point.count / maxCount;
            const color = `rgba(66, 133, 244, ${intensity})`;
            const pos1 = (i / 24) * 100;
            const pos2 = ((i + 1) / 24) * 100;
            gradientParts.push(`${color} ${pos1}%`);
            gradientParts.push(`${color} ${pos2}%`);
        });
        
        timeBar.style.background = `linear-gradient(90deg, ${gradientParts.join(', ')})`;
        timeBar.style.width = '100%';
    }
    
    function handleTransition(btn, url) {

        const btnColor = window.getComputedStyle(btn).backgroundColor;

        overlay.style.backgroundColor = btnColor;
        overlay.style.width = '0';
        
        overlay.style.display = 'block';
        loadingText.style.opacity = '1';
        
        setTimeout(() => {
            overlay.style.width = '100%';
        }, 10);
        
        visits++;
        const now = new Date();
        const timestamp = now.getTime();
        
        visitHistory.push({
            time: timestamp,
            site: url.includes('site-a') ? 'A' : 'B'
        });
        
        localStorage.setItem('transitionVisits', visits);
        localStorage.setItem('lastTransitionTime', timestamp);
        localStorage.setItem('visitHistory', JSON.stringify(visitHistory));
        
        setTimeout(() => {
            loadingText.textContent = 'Открываем сайт...';
            
            const finalUrl = new URL(url);
            finalUrl.searchParams.set('from', 'transition_page');
            finalUrl.searchParams.set('t', timestamp);
            
            setTimeout(() => {
                window.location.href = finalUrl.toString();
            }, 300);
        }, 800);
    }
    
    initStats();
    
    siteABtn.addEventListener('click', function() {
        handleTransition(this, 'https://site-a.com');
    });
    
    siteBBtn.addEventListener('click', function() {
        handleTransition(this, 'https://site-b.com');
    });
});