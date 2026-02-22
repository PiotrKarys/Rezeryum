const fs = require('fs');
const path = require('path');

const directoryPath = 'a:\\Coding\\game\\Rezeryum\\Rasy';

const patterns = [
    /\(Rozwiązanie z \*Do Doprecyzowania\*\)\s*/g,
    /\(rozwiązanie \*Do Doprecyzowania\*:.*?\)\s*/g,
    /\(AI Prompt Guide\)\s*/g,
    /\(AI Prompt\)\s*/g,
    /\(AI Prompt.*?\)\s*/g,
    /\(Dodano nową cechę\)\s*/g,
    /\(RozwiÄ…zanie z \*Do Doprecyzowania\*\)\s*/g,
    /\(rozwiÄ…zanie \*Do Doprecyzowania\*:.*?\)\s*/g
];

const fixes = {
    "Ĺş": "ź", "Ĺ‚": "ł", "Ä…": "ą", "Ä™": "ę", "Ĺ›": "ś", "Ăł": "ó", "ĹĽ": "ż", "Ä‡": "ć", "Ĺ„": "ń",
    "Ĺą": "Ź", "Ĺ ": "Ł", "Ä„": "Ą", "Ä˜": "Ę", "Ĺš": "Ś", "Ă“": "Ó", "Ĺť": "Ż", "Ä†": "Ć", "Ĺƒ": "Ń",
    "â€“": "–", "â€ž": "„", "â€ ": "”"
};

const processed = [];

fs.readdir(directoryPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    }

    files.forEach(function (file) {
        if (path.extname(file) === '.md') {
            const filePath = path.join(directoryPath, file);
            let content = fs.readFileSync(filePath, 'utf8');
            let original = content;

            // Fix encoding errors from powershell string interpolation
            for (let bad in fixes) {
                content = content.replace(new RegExp(bad, 'g'), fixes[bad]);
            }

            // Remove tags
            patterns.forEach(regex => {
                content = content.replace(regex, '');
            });

            if (content !== original) {
                fs.writeFileSync(filePath, content, 'utf8');
                processed.push(file);
                console.log(`[${file}] - Usunięto meta-tagi.`);
            }
        }
    });

    console.log("Operacja Czyste Cięcie zakończona. Cała baza Rezeryum 3.0 jest gotowa, spójna i wolna od artefaktów AI.");
});
