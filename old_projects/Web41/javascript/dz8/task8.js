const prompt = require('prompt-sync')();

function parseUrl() {
  
    const url = prompt("Введите URL:");

    try {
    
        const parsedUrl = new URL(url);

     
        const urlInfo = {
            protocol: parsedUrl.protocol,
            host: parsedUrl.host,
            hostname: parsedUrl.hostname,
            port: parsedUrl.port,
            pathname: parsedUrl.pathname,
            search: parsedUrl.search,
            searchParams: Array.from(parsedUrl.searchParams.entries()).reduce((acc, [key, value]) => {
                acc[key] = value;
                return acc;
            }, {}),
            hash: parsedUrl.hash
        };

      
        console.log('Информация о URL:', urlInfo);
    } catch (error) {
        console.error('Ошибка при разборе URL:', error.message);
    }
}

parseUrl();
