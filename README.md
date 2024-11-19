Instrukcja uruchomienia:
1.Zainstaluj wymagane biblioteki(OpenAI)
2. Wstaw klucz API do "openai.api_key"
3. Przygotuj plik "artykulTekst.txt" wraz z treścią artykułu
4. Uruchom program.
5. Sprawdź wynik, który został zapisany w pliku "artykul.html".

Opis działania aplikacji:
Aplikacja opiera się na integracji z modelem językowym OpenAI (GPT-4o) w celu automatycznego generowania kodu HTML na podstawie dostarczonego tekstu artykułu.

Wejście danych:
Aplikacja wczytuje plik tekstowy o nazwie artykulTekst.txt, który zawiera treść artykułu.

Przetwarzanie:
Wygenerowany prompt (polecenie) prosi model OpenAI o utworzenie kodu HTML na podstawie treści artykułu:

Kod HTML jest ograniczony wyłącznie do zawartości między znacznikami <body> i </body>.
Treść artykułu jest strukturyzowana za pomocą odpowiednich znaczników HTML.
Miejsca na obrazy są wskazywane przez znaczniki <img> z opisem w atrybucie alt oraz krótkim podpisem poniżej obrazu.

Wyjście danych:
Wygenerowany kod HTML jest zapisywany w pliku artykul.html.

Komunikat końcowy:
Po zapisaniu pliku aplikacja wyświetla komunikat "Zakonczono sukcesem".
