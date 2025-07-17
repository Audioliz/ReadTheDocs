// Sélecteur de langue personnalisé pour Read the Docs
(function() {
    'use strict';
    
    // Configuration des langues
    const languages = {
        'en': {
            name: 'English',
            flag: 'EN',
            url: '/en/latest/'
        },
        'fr': {
            name: 'Français',
            flag: 'FR',
            url: '/fr/latest/'
        }
    };
    
    // Fonction pour créer le sélecteur
    function createLanguageSelector() {
        // Créer le conteneur
        const container = document.createElement('div');
        container.className = 'language-selector';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        `;
        
        // Créer le sélecteur
        const select = document.createElement('select');
        select.style.cssText = `
            border: none;
            background: transparent;
            font-size: 14px;
            padding: 4px 8px;
            cursor: pointer;
            outline: none;
        `;
        
        // Ajouter les options
        Object.keys(languages).forEach(langCode => {
            const lang = languages[langCode];
            const option = document.createElement('option');
            option.value = langCode;
            option.textContent = `${lang.flag} ${lang.name}`;
            
            // Marquer la langue actuelle
            if (window.location.pathname.includes(`/${langCode}/`)) {
                option.selected = true;
            }
            
            select.appendChild(option);
        });
        
        // Gérer le changement de langue
        select.addEventListener('change', function() {
            const selectedLang = this.value;
            const lang = languages[selectedLang];
            
            // Construire la nouvelle URL
            const currentPath = window.location.pathname;
            const newPath = currentPath.replace(/^\/(en|fr)\//, lang.url);
            
            // Rediriger vers la nouvelle langue
            window.location.href = newPath;
        });
        
        container.appendChild(select);
        return container;
    }
    
    // Fonction pour créer un sélecteur alternatif (boutons)
    function createLanguageButtons() {
        const container = document.createElement('div');
        container.className = 'language-buttons';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            display: flex;
            gap: 8px;
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        `;
        
        Object.keys(languages).forEach(langCode => {
            const lang = languages[langCode];
            const button = document.createElement('button');
            button.textContent = `${lang.flag} ${lang.name}`;
            button.style.cssText = `
                border: none;
                background: transparent;
                padding: 6px 12px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
                transition: background-color 0.2s;
            `;
            
            // Style pour la langue active
            if (window.location.pathname.includes(`/${langCode}/`)) {
                button.style.backgroundColor = '#007bff';
                button.style.color = 'white';
            } else {
                button.addEventListener('mouseenter', function() {
                    this.style.backgroundColor = '#f8f9fa';
                });
                button.addEventListener('mouseleave', function() {
                    this.style.backgroundColor = 'transparent';
                });
            }
            
            // Gérer le clic
            button.addEventListener('click', function() {
                const currentPath = window.location.pathname;
                const newPath = currentPath.replace(/^\/(en|fr)\//, lang.url);
                window.location.href = newPath;
            });
            
            container.appendChild(button);
        });
        
        return container;
    }
    
    // Attendre que le DOM soit chargé
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            // Choisir le type de sélecteur (select ou boutons)
            const selector = createLanguageButtons(); // ou createLanguageSelector()
            document.body.appendChild(selector);
        });
    } else {
        const selector = createLanguageButtons(); // ou createLanguageSelector()
        document.body.appendChild(selector);
    }
})(); 